import pytest
from otp_checker import OTPChecker

def test_valid_code():
    checker = OTPChecker()
    assert checker.validate_code("123456", "123456") is True
    assert checker.validate_code("000000", "000000") is True

def test_invalid_code_length():
    checker = OTPChecker()
    assert checker.validate_code("12345", "12345") is False
    assert checker.validate_code("7654321", "7654321") is False

def test_invalid_code_non_digits():
    checker = OTPChecker()
    assert checker.validate_code("12ab56", "12ab56") is False

def test_code_not_equal_expected():
    checker = OTPChecker()
    assert checker.validate_code("123456", "654321") is False

def test_code_empty():
    checker = OTPChecker()
    assert checker.validate_code("", "") is False


def test_code_negative_numbers():
    checker = OTPChecker()
    assert checker.validate_code("-123456", "-123456") is False


