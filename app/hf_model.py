from sentence_transformers import SentenceTransformer

# Load from Hugging Face Hub (model not stored locally)
# model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def get_model():
    return SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def get_embedding(text: str):
    model = get_model()
    return model.encode(text).tolist()
