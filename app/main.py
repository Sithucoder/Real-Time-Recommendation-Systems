from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load models and data (reuse code above for recommendation functions)
product_data = pd.read_csv('data/product_data.csv')

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_id = int(request.args.get('user_id'))
    recommendations = recommend_for_user(user_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
