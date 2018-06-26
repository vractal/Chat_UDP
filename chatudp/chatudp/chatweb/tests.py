from django.test import TestCase
from ..core.models import *


# Create your tests here.
class ChatViewTest(TestCase):

    def setUp(self):
        r = Room.objects.create(room_name="room", my_username="victor", room_password="1234")
        p = Participant.objects.create(username="victor", ip="127.255.123.5", room=r)
        p2 = Participant.objects.create(username="luiz", ip="127.255.232", room=r)
        m1 = SentTextMessage.objects.create(room=r, text="mensagemzinha", is_sent=True)
        m2 = ReceivedTextMessage.objects.create(room=r, text="mensagemzinha recebida", participant=p2)
        self.resp = self.client.get("/room")

    def test_get(self):
        self.assertEqual(200,self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp,"room_view.html")


    def test_context_has(self):
        required_context = (
            ('participants',Participant),
            ('messages', Message),
            ('room',Room),
        )

        for context, cl in required_context:
            with self.subTest(context=context,cl=cl):
                try:
                    instance = self.resp.context[context][0]
                except:
                    instance = self.resp.context[context]

                self.assertIsInstance(instance,cl)


    def test_post_request(self):
        self.post = self.client.post("/room", {"message-to-send": "teste123"})
        self.resp = self.client.get("/room")
        self.assertContains(self.resp,"teste123",)
