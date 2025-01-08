import pytest

from discount_applier import DiscountApplier

class Notifier:
    def __init__(self):
        self.notified_users = []

    def notify(self, user, message):
        print(f"Notification sent to {user}: {message}")
        self.notified_users.append(user)

@pytest.fixture
def notifier():
    notifier = Notifier()
    return notifier

@pytest.fixture
def applier(notifier):
    applier = DiscountApplier(notifier)
    return applier

def test_apply_v1(applier, notifier):
    users_to_notify = ["Alice", "Bob", "Charlie"]

    applier.apply_v1(10, users_to_notify)
    assert notifier.notified_users == users_to_notify

def test_apply_v2(applier, notifier):
    users_to_notify = ["Alice", "Bob", "Charlie"]

    applier.apply_v2(10, users_to_notify)
    assert notifier.notified_users == users_to_notify
