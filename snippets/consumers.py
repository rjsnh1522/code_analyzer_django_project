import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class SnippetConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        name = "snippet"
        self.room_name = name
        self.room_group_name = 'snippet_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def code_language(self, event):
        print(event)
        msg = event['message']
        await self.send(text_data=json.dumps({
            'type': 'code_lang',
            'result': msg,
        }))


    # async def receive(self, text_data=None, bytes_data=None, **kwargs):
    #     import ipdb; ipdb.set_trace()
    #     # print(f"in save info before group_send----- {self.room_group_name} and data - {data}")
    #     # await self.channel_layer.group_send(
    #     #     self.room_group_name,
    #     #     {
    #     #         'type': 'train_message',
    #     #         'message': data,
    #     #     }
    #     # )
