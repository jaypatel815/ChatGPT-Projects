import config
import openai

openai.api_key = config.api_key

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {
            "role": "user",
            "content": "Can you please code an example of a portfolio website"
        }
    ]
)

print(completion.choices[0].message.content)
