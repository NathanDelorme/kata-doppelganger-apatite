import pytest
from mail_sender import MailSender, SendMailResponse, SendMailRequest

class User:
    def __init__(self, email):
        self.email = email

class HttpClientV1:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def post(self, base_url, request):
        if request.recipient not in [user.email for user in self.users]:
            return SendMailResponse(code=404, message="User Not Found")
        return SendMailResponse(code=200, message="OK")

class HttpClientV2:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def post(self, base_url, request):
        if type(request) != SendMailRequest:
            return SendMailResponse(code=403, message="Bad Request Type")
        return SendMailResponse(code=503, message="Internal server error")

@pytest.fixture
def http_client_v1():
    http_client = HttpClientV1()
    return http_client

@pytest.fixture
def mail_sender_v1(http_client_v1):
    mail_sender = MailSender(http_client_v1)
    return mail_sender

def test_send_v1(mail_sender_v1, http_client_v1):
    alice = User(email="alice@gmail.com")
    http_client_v1.add_user(alice)
    message = "test à la noix"

    response = mail_sender_v1.send_v1(alice, message)
    assert response.code == 200


@pytest.fixture
def http_client_v2():
    http_client = HttpClientV2()
    return http_client

@pytest.fixture
def mail_sender_v2(http_client_v2):
    mail_sender = MailSender(http_client_v2)
    return mail_sender

def test_send_v2(mail_sender_v2, http_client_v2):
    alice = User(email="alice@gmail.com")
    http_client_v2.add_user(alice)
    message = "test à la noix"

    response = mail_sender_v2.send_v2(alice, message)
    assert response.code == 200
