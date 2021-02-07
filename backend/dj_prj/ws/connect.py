from channels.generic.websocket import WebsocketConsumer
import json

class ConnectConsumer(WebsocketConsumer):
    
    def connect(self):
        print('Connnect!!!')
        self.accept()
        self.send(text_data=json.dumps({ \
            'type': 'online:ping', \
            'payload': 'ping from server' \
            } \
        ))

    def disconnect(self, close_code):
        # Channel.objects.filter(name=self.channel_name).delete()
        print('DISCONNECT!!! ONLINE')

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
