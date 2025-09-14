class OTPChecker:
    def validate_code(self, code: str, expected: str) -> bool:
        """
        TODO: Реализуй проверку одноразового кода:
        - Код должен быть строкой из 6 цифр.
        - Должен совпадать с expected.
        - Верни True если код валиден, иначе False.
        Подумай над граничными случаями.
        """

        if not (
                type(code) == str and
                type(expected) == str and
                code.isdigit() and
                len(code) == 6):
            return False

        return code == expected
