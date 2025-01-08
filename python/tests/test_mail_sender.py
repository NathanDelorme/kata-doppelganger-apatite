import pytest
from mail_sender import MailSender, SendMailResponse, SendMailRequest

class User:
    def __init__(self, email):
        self.email = email

class HttpClient:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def post(self, base_url, request):
        if type(request) != SendMailRequest:
            return SendMailResponse(code=403, message="Bad Request Type")
        if request.recipient not in [user.email for user in self.users]:
            return SendMailResponse(code=404, message="User Not Found")
        if request.body == "will failed":
            return SendMailResponse(code=503, message="Internal server error")
        return SendMailResponse(code=200, message="OK")


@pytest.fixture
def http_client():
    http_client = HttpClient()
    return http_client

@pytest.fixture
def mail_sender(http_client):
    mail_sender = MailSender(http_client)
    return mail_sender

def test_send_v1(mail_sender, http_client):
    alice = User(email="alice@gmail.com")
    http_client.add_user(alice)
    message = "test à la noix"

    response = mail_sender.send_v1(alice, message)
    assert response.code == 200

def test_send_v2(mail_sender, http_client):
    alice = User(email="alice@gmail.com")
    http_client.add_user(alice)
    message = "will failed"

    response = mail_sender.send_v2(alice, message)
    assert response.code == 200
