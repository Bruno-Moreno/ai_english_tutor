import requests
import json


class Analyser:
    def __init__(self):
        self.model = "llama3"
        self.num_predict = 50
        self.messages = [
            {
                "role": "system",
                "content": """
                    You are an English teacher that helps correct grammar and explains mistakes simply.
                    First, you need to spot grammatical mistakes and highlight them if they exist. 
                    Then, you must answer the question of the student or continue the conversation with new questions.
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
        print(response_text)
        self.messages.append({"role": "assistant", "content": response_text})


if __name__ == "__main__":
    analyser = Analyser()
    analyser.generate_response("Hello! wat is your name?")
    for _ in range(3):
        analyser.generate_response(input("Response: "))
