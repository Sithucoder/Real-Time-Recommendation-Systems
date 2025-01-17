import pandas as pd

def recommend_products(user_id, user_data, product_data):
    # Dummy recommendation logic: return top 5 products
    return product_data.head(5).to_dict(orient='records')

