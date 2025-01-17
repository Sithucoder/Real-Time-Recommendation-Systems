import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

# Load data
user_data = pd.read_csv('data/user_data.csv')
product_data = pd.read_csv('data/product_data.csv')

# Clean data (example: fill missing values)
product_data['description'].fillna('', inplace=True)

# Content-based Filtering: Extract TF-IDF Features
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(product_data['description'])

# Compute Similarity Matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend products based on product ID
def recommend_products(product_id, top_n=5):
    idx = product_data[product_data['product_id'] == product_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    product_indices = [i[0] for i in sim_scores]
    return product_data.iloc[product_indices][['product_id', 'title']]

# Example usage
print(recommend_products(101))


# Load user data for collaborative filtering
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(user_data[['user_id', 'product_id', 'rating']], reader)

# Train-Test Split
trainset, testset = train_test_split(data, test_size=0.25)

# Train SVD Model
model = SVD()
model.fit(trainset)

# Predict for a user and product
def recommend_for_user(user_id, top_n=5):
    all_products = user_data['product_id'].unique()
    predictions = [model.predict(user_id, pid) for pid in all_products]
    top_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)[:top_n]
    return [(pred.iid, pred.est) for pred in top_predictions]

# Example usage
print(recommend_for_user(1))
