
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from snippets.consumers import SnippetConsumer


application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/code_snippet/", SnippetConsumer)
    ])
})
