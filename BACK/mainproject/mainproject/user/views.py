from django.http import JsonResponse
from django.contrib.auth import authenticate, login as django_login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import CustomUser
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # Получаем данные из тела запроса в формате JSON
        data = json.loads(request.body)
        
        # Проверяем наличие всех обязательных полей в данных
        if 'full_name' not in data or 'username' not in data or 'password' not in data:
            return JsonResponse({'error': 'Please provide all required fields'}, status=400)
        
        # Извлекаем данные о пользователе из запроса
        full_name = data['full_name']
        username = data['username']
        password = data['password']
        
        # Создаем нового пользователя
        try:
            user = CustomUser.objects.create_user(full_name=full_name, username=username, password=password)
            return JsonResponse({'success': 'User registered successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({'error': 'Please provide both username and password'}, status=400)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            django_login(request, user)
            return JsonResponse({'success': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)