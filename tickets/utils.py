from .models import Ticket, TicketOrder
from django.contrib.auth.models import User

class TicketDB:
    def __init__(self):
        self.ticket = Ticket.objects.all()
        self.order = TicketOrder

    def get_all(self):
        return self.ticket.all()

    def get_id(self, id):
        return self.ticket.get(pk=id)

    def create_order(self, id, user: User):
        order = self.order()
        ticket = self.get_id(id)
        order.ticket = ticket
        order.client = user
        order.save()
        return True

    def delete_order(self, id ,user: User):
        ticket = self.get_id(id)
        self.order.objects.filter(client=user).filter(ticket=ticket).delete()
        return True

