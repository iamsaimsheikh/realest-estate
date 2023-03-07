from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
User = get_user_model()

# @method_decorator(csrf_exempt, name='dispatch')
class SignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({"error": "user already exists!"})
            else:
                if len(password) < 6:
                    return Response({"error": 'password length must be greater than 6'})
                else:
                    user = User.objects.create_user(
                        email=email, name=name, password=password)

                    user.save()
                    return Response({"info": "success!"})
        else:
            return Response({"error": "passwords do not match!"})
