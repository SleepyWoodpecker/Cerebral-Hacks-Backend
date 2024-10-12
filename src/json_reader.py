import json
from backend_types import User


class Json_DB:
    def __init__(self):
        self.customer_json_path = "data/customers_2.json"
        self.product_json_path = "../data/products_2.json"
        self.sales_json_path = "data/sales_2.json"
        self.chat_history_path = "data/chat_history.json"

    def get_user(self, id: int) -> User | None:
        with open(self.customer_json_path, "r") as file:
            customer_data = json.load(file)
            chosen_customer = customer_data.get(str(id), None)
            return chosen_customer


if __name__ == "__main__":
    db = Json_DB()
    print(db.get_user(1))
