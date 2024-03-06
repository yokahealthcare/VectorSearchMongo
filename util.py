import os

import requests
import openai

hf_token = os.getenv('HF_TOKEN')
embedding_url = os.getenv("EMBEDDING_URL")


def generate_embedding_hf(text):
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text})

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()


openai.api_key = os.getenv("OPENAI_API")


def generate_embedding_openai(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response["data"][0]["embedding"]
