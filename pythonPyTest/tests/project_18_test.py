import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
       self.calc = Calculator

    def test_multiply_calculate_positive(self):
       assert self.calc.multiply(self, 3, 3) == 9

    def test_division_positive(self):
       assert self.calc.division(self, 27, 9) == 3

    def test_subtraction_positive(self):
       assert self.calc.subtraction(self, 35, 15) == 20

    def test_adding_positive(self):
       assert self.calc.adding(self, 35, 15) == 50
