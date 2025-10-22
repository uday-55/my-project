import random
from datetime import datetime, timedelta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

CROP_BASE_PRICES = {
    "soybean": 4500,
    "groundnut": 5200,
    "mustard": 6000,
    "sunflower": 5800
}

def predict_price(crop_type, days=7):
    base_price = CROP_BASE_PRICES.get(crop_type.lower(), 5000)
    
    predictions = []
    current_price = base_price
    
    for i in range(days):
        date = datetime.now() + timedelta(days=i)
        
        volatility = random.uniform(-0.03, 0.05)
        seasonal_factor = 0.02 * (i % 3 - 1)
        trend = 0.01
        
        price_change = current_price * (volatility + seasonal_factor + trend)
        current_price = max(current_price + price_change, base_price * 0.8)
        
        predictions.append({
            "date": date.strftime("%Y-%m-%d"),
            "price": round(current_price, 2)
        })
    
    return predictions

def generate_price_chart(crop_type, predictions):
    dates = [p["date"] for p in predictions]
    prices = [p["price"] for p in predictions]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o', linewidth=2, markersize=8, color='#2ecc71')
    plt.fill_between(range(len(dates)), prices, alpha=0.3, color='#2ecc71')
    plt.title(f'{crop_type.capitalize()} Price Prediction - Next 7 Days', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=11)
    plt.ylabel('Price (₹/quintal)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=100, bbox_inches='tight')
    img.seek(0)
    plt.close()
    
    return base64.b64encode(img.getvalue()).decode()

def get_crop_advisory(crop_type):
    advisories = {
        "soybean": {
            "weather": "Moderate rainfall expected. Good for growth.",
            "pest_risk": "Low risk of pod borer. Monitor regularly.",
            "sowing_time": "Best: June-July (Kharif season)",
            "harvest_time": "October-November",
            "tips": "Ensure proper drainage to prevent waterlogging"
        },
        "groundnut": {
            "weather": "Warm and humid conditions favorable.",
            "pest_risk": "Medium risk of leaf miner. Use neem spray.",
            "sowing_time": "Best: May-June (Kharif) or Nov-Dec (Rabi)",
            "harvest_time": "September-October (Kharif) or March-April (Rabi)",
            "tips": "Calcium application improves pod development"
        },
        "mustard": {
            "weather": "Cool weather optimal. Avoid frost.",
            "pest_risk": "Aphid alert! Monitor and use organic pesticides.",
            "sowing_time": "Best: October-November (Rabi season)",
            "harvest_time": "February-March",
            "tips": "Light irrigation needed during pod formation"
        },
        "sunflower": {
            "weather": "Sunny conditions ideal. Drought resistant.",
            "pest_risk": "Low pest pressure. Watch for caterpillars.",
            "sowing_time": "Best: January-February or June-July",
            "harvest_time": "April-May or October-November",
            "tips": "Ensure adequate phosphorus for better yield"
        }
    }
    
    return advisories.get(crop_type.lower(), advisories["soybean"])

def generate_ai_insights(stats):
    insights = []
    
    if stats["total_transactions"] > 10:
        insights.append({
            "type": "success",
            "message": f"Platform activity is strong with {stats['total_transactions']} transactions completed!"
        })
    
    if "mustard" in stats["crops_summary"]:
        insights.append({
            "type": "info",
            "message": "Mustard oil prices expected to rise by 5% next week due to increased demand."
        })
    
    if "soybean" in stats["crops_summary"]:
        insights.append({
            "type": "warning",
            "message": "Soybean output may be affected by delayed monsoon in some regions."
        })
    
    insights.append({
        "type": "info",
        "message": "Government procurement at MSP available for all major oilseeds."
    })
    
    insights.append({
        "type": "success",
        "message": "FPO network expansion improving farmer access to better prices by 15%."
    })
    
    return insights

def get_ai_chat_response(user_message):
    message_lower = user_message.lower()
    
    responses = {
        "price": "Current oilseed prices are competitive! Check the price prediction chart for upcoming trends. Selling during peak demand periods can increase your profits by 10-15%.",
        "weather": "Weather conditions are favorable for most oilseed crops this season. However, ensure proper drainage and monitor for unexpected rainfall.",
        "pest": "For pest management, use integrated pest management (IPM) techniques. Neem-based organic pesticides are effective and eco-friendly. Regular field monitoring is key!",
        "fertilizer": "For optimal oilseed yield, use balanced NPK fertilizers. Phosphorus is especially important for groundnut and sunflower. Consider soil testing for precise application.",
        "sell": "The best time to sell depends on market demand and storage capacity. Use our AI price predictor to identify optimal selling windows. Consider forward contracts with FPOs for price security.",
        "subsidy": "Government subsidies are available for quality seeds, organic farming, and mechanization. Visit your nearest agriculture office or FPO for details on PM-KUSUM and other schemes.",
        "storage": "Proper storage is crucial! Ensure moisture content is below 8-10% before storage. Use clean, dry warehouses and check for pest infestation regularly.",
        "insurance": "Pradhan Mantri Fasal Bima Yojana (PMFBY) covers oilseed crops. Enroll during sowing season for comprehensive risk coverage at subsidized premiums.",
        "quality": "Maintain quality by: proper drying, clean storage, avoiding mixing varieties, and timely harvesting. Quality premium can fetch you 10-20% higher prices!",
        "credit": "Kisan Credit Cards offer easy access to crop loans at low interest rates. FPOs also provide credit facilities. Contact your nearest bank or FPO for assistance."
    }
    
    for keyword, response in responses.items():
        if keyword in message_lower:
            return response
    
    return "I'm here to help with oilseed farming, pricing, weather, pest management, and market insights. Try asking about prices, weather conditions, pest control, or selling strategies!"
