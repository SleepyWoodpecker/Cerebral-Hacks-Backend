from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from evaluator.evaluate import LLM
from .external_backend_types import Generate_Evaluation_Body

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


@app.post("/generate-evaluation")
def generate_evaluation(req_body: Generate_Evaluation_Body):
    # user_profiles, response_history = llm.generate_user_profiles()
    # store chat history
    print(req_body.pid)
    print(req_body.country)
    print(req_body.tags)

    # # # # hard-coded feedback # # # #
    return {
        "avgStarRating": 5.0,
        "actionBreakdown": {"purchase": 20.0, "view": 50.0, "like": 30.0},
        "feedback": "Overall, the Martha Stewart Crafts Stencil Tape is a versatile and user-friendly product that allows users to create unique patterns and designs, with some room for improvement in terms of color and stencil options.",
        "positive": [
            "Versatility in creating designs and patterns",
            "Easy application and removal of the low-tack adhesive",
            "Ability to personalize projects and express individuality",
        ],
        "improvement": [
            "Offer a wider range of color and pattern options",
            "Provide more stencil design choices or the ability to create custom stencils",
            "Expand the product's appeal to users with different creative needs and styles",
        ],
        "keywords": [
            "versatile",
            "user-friendly",
            "unique",
            "personalize",
            "express individuality",
        ],
        "bestSeason": "spring",
    }


@app.get("/generate-explanation")
def generate_explanation(queryId: str, userId: str, userEvaluation: str):
    return queryId + " " + userId + " " + userEvaluation
