import requests

class ChatGPT:
    @staticmethod
    def response(prompt):

        openai_api_key = "API code"
        if openai_api_key is None:
            raise ValueError("OpenAI API key is not set in environment variables.")

        url = "https://api.openai.com/v1/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }

        data = {
            "model": "gpt-3.5-turbo-instruct",
            "prompt": prompt,
            "temperature": 0,
            "max_tokens": 1500,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        response = requests.post(url, headers=headers, json=data)

        # Check if the request was successful
        if response.status_code == 200:

            return response.json()['choices'][0]['text']
        else:
            print("Error:", response.status_code, response.text)

