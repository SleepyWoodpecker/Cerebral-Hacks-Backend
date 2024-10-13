import json
from uuid import uuid1
from src.internal_backend_types import User


class Json_DB:
    def __init__(self):
        self.customer_json_path = "data/customers_2.json"
        self.product_json_path = "../data/products_2.json"
        self.sales_json_path = "data/sales_2.json"
        self.chat_history_path = "test.json"

    def get_user(self, id: int) -> User | None:
        with open(self.customer_json_path, "r") as file:
            customer_data = json.load(file)
            chosen_customer = customer_data.get(str(id), None)
            return chosen_customer

    def get_all_chats(self) -> dict[str, str] | None:
        with open(self.chat_history_path, "r") as file:
            return json.load(file)

    def get_chat_history(self, chat_id: int) -> dict[str, str] | None:
        return self.get_all_chats().get(str(chat_id), None)

    def update_chat_history(
        self,
        new_chat_history: dict[str, str],
        chat_id: int | None = None,
    ) -> None:
        chat_history = self.get_all_chats()

        # NOTE: this might not be the most efficient way because it rewrites the whole JSON everytime
        if chat_id:
            chat_history[str(chat_id)] = new_chat_history
        else:
            new_chat_id = str(uuid1())
            chat_history[new_chat_id] = new_chat_history

        with open(self.chat_history_path, "w") as file:
            json.dump(chat_history, file)


if __name__ == "__main__":
    db = Json_DB()
    print(db.get_chat_history(1))
    db.update_chat_history([{"sheesh": "dab"}], 2)
