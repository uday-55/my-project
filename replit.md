# AI-Enabled Value Chain Platform for Oilseed Self-Reliance

## Project Overview
This is a comprehensive web-based prototype platform designed to enhance India's oilseed self-reliance by connecting farmers, FPOs/processors, and policymakers through AI-powered analytics and blockchain-based traceability.

**Created:** October 22, 2025
**Technology Stack:** Flask (Python), HTML/CSS/JavaScript, Chart.js, Matplotlib, ReportLab

## Goal
Create a visually appealing, interactive, and informative prototype that demonstrates how AI and Blockchain can enhance India's oilseed self-reliance through smarter production, logistics, and policy decisions.

## Key Features

### 1. Three Role-Based Dashboards
- **Farmer Dashboard**: AI price prediction, crop advisory, selling interface, gamified badges, AI chatbot, **multilingual support (English/Hindi/Telugu/Tamil)**, **voice assistant**, **interactive map with farmers/buyers/warehouses**
- **FPO/Processor Dashboard**: Blockchain transaction log, warehouse management, Chart.js visualizations
- **Policymaker/Admin Dashboard**: National analytics, AI insights, logistics visualization, policy recommendations

### 2. AI Module (Simulated)
- Mock ML-based price prediction for 7 days ahead
- Matplotlib-generated price trend charts
- AI insight cards with market predictions
- AI Assistant chatbox with agricultural advisory responses

### 3. Blockchain Simulation
- Python-based blockchain with SHA-256 hashing
- Transaction records with farmer name, crop, price, quantity, timestamp
- Chain integrity verification
- Display on FPO and Admin dashboards

### 4. Data Visualizations
- Chart.js for interactive charts (warehouse capacity, crops by type, price trends, volume traded)
- Matplotlib for AI price prediction graphs
- Real-time chart updates

### 5. Gamified Badges System
- **Smart Seller** 💰: Achieved when selling at 10% above base price
- **High Volume Producer** 🌾: Earned for selling 1000+ kg
- **Loyal Member** ⭐: Given after 5+ transactions

### 6. AI Assistant Chatbox
- Predefined responses for common farmer queries
- Topics: pricing, weather, pests, fertilizers, subsidies, storage, insurance, quality, credit
- Real-time chat interface on farmer dashboard

### 7. PDF Report Generation
- Transaction reports with blockchain statistics
- Farmer performance reports with predictions and badges
- Uses ReportLab for professional PDF output

### 8. Multilingual Support
- Language selector with support for English, Hindi, Telugu, and Tamil
- Real-time interface translation
- Voice recognition in English and Hindi
- Inclusive design for farmers across India

### 9. Voice Assistant Integration
- Web Speech API for voice commands
- Voice-activated crop price prediction
- Text-to-speech feedback for transactions and predictions
- Voice input for AI chatbot queries
- Hands-free operation for farmers

### 10. Interactive Geographic Map
- Leaflet.js with OpenStreetMap integration
- 32 strategically placed locations across India:
  - 17 Farmers across North, South, East, West, and Central India
  - 7 Buyers in major processing hubs
  - 8 Warehouses/Storage facilities
- Visual markers with smooth animations:
  - 🟢 Farmers (green) - showing crop types and location
  - 🔵 Buyers (blue) - showing demand and location
  - 🟠 Marketplaces/Warehouses (orange) - showing capacity and location
- Advanced search functionality:
  - Search by name, type, location, crop, demand, or capacity
  - Auto-zoom to single results
  - Fit bounds for multiple results
  - Animated transitions with flyTo effects
- Interactive features:
  - Click markers to zoom in with smooth animation (1.5s duration)
  - Enhanced popups with location details, icons, and formatted info
  - Marker drop animations on load
  - Continuous pulse animations for visibility
  - Hover effects with scale transformation
- Responsive design matching dashboard theme
- Centered on India (lat: 20.5937, lng: 78.9629) with pan and zoom capabilities
- Map controls: zoom buttons, scroll wheel zoom, double-click zoom, touch zoom

## Project Structure

```
.
├── app.py                    # Main Flask application
├── blockchain.py             # Blockchain simulation module
├── ai_predictor.py          # AI price prediction and advisory
├── pdf_generator.py         # PDF report generation
├── templates/
│   ├── base.html            # Base template with navbar
│   ├── index.html           # Home page
│   ├── farmer.html          # Farmer dashboard
│   ├── fpo.html            # FPO dashboard
│   └── admin.html          # Admin dashboard
├── static/
│   ├── css/                # CSS files
│   └── js/                 # JavaScript files
└── replit.md               # This file
```

## API Endpoints

- `GET /` - Home page with role selection
- `GET /farmer` - Farmer dashboard
- `GET /fpo` - FPO/Processor dashboard
- `GET /admin` - Policymaker/Admin dashboard
- `POST /api/predict-price` - Get AI price predictions
- `POST /api/sell-crop` - Record crop sale on blockchain
- `POST /api/chat` - AI chatbot responses
- `GET /api/blockchain-status` - Blockchain validation status
- `GET /download-report` - Generate and download PDF reports

## Supported Crops
1. Soybean (Base price: ₹4,500/quintal)
2. Groundnut (Base price: ₹5,200/quintal)
3. Mustard (Base price: ₹6,000/quintal)
4. Sunflower (Base price: ₹5,800/quintal)

## Design Theme
- **Color Palette**: Green (#2ecc71, #27ae60), White, Light Brown, Blue gradients
- **Style**: Modern, responsive, nature-themed
- **UI Elements**: Cards with shadows, rounded corners, gradient backgrounds, icons from Font Awesome
- **Responsive**: Works on mobile and desktop devices

## How to Use

### For Farmers:
1. Visit the Farmer Dashboard
2. Select your crop type and view AI price predictions
3. Check crop advisory for weather, pest alerts, and farming tips
4. Enter your details and sell your crop to record it on the blockchain
5. Earn badges for smart selling decisions
6. Use the AI Assistant for farming advice
7. Download your performance report

### For FPOs:
1. Visit the FPO Dashboard
2. View all blockchain transactions from farmers
3. Monitor warehouse capacity utilization
4. Analyze crops procured by type
5. Manage forward contracts
6. Download comprehensive transaction reports

### For Policymakers:
1. Visit the Admin Dashboard
2. View national-level statistics and analytics
3. Read AI-generated market insights
4. Monitor price trends across different oilseeds
5. Review logistics and warehouse distribution
6. Get policy recommendations
7. Download national reports

## Running the Application
The application runs on port 5000 and is accessible via the webview.

## Future Enhancements
- Integrate real weather API for live crop advisory
- Connect to actual commodity price APIs
- Implement PostgreSQL for persistent storage
- Add multi-user authentication with role-based access
- Enhance AI with actual ML models (LSTM/Prophet)
- Real-time notifications for price alerts
- Mobile app development
- Multi-language support (Hindi, regional languages)

## Note
This is a prototype demonstration. All AI predictions and blockchain simulations use mock data for demonstration purposes. The platform showcases the potential of integrating AI and blockchain technology in agricultural value chains.
