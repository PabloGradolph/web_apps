import openai
import base64
import os

# Retrieve the API key from the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key is None:
    raise ValueError("No OpenAI API key found in environment variables")

def gpt4_vision(image):

    # Convert the image to the format required by GPT-4 (e.g., Base64 encoding)
    with open(image, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode('utf-8')

    client = openai.OpenAI(api_key = openai_api_key)

    template = """
        {
            "recipe": {
                "name": "",
                "ingredients": [],
                "steps": []
            },
            "recipe": {
                "name": "",
                "ingredients": [],
                "steps": []
            }
        }
        """

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"What can I cook with the following image? The output string must be correctly formatted as JSON, this means using double quotes for strings and following JSON syntax rules. Take this as a template: {template}"},
                    {
                        "image": encoded_image
                    },
                ],
            }
        ],
        max_tokens=500,
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content