from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from evaluator.evaluate import LLM
from .external_backend_types import Generate_Evaluation_Body
from .json_reader import Json_DB
from uuid import uuid1
from evaluator.aggregate import average_rating, action_breakdown

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
    # product = db.get_product(req_body.pid)
    # chat_id = str(uuid1())

    # generated_users, chat_history = llm.generate_user_profiles(
    #     country=req_body.country, demographic=req_body.demographicTags
    # )

    # print("generated users")

    # all_user_evaluations, chat_history = llm.query_users(
    #     users_dict=generated_users,
    #     product_dict=product,
    #     history=chat_history,
    #     image_url=product.get("Image", None),
    # )
    # # store user evaluations for retrieval later
    # db.save_generated_users(chat_id=chat_id, generated_user_data=all_user_evaluations)

    # print("created user evaluations")

    # final_evaluation, chat_history = llm.generate_evaluation(chat_history)
    # # save final copy of chat history
    # db.update_chat_history(chat_id=chat_id, new_chat_history=chat_history)

    # avg_star_rating = average_rating(user_output=final_evaluation)
    # final_evaluation["avgStarRating"] = avg_star_rating

    # action_overview = average_rating(user_output=final_evaluation)
    # final_evaluation["actionBreakdown"] = action_overview

    # return final_evaluation

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
        "generated_reviews": [
            {
                "id": 1,
                "rating": 4,
                "explanation": "Takeshi would likely find the Martha Stewart Crafts Stencil Tape to be a useful tool for his various DIY projects. As an active individual who enjoys outdoor activities, he may use this tape to create custom stencils for decorating his hiking or camping gear, or even to add personalized designs to his sports equipment. The low-tack adhesive and ease of removal would appeal to Takeshi's practical nature, allowing him to experiment with different designs without causing any damage.",
                "improvement": "To make the product more appealing to Takeshi, it could be offered in a wider range of colors or patterns, allowing him to better coordinate with his outdoor gear and personal style. Additionally, including instructions or examples for using the stencil tape in outdoor-themed crafts and projects would further enhance its usefulness for this user.",
                "action": "purchase",
            },
            {
                "id": 2,
                "rating": 5,
                "explanation": "As an environmentally conscious individual, Emi would highly appreciate the Martha Stewart Crafts Stencil Tape. The low-tack adhesive and easy removability would allow her to experiment with various designs and patterns without causing any damage to the surfaces she applies them to, aligning with her sustainable mindset. Emi could use this tape to create custom stencils for her camping gear, outdoor apparel, or even for decorating her living space with nature-inspired motifs.",
                "improvement": "To make the product even more attractive to Emi, the manufacturer could consider offering a version of the stencil tape that is made from recycled or sustainable materials, further reinforcing its eco-friendly credentials.",
                "action": "purchase",
            },
            {
                "id": 3,
                "rating": 4,
                "explanation": "Ryuichi, as a physical education teacher, would find the Martha Stewart Crafts Stencil Tape useful for creating custom designs and decorations for his outdoor activities and sports equipment. The tape's ability to hold stencils securely in place and prevent paint bleeding would be valuable for Ryuichi, as he may use it to create personalized markings or logos for his students' sports gear or for decorating the equipment used in his outdoor classes.",
                "improvement": "To make the product more appealing to Ryuichi, the manufacturer could consider offering the stencil tape in a wider range of colors, allowing him to better match the designs with the specific sports or activities he is teaching. Additionally, providing educational resources or tutorials on how to use the tape for sports-related crafts and projects would further enhance its usefulness for this user.",
                "action": "purchase",
            },
            {
                "id": 4,
                "rating": 5,
                "explanation": "Yuki, as a college student studying outdoor recreation, would find the Martha Stewart Crafts Stencil Tape to be an invaluable tool for her various outdoor-themed projects and DIY activities. The low-tack adhesive and ease of removal would allow her to experiment with different designs and patterns on her hiking, mountain biking, and rock climbing gear, without worrying about any damage. Yuki could use the stencil tape to create customized decorations, logos, or even safety markings for her outdoor equipment.",
                "improvement": "To further enhance the product's appeal to Yuki, the manufacturer could consider offering the stencil tape in additional sizes or formats, allowing her to tackle a wider range of project sizes and shapes. Additionally, including a small collection of pre-made stencil designs inspired by nature or outdoor themes would be a helpful addition for this user.",
                "action": "purchase",
            },
            {
                "id": 5,
                "rating": 4,
                "explanation": "Hiroshi, as an outdoor enthusiast, would find the Martha Stewart Crafts Stencil Tape to be a useful tool for customizing his camping, hiking, and kayaking gear. The low-tack adhesive and easy removability would allow him to experiment with different designs and patterns without worrying about damaging his equipment. Hiroshi could use the stencil tape to create custom decorations, logos, or even labeling for his outdoor gear, enhancing both the functionality and personal touch of his equipment.",
                "improvement": "To make the product more appealing to Hiroshi, the manufacturer could consider offering the stencil tape in a wider range of colors, allowing him to better coordinate with the color schemes of his outdoor gear. Additionally, providing instructions or inspiration for using the tape to create outdoor-themed designs would further enhance its usefulness for this user.",
                "action": "purchase",
            },
            {
                "id": 6,
                "rating": 5,
                "explanation": "As an avid hiker and rock climber, Sakura would find the Martha Stewart Crafts Stencil Tape to be an extremely valuable tool for her outdoor activities. The low-tack adhesive and easy removability would allow her to experiment with different designs and patterns on her climbing gear, hiking equipment, and even her outdoor apparel without causing any damage. Sakura could use the stencil tape to create custom decorations, labels, or even safety markings for her gear, enhancing both the functionality and personalization of her outdoor equipment.",
                "improvement": "To further enhance the product's appeal to Sakura, the manufacturer could consider offering the stencil tape in a wider range of sizes or shapes, allowing her to tackle a greater variety of project scales and designs. Additionally, including a selection of pre-made stencil designs inspired by nature or outdoor themes would be a helpful addition for this user.",
                "action": "purchase",
            },
            {
                "id": 7,
                "rating": 4,
                "explanation": "Takumi, as an avid cyclist and hiker, would find the Martha Stewart Crafts Stencil Tape to be a useful tool for customizing his outdoor gear and equipment. The low-tack adhesive and easy removability would allow him to experiment with different designs and patterns on his bicycles, hiking backpacks, and other gear without causing any damage. Takumi could use the stencil tape to create personalized decorations, labels, or even safety markings for his outdoor equipment, enhancing both the functionality and visual appeal of his gear.",
                "improvement": "To make the product more appealing to Takumi, the manufacturer could consider offering the stencil tape in a wider range of colors or patterns, allowing him to better coordinate with the aesthetic of his outdoor gear. Additionally, providing instructions or inspiration for using the tape to create cycling or hiking-themed designs would further enhance its usefulness for this user.",
                "action": "purchase",
            },
            {
                "id": 8,
                "rating": 5,
                "explanation": "As an environmentally conscious college student studying outdoor recreation, Aiko would greatly appreciate the Martha Stewart Crafts Stencil Tape. The low-tack adhesive and easy removability would allow her to experiment with different eco-friendly designs and patterns on her hiking, camping, and skiing gear without causing any damage. Aiko could use the stencil tape to create personalized decorations, labels, or even safety markings for her outdoor equipment, all while maintaining a sustainable approach.",
                "improvement": "To further enhance the product's appeal to Aiko, the manufacturer could consider offering a version of the stencil tape that is made from recycled or sustainable materials, reinforcing its eco-friendly credentials. Additionally, providing a selection of pre-made stencil designs inspired by nature or outdoor themes would be a helpful addition for this user.",
                "action": "purchase",
            },
            {
                "id": 9,
                "rating": 4,
                "explanation": "Takahiro, as an avid hiker, mountain biker, and rock climber, would find the Martha Stewart Crafts Stencil Tape to be a valuable tool for customizing his outdoor gear and equipment. The low-tack adhesive and easy removability would allow him to experiment with different designs and patterns on his hiking backpacks, mountain bikes, and climbing gear without causing any damage. Takahiro could use the stencil tape to create personalized decorations, labels, or even safety markings for his outdoor equipment, enhancing both the functionality and visual appeal of his gear.",
                "improvement": "To make the product more appealing to Takahiro, the manufacturer could consider offering the stencil tape in a wider range of colors or patterns, allowing him to better coordinate with the aesthetic of his outdoor gear. Additionally, providing instructions or inspiration for using the tape to create designs inspired by nature or outdoor activities would further enhance its usefulness for this user.",
                "action": "purchase",
            },
            {
                "id": 10,
                "rating": 5,
                "explanation": "As an environmentally conscious college student studying environmental science, Emi would highly appreciate the Martha Stewart Crafts Stencil Tape. The low-tack adhesive and easy removability would allow her to experiment with different eco-friendly designs and patterns on her hiking, kayaking, and rock climbing gear without causing any damage. Emi could use the stencil tape to create personalized decorations, labels, or even safety markings for her outdoor equipment, all while promoting sustainable practices.",
                "improvement": "To further enhance the product's appeal to Emi, the manufacturer could consider offering a version of the stencil tape that is made from recycled or sustainable materials, reinforcing its eco-friendly credentials. Additionally, providing a selection of pre-made stencil designs inspired by nature or outdoor themes would be a helpful addition for this user.",
                "action": "purchase",
            },
        ],
    }
