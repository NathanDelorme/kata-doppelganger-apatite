from safe_calculator import SafeCalculator

class Authorizer:
    def __init__(self, value):
        self.value = value

    def authorize(self):
        return self.value

def test_divide_should_not_raise_any_error_when_authorized():
    calculator = SafeCalculator(authorizer=Authorizer(True))
    calculator.add(1, 2)
