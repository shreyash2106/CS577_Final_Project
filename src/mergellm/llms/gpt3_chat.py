import os
import sys
import time

import openai
from openai import OpenAI

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class GPT3ChatModel:
    def __init__(self, model, temperature=0.7):
        with open(os.path.join(ROOT_DIR, "openai_key.txt"), "r") as f:
            key = f.readline().strip()
        self.client = OpenAI(api_key=key)
        self.model = model
        self.temperature = temperature

    def generate_response(self, prompt):
        response = None
        received = False
        while not received:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "user", "content": prompt},
                    ],
                    temperature=self.temperature,
                    stop=None,
                    max_tokens=1000,
                    n=1,
                )
                received = True
            except (openai.PermissionDeniedError, openai.AuthenticationError) as e:
                print("Permission Denied request:", e)
                time.sleep(1)
            except openai.APIConnectionError as e:
                print("API error occurred:", e)
                time.sleep(1)
            except openai.RateLimitError as e:
                print("Rate limit exceeded:", e)
                time.sleep(1)
            except Exception as e:
                print("Some other error occurred:", e)
                time.sleep(1)
        # print(response)
        if response:
            return response.choices[0].message.content
        return None
