from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from evaluator.evaluate import LLM

# TODO: change allowed cors origins, error handling

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = LLM()


@app.get("/generate-evaluation")
def generate_evaluation(productName: str, customerFilter: str, productCategory: str):
    user_profiles, response_history = llm.generate_user_profiles()

    # store chat history
    return productName + " " + customerFilter + " " + productCategory


@app.get("/generate-explanation")
def generate_explanation(queryId: str, userId: str, userEvaluation: str):
    return queryId + " " + userId + " " + userEvaluation
