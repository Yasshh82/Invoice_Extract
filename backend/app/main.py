from fastapi import FastAPI

app = FastAPI(title="Invoice AI API")


@app.get("/")
def root():
    return {"message": "Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}