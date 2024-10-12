from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# TODO: change allowed cors origins, error handling

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/generate-evaluation")
def generate_evaluation(productName: str, customerFilter: str, productCategory: str):
    return productName + " " + customerFilter + " " + productCategory


@app.get("/generate-explanation")
def generate_explanation(queryId: str, userId: str, userEvaluation: str):
    return queryId + " " + userId + " " + userEvaluation
