from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router


load_dotenv()
app = FastAPI(title="Qdrant + SentenceTransformer API")

origins = [
    "http://localhost:3000",  # Next.js dev server
    "https://heliusdev.in" 

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello Parvez Alam from FastAPI!"}


app.include_router(router)