from channels.generic.websocket import AsyncWebsocketConsumer

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'messages',
            self.channel_name
        )
        await self.accept()
        
    async def disconnect(self, code: int) -> None:
        await self.channel_layer.group_discard(
            'messages',
            self.channel_name
        )
        return await super().disconnect(code)
    
    async def message_new(self, event):
        message = event['text']
        await self.send(message)