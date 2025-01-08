from unittest.mock import Mock, call

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





@pytest.fixture
def notifier_mock():
    notifier_mock = Mock()
    return notifier_mock

@pytest.fixture
def applier_with_mock_notifier(notifier_mock):
    applier_with_mock_notifier = DiscountApplier(notifier_mock)
    return applier_with_mock_notifier

def test_apply_v1_mock(applier_with_mock_notifier, notifier_mock):
    users_to_notify = ["Alice", "Bob", "Charlie"]
    applier_with_mock_notifier.apply_v1(10, users_to_notify)
    assert notifier_mock.notify.call_count == 3

def test_apply_v2_mock(applier_with_mock_notifier, notifier_mock):
    users_to_notify = ["Alice", "Bob", "Charlie"]
    applier_with_mock_notifier.apply_v2(10, users_to_notify)

    assert notifier_mock.notify.call_args_list == [call("Alice", "You've got a new discount of 10%"),
                                                  call("Bob", "You've got a new discount of 10%"),
                                                  call("Charlie", "You've got a new discount of 10%")]