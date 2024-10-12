import anthropic

class LLM():
    def __init__(self, model_name = "claude-3-haiku-20240307", data_path = "data/data.json"):
        self.model_name = model_name
        try:
            self.client = anthropic.Anthropic()
            print("Successfully Connected to Anthropic API")
        except:
            print("Connection Error")
        with open(data_path, 'r') as f:
            self.data = f.read()

    def generate_user_profiles(self, n_users=10):
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
        """
        history = [
            {"role": 'user', "content": prompt}
        ]
        response = self._send_message(history)
        history.append({'role':'assistant', 'content': response})
        return response, history
        
    
    def queryUsers(self, users_dict: list, product_dict: dict, history: list):
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
"liked": list of str (a description in a list in point form, on what the user liked),
"disliked": list of str (a description in a list in point form, on what the user disliked)
}},
... (rest of the users)
]
"""
        history.append({"role": 'user', "content":  prompt})
        response = self._send_message(history)
        history.append({'role':'assistant', 'content': response})
        return response, history

    def generate_summary(self):
        prompt = f"""
Imagine you are a sales consultant, and you are provided with the following sales data on electronics, in JSON format:

<json>
{self.data}
</json>

Generate a summary of this data.
"""
        return self._send_message([{"role": 'user', "content":  prompt}])

    def _send_message(self, history):
        response = self.client.messages.create(
            model=self.model_name,
            max_tokens=2048,
            messages=history
        ).content[0].text
        return response
