from otp_checker import OTPChecker

if __name__ == "__main__":
    calc = OTPChecker()
    # Пример вызова: кандидат должен реализовать метод validate_code
    code = "123456"
    result = calc.validate_code(code, "123456")
    print("Result:", result)
