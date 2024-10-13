import anthropic
import base64
import httpx
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class LLM:
    def __init__(
        self, model_name="claude-3-haiku-20240307", data_path="data/data.json"
    ):
        self.model_name = model_name
        try:
            self.client = anthropic.Anthropic(
                api_key=os.environ.get("ANTHROPIC_API_KEY"),
            )
            print("Successfully Connected to Anthropic API")
        except:
            print("Connection Error")
        with open(data_path, "r") as f:
            self.data = f.read()

    def generate_user_profiles(self, country: str, demographic: list[str], n_users=10):
        prompt = f"""
You are given a dataset of user demographics and their purchasing habits as follows:

<json>
{self.data}
</json>

From this distribution, generate {n_users} synthetic user profiles in a JSON format, as follows:

<json>
[
{{
"id": 1
"age": int,
"gender": "Male" or "Female",
"location": string,
"user_description": a string describing an instance of a user living in the location specified, given the purchasing habits in the dataset. Be more detailed.
    
}},
...
]
</json>
Only return the JSON, and nothing else.
All users should be from {country}.
Ensure that the users generated are sufficiently diverse to represent the demographic of {country}, with a slight focus on the following traits:
{demographic} 
You must format the output as proper JSON (i.e. close all curly brackets).
"""
        return self._send_message(prompt, [])

    def query_users(
        self, users_dict: list, product_dict: dict, history: list, image_url=None
    ):
        prompt = f"""
For the users below:

{users_dict}

For each user, how would you rate and review the following product?

{product_dict}

Return a JSON output only, and nothing else. The format is as follows:

[
{{
"id": int,
"rating": int (out of 5 stars),
"explanation": str,
"improvement": str (describing what changes to the product can be made to make it more attractive to this user),
"action": str (should be from the following options: view, like, purchase) based on how the user will likely interact with the product,
}},
... (rest of the users)
]

You must format the output as proper JSON (i.e. close all curly brackets).
"""

        content = [
            {"type": "text", "text": prompt},
        ]
        if image_url != None:
            image_media_type = "image/jpeg"
            image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")
            content.append(
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                    },
                }
            )
            content.append(
                {
                    "type": "text",
                    "text": "This is how the product looks like. Use this in your product evaluations for each user.",
                }
            )
        return self._send_message(content, history)

    def generate_evaluation(self, history):

        prompt = """
You have previously generated a list of users with their responses to the given product.

Now, summarize the responses of all the users into a single JSON file, as follows

{{
"feedback": str (a brief 1-sentence summary, not more than 250 characters, of all the user responses. i.e., "what most users say about this product"),
"positive": list of str (3 good points about the product, each point being less than 100 characters),
"improvement": list of str (3 points for improvements for the product, each point being less than 100 characters),
}}

You must format the output as proper JSON (i.e. close all curly brackets).

"""
        return self._send_message(prompt, history)


    def generate_new_description(self, history):
        # Must be run after generate_evaluation (results saved in history)

        prompt = """
Based on the data you have received, and what you have generated so far,
generate a new product description to better cater to the needs
of this specific demographic (eg. country, age, etc. ) based on cultural awareness
and understanding of the age group and their purchasing habits.

You may choose to cater to a specific subgroup of the demographic who are most likely to purchase the product.

There is no need to mention the country name in your description.

Limit the description to not more than 300 characters.        
        """
        return self._send_message(prompt, history)

    def _send_message(self, content, history):
        history.append({"role": "user", "content": content})
        response = (
            self.client.messages.create(
                model=self.model_name, max_tokens=4096, messages=history
            )
            .content[0]
            .text
        )
        history.append({"role": "assistant", "content": response})
        return response, history
