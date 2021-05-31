from .serializer import ClientLoginSerializer
from .serializer import ClientRegisterSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpRequest
from json import loads
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class ClientRegister(APIView):
    def __init__(self):
        super().__init__()
        self.serializer = ClientRegisterSerializer
    def post(self, request: HttpRequest):
        data = loads(request.body)
        serializer = self.serializer(data=data)
        if not serializer.is_valid():
            return Response(status=400)
        User(**serializer.data).save()
        return Response(status=200)

class ClientLogin(APIView):
    def __init__(self):
        super().__init__()
        self.serializer = ClientLoginSerializer

    def post(self, request: HttpRequest):
        data = loads(request.body)
        serializer = self.serializer(data=data)
        if not serializer.is_valid():
            return Response(status=400)
        client = authenticate(username=serializer.data['username'],
                              password=serializer.data['password'])

        if client is None:
            return Response(status=400)

        login(request, client)
        return Response(status=200)

class ClientLogout(APIView):
    def post(self, request: HttpRequest):
        try:
            logout(request)
        except:
            return Response(status=400)
        return Response(status=200)
