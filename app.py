from flask import Flask, render_template, request, jsonify, send_file, session
from blockchain import Blockchain
from ai_predictor import predict_price, generate_price_chart, get_crop_advisory, generate_ai_insights, get_ai_chat_response
from pdf_generator import generate_transaction_report, generate_farmer_report
import random
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'oilseed-value-chain-secret-key-2025')

blockchain = Blockchain()

farmer_data = {
    "badges": [],
    "total_sales": 0,
    "transactions": []
}

warehouse_data = {
    "capacity": 10000,
    "current_stock": 0,
    "crops": {}
}

def calculate_badges(price, crop_type, quantity):
    badges = []
    base_price = {"soybean": 4500, "groundnut": 5200, "mustard": 6000, "sunflower": 5800}
    
    if price >= base_price.get(crop_type, 5000) * 1.1:
        badges.append("Smart Seller 💰")
    
    if quantity >= 1000:
        badges.append("High Volume Producer 🌾")
    
    if len(farmer_data["transactions"]) >= 5:
        badges.append("Loyal Member ⭐")
    
    return badges

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/farmer')
def farmer_dashboard():
    return render_template('farmer.html')

@app.route('/fpo')
def fpo_dashboard():
    transactions = blockchain.get_all_transactions()
    stats = blockchain.get_statistics()
    return render_template('fpo.html', transactions=transactions, stats=stats, warehouse=warehouse_data)

@app.route('/admin')
def admin_dashboard():
    stats = blockchain.get_statistics()
    insights = generate_ai_insights(stats)
    transactions = blockchain.get_all_transactions()
    return render_template('admin.html', stats=stats, insights=insights, transactions=transactions)

@app.route('/test')
def test_page():
    return render_template('test_farmer.html')

@app.route('/api/predict-price', methods=['POST'])
def api_predict_price():
    data = request.json
    crop_type = data.get('crop_type', 'soybean')
    
    predictions = predict_price(crop_type)
    chart_image = generate_price_chart(crop_type, predictions)
    advisory = get_crop_advisory(crop_type)
    
    return jsonify({
        'predictions': predictions,
        'chart': chart_image,
        'advisory': advisory
    })

@app.route('/api/sell-crop', methods=['POST'])
def api_sell_crop():
    data = request.json
    farmer_name = data.get('farmer_name', 'Anonymous Farmer')
    crop_type = data.get('crop_type', 'soybean')
    quantity = float(data.get('quantity', 100))
    price = float(data.get('price', 5000))
    
    block = blockchain.add_transaction(farmer_name, crop_type, quantity, price)
    
    badges = calculate_badges(price, crop_type, quantity)
    farmer_data["badges"].extend(badges)
    farmer_data["badges"] = list(set(farmer_data["badges"]))
    farmer_data["total_sales"] += 1
    farmer_data["transactions"].append({
        "crop": crop_type,
        "quantity": quantity,
        "price": price
    })
    
    if crop_type in warehouse_data["crops"]:
        warehouse_data["crops"][crop_type] += quantity
    else:
        warehouse_data["crops"][crop_type] = quantity
    warehouse_data["current_stock"] += quantity
    
    return jsonify({
        'success': True,
        'block_hash': block.hash,
        'badges': farmer_data["badges"],
        'message': 'Transaction recorded on blockchain successfully!'
    })

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json
    user_message = data.get('message', '')
    
    response = get_ai_chat_response(user_message)
    
    return jsonify({
        'response': response
    })

@app.route('/api/blockchain-status')
def api_blockchain_status():
    return jsonify({
        'is_valid': blockchain.is_chain_valid(),
        'total_blocks': len(blockchain.chain),
        'latest_hash': blockchain.get_latest_block().hash
    })

@app.route('/download-report')
def download_report():
    report_type = request.args.get('type', 'transactions')
    
    if report_type == 'farmer' and farmer_data["transactions"]:
        last_transaction = farmer_data["transactions"][-1]
        predictions = predict_price(last_transaction["crop"])
        pdf_buffer = generate_farmer_report(
            "Farmer User",
            last_transaction["crop"],
            last_transaction["quantity"],
            last_transaction["price"],
            predictions,
            farmer_data["badges"]
        )
        return send_file(pdf_buffer, as_attachment=True, download_name='farmer_report.pdf', mimetype='application/pdf')
    else:
        pdf_buffer = generate_transaction_report(blockchain)
        return send_file(pdf_buffer, as_attachment=True, download_name='blockchain_report.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
