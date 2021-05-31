from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from json import loads, dumps
from .serializer import TicketSerializer
from .utils import TicketDB
import redis

redis = redis.Redis('localhost', port=6379, db=1)


class TicketsView(APIView):
    def __init__(self):
        super().__init__()
        self.serializer = TicketSerializer
        self.util = TicketDB()

    def get(self, request: Request):
        id = request.query_params.get('id', None)
        if id is None:
            tickets = self.util.get_all()
            serializer = self.serializer(tickets, many=True)
            return Response(serializer.data, status=200)

        return self.get_id(id)

    def get_id(self, id):
        cache = redis.get(id)
        if cache:
            return Response(loads(cache), status=200)
        ticket = self.util.get_id(id)
        if ticket:
            serializer = self.serializer(ticket)
            redis.append(id, dumps(serializer.data))
            return Response(serializer.data, status=200)
        return Response(status=400)

    def put(self, request: Request):
        if not request.user.is_authenticated:
            return Response(status=400)
        id = request.query_params.get('id', None)
        if id is None:
            return Response(status=400)
        try:
            self.util.create_order(id, request.user)
        except:
            return Response(status=400)
        return Response(status=200)

    def delete(self, request: Request):
        if not request.user.is_authenticated:
            return Response(status=400)
        id = request.query_params.get('id', None)
        if not id:
            return Response(status=400)
        try:
            self.util.delete_order(id, request.user)
        except:
            return Response(status=400)
        return Response(status=200)