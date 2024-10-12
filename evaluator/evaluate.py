import anthropic

class LLM():
    def __init__(self, model_name = "claude-3-haiku-20240307", data_path = "data/data.json"):
        self.model_name = model_name
        self.history = []
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
"user_description": a string describing an instance of a user living in the location specified, given the purchasing habits in the dataset
    
}},
...
]
</json>
Only return the JSON, and nothing else.
        """
        return self._send_message(prompt)
        
    def generate_summary(self):
        prompt = f"""
Imagine you are a sales consultant, and you are provided with the following sales data on electronics, in JSON format:

<json>
{self.data}
</json>

Generate a summary of this data.
"""
        return self._send_message(prompt)

    def _send_message(self, content, new_message = True):
        if new_message:
            self.history = [{"role": 'user', "content":  content}]
        else:
            self.history.append({"role": 'user', "content":  content})
        response = self.client.messages.create(
            model=self.model_name,
            max_tokens=2048,
            messages=self.history
        ).content[0].text
        self.history.append({'role':'assistant', 'content': response})
        return response
