from sentence_transformers import SentenceTransformer

# Load from Hugging Face Hub (model not stored locally)
# model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def get_model():
    return SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def get_embedding(text: str):
    print(f"Generating embedding for text: {text[:50]}...")  # Print first 50 chars for context
    if not text:
        print("Empty text provided, returning empty vector.")
        return []
    model = get_model()
    print("Model loaded successfully.")
    if not model:
        print("Model not loaded, returning empty vector.")
        return []
    
    vector=model.encode(text).tolist()
    print(f"Generated embedding vector of length {len(vector)}")
    return vector
