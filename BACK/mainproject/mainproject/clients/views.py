from django.http import JsonResponse
from .models import Client
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def client_list(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            clients = Client.objects.filter(responsible_person=request.user).values()
            return JsonResponse({'clients': list(clients)})
        else:
            return JsonResponse({'error': 'User is not authenticated'})
    
@csrf_exempt
def change_status(request, client_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        client = Client.objects.get(pk=client_id)
        new_status = data.get('new_status')

        client.status = new_status
        client.save()
        return JsonResponse({'success': 'Status changed successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'})