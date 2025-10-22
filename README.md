# 🌾 AI-Enabled Value Chain Platform for Oilseed Self-Reliance

A comprehensive web-based prototype platform designed to enhance India's oilseed self-reliance by connecting farmers, FPOs/processors, and policymakers through AI-powered analytics and blockchain-based traceability.

## 🎯 Project Goal

Create a visually appealing, interactive, and informative prototype that demonstrates how AI and Blockchain can enhance India's oilseed self-reliance through smarter production, logistics, and policy decisions.

## ✨ Key Features

### 🚜 Farmer Dashboard
- **AI Price Predictor**: 7-day price forecasting with interactive charts
- **Crop Advisory**: Weather alerts, pest warnings, sowing/harvest recommendations
- **Smart Selling**: Record crop sales on blockchain
- **Gamified Badges**: Earn achievements for smart decisions
  - 💰 Smart Seller (selling 10% above base price)
  - 🌾 High Volume Producer (1000+ kg sold)
  - ⭐ Loyal Member (5+ transactions)
- **AI Assistant**: Real-time chatbot for farming advice
- **PDF Reports**: Download personalized performance reports

### 🏭 FPO/Processor Dashboard
- **Blockchain Transaction Log**: Complete transaction history with verification
- **Warehouse Management**: Capacity monitoring and utilization
- **Procurement Analytics**: Chart.js visualizations
  - Crops by type
  - Warehouse capacity pie chart
- **Forward Contracts**: Manage procurement agreements
- **PDF Reports**: Export comprehensive transaction summaries

### 📊 Policymaker/Admin Dashboard
- **National Analytics**: Transaction volume, total value, and statistics
- **AI-Generated Insights**: Market predictions and policy recommendations
- **Price Trend Analysis**: Multi-crop comparative charts
- **Logistics Visualization**: Regional warehouse distribution map
- **Volume Tracking**: Daily trading volume analytics
- **Policy Recommendations**: Short-term and long-term strategies

## 🛠️ Technology Stack

- **Backend**: Flask (Python 3.11)
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualizations**: Chart.js, Matplotlib
- **PDF Generation**: ReportLab
- **Blockchain**: Custom Python implementation with SHA-256
- **UI Framework**: Custom responsive CSS with gradient themes

## 🎨 Design Theme

- **Color Palette**: Green (#2ecc71, #27ae60), gradient backgrounds
- **Style**: Modern, nature-themed, eco-friendly
- **Icons**: Font Awesome
- **Responsive**: Mobile and desktop optimized

## 🌱 Supported Crops

1. **Soybean** - Base price: ₹4,500/quintal
2. **Groundnut** - Base price: ₹5,200/quintal
3. **Mustard** - Base price: ₹6,000/quintal
4. **Sunflower** - Base price: ₹5,800/quintal

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Flask and dependencies (automatically installed)

### Running the Application
The application is already configured and running on port 5000. Simply access it through your browser.

### Navigation
- **Home**: `/` - Choose your role (Farmer, FPO, Policymaker)
- **Farmer Dashboard**: `/farmer`
- **FPO Dashboard**: `/fpo`
- **Admin Dashboard**: `/admin`

## 📡 API Endpoints

- `POST /api/predict-price` - Get AI price predictions
- `POST /api/sell-crop` - Record crop sale on blockchain
- `POST /api/chat` - AI chatbot responses
- `GET /api/blockchain-status` - Blockchain validation
- `GET /download-report` - Generate PDF reports

## 💡 How to Use

### For Farmers:
1. Navigate to Farmer Dashboard
2. Select crop type and view AI price predictions
3. Review crop advisory (weather, pests, tips)
4. Enter details to sell your crop
5. Earn badges for smart selling
6. Chat with AI Assistant for farming advice
7. Download your performance report

### For FPOs:
1. Navigate to FPO Dashboard
2. View all blockchain transactions
3. Monitor warehouse capacity
4. Analyze procurement by crop type
5. Manage forward contracts
6. Download transaction reports

### For Policymakers:
1. Navigate to Admin Dashboard
2. View national-level statistics
3. Review AI-generated insights
4. Monitor price trends
5. Analyze logistics distribution
6. Get policy recommendations
7. Download national reports

## 🔐 Blockchain Features

- SHA-256 cryptographic hashing
- Immutable transaction records
- Chain integrity verification
- Complete audit trail
- Transparent and secure

## 🤖 AI Capabilities

- Mock ML-based price prediction
- 7-day forecasting with volatility modeling
- Crop-specific advisory generation
- Market insights and recommendations
- Intelligent chatbot responses

## 📱 Responsive Design

The platform is fully responsive and works seamlessly on:
- Desktop computers
- Tablets
- Mobile devices

## 📈 Future Enhancements

- Real weather API integration
- Live commodity price feeds
- PostgreSQL database for persistence
- Multi-user authentication
- Actual ML models (LSTM/Prophet)
- Real-time price alerts
- Mobile app development
- Multi-language support (Hindi, regional languages)

## 🇮🇳 Impact

This platform aims to reduce India's edible oil imports from the current 55-60% by:
- Optimizing farmer pricing decisions
- Improving supply chain transparency
- Enabling data-driven policy making
- Connecting all stakeholders efficiently

## 📝 Note

This is a **prototype demonstration**. All AI predictions and blockchain simulations use mock data for demonstration purposes. The platform showcases the potential of integrating AI and blockchain technology in agricultural value chains.

## 📄 License

This project is created for educational and demonstration purposes.

---

**Created with 🌱 for India's Oilseed Self-Reliance Initiative**
