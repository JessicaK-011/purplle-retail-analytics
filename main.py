from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Retail Analytics System"}

@app.get("/health")
def health():
    return {"status": "healthy"}