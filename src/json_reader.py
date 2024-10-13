import json
from .internal_backend_types import User


class Json_DB:
    def __init__(self):
        self.customer_json_path = "data/customers_2.json"
        self.product_json_path = "data/products_2.json"
        self.sales_json_path = "data/sales_2.json"
        self.chat_history_path = "data/chat_history.json"

    # # # user # # #
    def _get_user_profile_folder(self, chat_id: str) -> str:
        return f"data/user_profiles/{chat_id}.json"

    def save_generated_users(
        self, chat_id: str, generated_user_data: list[User]
    ) -> None:
        with open(self._get_user_profile_folder(chat_id=chat_id), "w") as file:
            json.dump(generated_user_data, file)

    def get_generated_user(self, chat_id: str, user_id: int) -> User:
        with open(self._get_user_profile_folder(chat_id=chat_id), "r") as file:
            generated_users = json.load(file)
            for user in generated_users:
                if user_id == user["id"]:
                    return user

    # # # chat # # #
    def get_all_chats(self) -> dict[str, str] | None:
        with open(self.chat_history_path, "r") as file:
            return json.load(file)

    def get_chat_history(self, chat_id: str) -> dict[str, str] | None:
        return self.get_all_chats().get(str(chat_id), None)

    def update_chat_history(
        self,
        chat_id: str,
        new_chat_history: dict[str, str],
    ) -> None:
        chat_history = self.get_all_chats()

        # NOTE: this might not be the most efficient way because it rewrites the whole JSON everytime
        chat_history[chat_id] = new_chat_history

        with open(self.chat_history_path, "w") as file:
            json.dump(chat_history, file)

    # # # products # # #
    def get_product(self, product_id: str):
        with open(self.product_json_path, "r") as file:
            products = json.load(file)
            for product in products.values():
                if product_id == product["Uniqe Id"]:
                    return product


if __name__ == "__main__":
    db = Json_DB()
    # db.save_generated_users(
    #     chat_id="abc", generated_user_data=[{"sheesh": "dab", "id": 1}]
    # )
    # print(db.get_generated_user(chat_id="abc", user_id=1))
    db.update_chat_history(
        chat_id="hithere", new_chat_history=[{"user": "sheesh", "conrtent": "hi"}]
    )
