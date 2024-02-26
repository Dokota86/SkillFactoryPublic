import pytest
from app.calculator import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def teardown_method(self):
        print('Выполнение метода Teardown')

    def test_multiply_success(self):
        assert self.calc.multiply(4, 2) == 8

    def test_division_success(self):
        assert self.calc.division(8, 2) == 4

    def test_substraction_success(self):
        assert self.calc.subtraction(5, 2) == 3

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)
