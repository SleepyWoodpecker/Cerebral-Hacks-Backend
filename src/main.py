from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from evaluator.evaluate import LLM
from external_backend_types import Generate_Evaluation_Body

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
        "feedback": "Overall, the users find the Martha Stewart Crafts Stencil Tape to be a versatile and useful product for creating unique designs and patterns. They appreciate the low-tack adhesive and ease of application and removal, which allows for experimentation and customization. However, some users express a desire for a wider selection of stencil designs and patterns to cater to different styles and preferences.",
        "positive": "The users highlight the product's ability to create customized designs, its easy application and removal, and its potential for use in various creative projects, such as home decor and fashion design.",
        "improvement": "The limited selection of stencil designs is the main concern expressed by the users, as they would like to have more options to choose from to accommodate their individual styles and needs.",
        "keywords": [
            "low-tack adhesive",
            "customization",
            "versatile",
            "easy to use",
            "home decor",
            "fashion design",
            "limited selection",
        ],
        "bestSeason": "Spring and Fall",
    }


@app.get("/generate-explanation")
def generate_explanation(queryId: str, userId: str, userEvaluation: str):
    return queryId + " " + userId + " " + userEvaluation
