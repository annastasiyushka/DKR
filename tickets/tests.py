from django.test import TestCase
from .utils import TicketDB
from .models import Ticket
from django.contrib.auth.models import User


class TicketTest(TestCase):
    def setUp(self) -> None:
        self.util = TicketDB()
        self.ticket = Ticket()
        self.ticket.price = 1000
        self.ticket.date = '2021-05-27 12:12:12'
        self.ticket.city_from = 'Kyiv'
        self.ticket.city_to = 'Madrid'
        self.ticket.save()

        self.user = User()
        self.user.username = 'username'
        self.user.set_password('1q2w3e4r5t6y7u')
        self.user.email = 'username@gmail.com'
        self.user.save()

    def test(self):
        self.assertEqual(len(self.util.get_all()), 1)
        self.assertEqual(self.util.get_id(1), self.ticket)
        self.assertEqual(self.util.create_order(1, self.user), True)
        self.assertEqual(self.util.delete_order(1, self.user), True)
