# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest

import Prob1
import Prob2

def numcheck(num, ans, tol=0.02):
    """Checks if a number is within a percentage tolerance of another. """
    return (ans*(1-tol) < num < ans*(1+tol))

def numcheck_pm(num, ans, pm=0.02):
    """Checks if a number is within a plus/minus threshold of another number. """
    return (ans-pm < num < ans+pm)

class Test_Prob1:
    def test_returns_something(self):
        student = Prob1.digital_root(10)
        assert student is not None, "You should be returning something here, and yet you don't seem to be doing so."

    def test_input_2digits(self):
        values = [10, 23, 70, 99]
        sols = [1, 5, 7, 9]
        for v,s in zip(values, sols):
            student = Prob1.digital_root(v)
            assert student == s, f"Expected {s} from digital_root({v}) but got {student} instead."

    def test_input_3digits(self):
        values = [101, 230, 707, 999]
        sols = [2, 5, 5, 9]
        for v,s in zip(values, sols):
            student = Prob1.digital_root(v)
            assert student == s, f"Expected {s} from digital_root({v}) but got {student} instead."

    def test_input_LARGE_NUMBERS(self):
        values = [9874982824999845, 9887499872782498899849 ]
        sols = [6, 3 ]
        for v,s in zip(values, sols):
            student = Prob1.digital_root(v)
            assert student == s, f"Expected {s} from digital_root({v}) but got {student} instead."

class Test_Prob2:
    def test_returns_something(self):
        student = Prob2.approximate_pi(5)
        assert student is not None, "Did you forget to actually return something from your function?"

    def test_1_term(self):
        student = Prob2.approximate_pi(1)
        sol = 4
        assert numcheck_pm(student, sol), f"Your approximate value of {student} is unexpectedly far from the correct value of {sol}."

    def test_5_term(self):
        student = Prob2.approximate_pi(5)
        sol = 3.3396825396825403
        assert numcheck_pm(student, sol, 0.002), f"Your approximate value of {student} is unexpectedly far from the correct value of {sol}."

    def test_50_term(self):
        student = Prob2.approximate_pi(50)
        sol = 3.121594652591011
        assert numcheck_pm(student, sol, 0.002), f"Your approximate value of {student} is unexpectedly far from the correct value of {sol}."

    def test_1000_term(self):
        student = Prob2.approximate_pi(1000)
        sol = 3.140592653839794
        assert numcheck_pm(student, sol, 0.002), f"Your approximate value of {student} is unexpectedly far from the correct value of {sol}."

    def test_1mil_term(self):
        student = Prob2.approximate_pi(1000000)
        sol = 3.1415916535897743
        assert numcheck_pm(student, sol, 0.000004), f"Your approximate value of {student} is unexpectedly far from the correct value of {sol}."


class Test_Prob3:
    def test_used_a_loop(self):
        with open('Prob3.py', 'r') as f:
            filestr = ''.join(f.readlines())
        assert 'while' in filestr or 'for' in filestr, 'It does not look like you used a loop anywhere in your image.\n'
    
    def test_defined_a_function(self):
        with open('Prob3.py', 'r') as f:
            filestr = ''.join(f.readlines())
        assert 'def' in filestr, 'It does not look like you defined a function anywhere in your image.\n'

    def test_created_a_label(self):
        with open('Prob3.py', 'r') as f:
            filestr = ''.join(f.readlines())
        assert 'GLabel(' in filestr, 'Did you remember to include a centered label in your image?\n'
