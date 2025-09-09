"""Tests for the calculator module."""
import pytest
from calculator import add, subtract, multiply


def test_addition():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtraction():
    """Test the subtract function."""
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5
    assert subtract(-5, -3) == -2


def test_multiplication():
    """Test the multiply function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0
