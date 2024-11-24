#!/usr/bin/env python
import argparse
import sys

from mistralai import Mistral
from mistralai.models import AssistantMessage, SystemMessage, UserMessage

DEFAULT_MODEL = "open-mistral-7b"
DEFAULT_TEMPERATURE = 0.7

class ChatBot:
    def __init__(
        self, api_key, model=DEFAULT_MODEL, system_message=None, temperature=DEFAULT_TEMPERATURE
    ):
        if not api_key:
            raise ValueError("An API key must be provided to use the Mistral API.")
        self.client = Mistral(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.system_message = system_message

    def new_chat(self):
        print("New Chat created")
        self.messages = []
        if self.system_message:
            self.messages.append(SystemMessage(content=self.system_message))

    def collect_user_input(self):
        return input()

    def run_inference(self, content):
        self.messages.append(UserMessage(content=content))

        if len(self.messages) > 10:
            self.messages = self.messages[-10:]

        assistant_response = ""
        for chunk in self.client.chat.stream(
            model=self.model, temperature=self.temperature, messages=self.messages
        ):
            response = chunk.data.choices[0].delta.content
            if response is not None:
                assistant_response += response

        if assistant_response:
            self.messages.append(AssistantMessage(content=assistant_response))
        
        return assistant_response

    def start(self):
        self.new_chat()
        while True:
            try:
                input = self.collect_user_input()
                assistant_response = self.run_inference(input)
            except KeyboardInterrupt:
                sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A simple chatbot using the Mistral API"
    )
    parser.add_argument(
        "--api-key",
        default="",
        help="Mistral API key. Defaults to environment variable MISTRAL_API_KEY",
    )
    parser.add_argument(
        "-s", "--system-message", help="Optional system message to prepend."
    )

    args = parser.parse_args()

    try:
        bot = ChatBot(args.api_key, system_message=args.system_message)
        bot.start()
    except Exception as e:
        sys.exit(1)