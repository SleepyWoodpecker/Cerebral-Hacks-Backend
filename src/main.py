from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from evaluator.evaluate import LLM
from .external_backend_types import Generate_Evaluation_Body
from .json_reader import Json_DB
from uuid import uuid1

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
db = Json_DB()


@app.post("/generate-evaluation")
def generate_evaluation(req_body: Generate_Evaluation_Body):
    """
    1. generate user profiles (hardcoded)
    2. queryUsers based on single product and
    3. evaluate
    """
    product = db.get_product(req_body.pid)
    chat_id = uuid1()

    generated_users, chat_history = llm.generate_user_profiles(
        country=req_body.country, demographic=req_body.demographicTags
    )

    all_user_evaluations, chat_history = llm.queryUsers(
        users_dict=generated_users,
        product_dict=product,
        history=chat_history,
        image_url=product.get("Image", None),
    )
    # store user evaluations for retrieval later
    db.save_generated_users(chat_id=chat_id, generated_user_data=all_user_evaluations)

    final_evaluation = llm.generate_evaluation(chat_history)

    return final_evaluation

    # # # # hard-coded feedback # # # #
    # return {
    #     "avgStarRating": 5.0,
    #     "actionBreakdown": {"purchase": 20.0, "view": 50.0, "like": 30.0},
    #     "feedback": "Overall, the Martha Stewart Crafts Stencil Tape is a versatile and user-friendly product that allows users to create unique patterns and designs, with some room for improvement in terms of color and stencil options.",
    #     "positive": [
    #         "Versatility in creating designs and patterns",
    #         "Easy application and removal of the low-tack adhesive",
    #         "Ability to personalize projects and express individuality",
    #     ],
    #     "improvement": [
    #         "Offer a wider range of color and pattern options",
    #         "Provide more stencil design choices or the ability to create custom stencils",
    #         "Expand the product's appeal to users with different creative needs and styles",
    #     ],
    #     "keywords": [
    #         "versatile",
    #         "user-friendly",
    #         "unique",
    #         "personalize",
    #         "express individuality",
    #     ],
    #     "bestSeason": "spring",
    # }


@app.get("/generate-explanation")
def generate_explanation(chatId: str, userId: int):
    return db.get_generated_user(chat_id=chatId, user_id=userId)
