import anthropic
import os

class LLM():
    def __init__(self, model_name = "claude-3-haiku-20240307"):
        self.model_name = model_name
        self.history = []
        try:
            self.client = anthropic.Anthropic()
            print("Successfully Connected to Anthropic API")
        except:
            print("Connection Error")
        self.generate_prompt()
        
    def generate_summary(self):
        return self._send_message(self.prompt)

    

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
    

    def generate_prompt(self, path = "./data/data.json"):

        data = ""
        with open(path, 'r') as f:
            data = f.read()
        self.prompt = f"""
Imagine you are a sales consultant, and you are provided with the following sales data on electronics, in JSON format:

<json>
{data}
</json>

Generate a summary of this data.
"""