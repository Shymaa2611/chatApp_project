from channels.routing import route 
from . import consumers

channel_routing = [
	route('websocket.connect',consumers.connet, path=r'^/chat/$'),
	route('websocket.receive',consumers.receive_message, path=r'^/chat/$'),
	route('websocket.disconnect',consumers.disconnect, path=r'^/chat/$')

]