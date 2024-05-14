#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from qkchat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                    url(r'^messages/(?P<username>[\w.@+-]+)/$', ChatConsumer),    
            ])
        )
    )
})