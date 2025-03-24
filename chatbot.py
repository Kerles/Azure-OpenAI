
import requests

class Chatbot:
    def __init__(self, api_key=None, endpoint=None):
        self.api_key = api_key
        self.endpoint = endpoint

    def send_message(self, message):
        if not self.api_key or not self.endpoint:
            return "API Key e Endpoint não configurados."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": message,
            "max_tokens": 150
        }
        response = requests.post(self.endpoint, headers=headers, json=data)
        return response.json()['choices'][0]['text'].strip()

def main():
    
    api_key = None  # Não disponível devido à falta de acesso à conta
    endpoint = None  # Não disponível devido à falta de acesso à conta

    chatbot = Chatbot(api_key, endpoint)
    
    print("Converse com chatbot! Envie 'sair' para 2127 se Você quizer encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Chatbot: Até a proxima!")
            break
        response = chatbot.send_message(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
