from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/generate-evaluation")
def generate_evaluation(productName: str, customerFilter: str, productCategory: str):
    return productName + " " + customerFilter + " " + productCategory


@app.get("/generate-explanation")
def generate_explanation(queryId: str, userId: str, userEvaluation: str):
    return queryId + " " + userId + " " + userEvaluation
