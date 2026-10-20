import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from uvi_app.websocket_routing import router
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uvicorn_pr.settings')
django_app = get_asgi_application()
application = ProtocolTypeRouter(
    {
        'http': django_app,
        'websocket': router
    }
)
# django channels uvicorn[standard]