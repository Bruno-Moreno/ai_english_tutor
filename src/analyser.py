import requests
import json


def print_analyser_text(text):
    print(f"\n\033[34m{text}\033[0m")


class Analyser:
    def __init__(self, model):
        self.model = model
        self.num_predict = 50
        self.messages = [
            {
                "role": "system",
                "content": """
                You are an English teacher that helps correct grammar and explains mistakes simply.
                If you spot a grammatical mistake, write the corrected version in brackets and explains why it is an error.
                Then, you must continue the conversation with the student.
                """,
            }
        ]

    def generate_response(self, prompt):
        self.messages.append({"role": "user", "content": prompt})

        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": self.model,
                "messages": self.messages,
                "num_predict": self.num_predict,
            },
        )
        response_text = ""
        for line in response.iter_lines():
            response_text += json.loads(line.decode())["message"]["content"]
        print_analyser_text(response_text)
        self.messages.append({"role": "assistant", "content": response_text})


if __name__ == "__main__":
    analyser = Analyser()
    analyser.generate_response("Hello! wat is you name?")
    for _ in range(3):
        analyser.generate_response(input("Response: "))
