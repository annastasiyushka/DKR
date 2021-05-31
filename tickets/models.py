from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    city_from = models.CharField(max_length=255)
    city_to = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField()
    date = models.DateTimeField()

class TicketOrder(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)