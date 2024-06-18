from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import json

class CustomUserSerializer(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, CustomUser):
            return {
                "id": obj.id,
                "username": obj.username,
                "fullname": obj.fullname,
            }
        return super().default(obj)

def serialize_user(user):
    return json.dumps(user, cls=CustomUserSerializer)
