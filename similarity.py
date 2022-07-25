from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


similarity_model_path = 'Maunish/ecomm-sbert'
model = SentenceTransformer(similarity_model_path)

def get_similarity(sentence1,sentence2):
    
    sentence1 = model.encode([sentence1])
    sentence2 = model.encode([sentence2])

    results = cosine_similarity(
        sentence1,
        sentence2)
    return results[0][0]

