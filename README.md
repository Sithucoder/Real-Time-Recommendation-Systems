# Real-Time Recommendation System

This project implements a real-time recommendation system for an e-commerce platform using collaborative filtering and content-based filtering techniques.

## Features
- Recommends products based on user activity (browsing and purchase history).
- Implements both collaborative and content-based filtering.
- Live updates via a simple web interface.

## Setup Instructions

### Prerequisites
- Python 3.8 or later
- Pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sithucoder/Real-Time-Recommendation-Systems.git
   cd Real-Time-Recommendation-Systems
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Navigate to the `app` directory and run the Flask server:
   ```bash
   cd app
   python main.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000` to view the app.

### Usage
- Modify `user_data.csv` and `product_data.csv` in the `data/` folder to add your data.
- Access the endpoint `/recommendations?user_id=<id>` to get recommendations for a specific user.

### Repository Structure
```
Real-Time-Recommendation-Systems/
├── app/                     # Flask application
├── data/                    # Sample data
├── notebooks/               # Model building notebook
├── requirements.txt         # Dependencies
└── README.md                # Project instructions
```

### Technologies Used
- Python
- Flask
- Surprise Library
- Scikit-learn
- HTML/CSS for frontend

### Future Improvements
- Add user authentication.
- Deploy the system on a cloud platform (e.g., AWS, Heroku).
- Integrate WebSockets for faster updates.

### License
MIT License
