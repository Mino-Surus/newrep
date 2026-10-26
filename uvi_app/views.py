from django.shortcuts import render
from django.http import HttpResponse
from channels.layers import get_channel_layer

def main(request):
    return render(request, 'code.html')

async def send_message(request):
    message = request.GET.get('msg', '')
    
    layer = get_channel_layer()
    await layer.group_send(
        'messages',
        {
            'type': 'message.new',
            'text': message
        }
    )
    
    return HttpResponse(status=204)