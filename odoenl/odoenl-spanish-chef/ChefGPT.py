from openai import OpenAI
from dotenv import load_dotenv
import os

INTRO = ["Welcome to ChefGPT!",
         "I am a Spanish chef specializing in the delicious cuisine of Valencia, Spain."]

PERSONALITY = "You are a young but very enthusiastic Spanish chef, specializing in the delicious cuisine of Valencia, Spain, your homeland. With a deep knowledge of local ingredients and traditional techniques, you are perfectly equipped to share the culinary secrets of the region. From preparing a recipe to creating innovative dishes that fuse tradition with modern touches, you offer personalized and passionate culinary advice. Your kindness and enthusiasm are reflected in every recommendation for those seeking to explore the unique flavors of Spain."
SCENARIO_1 = "If asked about the name of a dish, you provide the detailed recipe, including ingredients and cooking times for that dish."
SCENARIO_2 = "If ingredients are suggested to you, mention the names of Spanish dishes that can be made with those ingredients; it's not necessary to mention the recipes."
SCENARIO_3 = "If a detailed recipe is suggested to you, offer constructive critique with suggestions for improvement."
FALSY_INPUT = "If asked doesn't match these scenarios, politely decline and prompt for a valid request."
HELP = "You always asks how you can help more."

SYSTEM_CONFIG = [{"role": "system", "content": PERSONALITY},
                 {"role": "system", "content": SCENARIO_1},
                 {"role": "system", "content": SCENARIO_2},
                 {"role": "system", "content": SCENARIO_3},
                 {"role": "system", "content": FALSY_INPUT},
                 {"role": "system", "content": HELP}]

MODEL = "gpt-4o-mini"


def load_api_client():
    load_dotenv()
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def initialize_messages():
    return SYSTEM_CONFIG


def request_api(client, messages, stream=True):
    return client.chat.completions.create(model=MODEL, messages=messages, stream=stream)


def process_stream(stream):
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    return "".join(collected_messages)


def new_message(messages, role, content):
    messages.append({"role": role, "content": content})


def set_stream(client, messages):
    stream = request_api(client, messages)
    new_message(messages, "system", process_stream(stream))


def main():
    client = load_api_client()
    messages = initialize_messages()

    for line in INTRO: print(line)
    question = input("What can I help you with today?\n")

    new_message(messages, "user", question)
    set_stream(client, messages)

    while True:
        print("\n")
        new_message(messages, "user", input())
        set_stream(client, messages)


if __name__ == "__main__":
    main()
