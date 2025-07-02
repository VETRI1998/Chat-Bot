import json
import os
import string
import difflib
from channels.generic.websocket import AsyncWebsocketConsumer
from .dataset import dataset

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_message = data.get('message', '')

        # Get bot response from dataset
        bot_reply = self.get_response_from_dataset(user_message)

        await self.send(text_data=json.dumps({
            'message': bot_reply
        }))

    def normalize(self, text):
        # Lowercase and remove punctuation
        return text.lower().translate(str.maketrans('', '', string.punctuation))

    def get_response_from_dataset(self, message):
        normalized = self.normalize(message)
        keys = [self.normalize(k) for k in dataset.keys()]
        matches = difflib.get_close_matches(normalized, keys, n=1, cutoff=0.6)

        if matches:
            match_index = keys.index(matches[0])
            matched_key = list(dataset.keys())[match_index]
            return dataset[matched_key]

        return "I'm sorry, I didn't understand that."

