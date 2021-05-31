from .models import Ticket
from rest_framework import serializers

class TicketSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Ticket
        fields = '__all__'