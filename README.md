# Тестовое задание

## Задача
Реализовать метод `validate_code` в файле `otp_checker.py`.

### Условия
- Код должен быть строкой из **6 цифр**.
- Должен совпадать с ожидаемым значением `expected`.
- Вернуть `True`, если код валиден, иначе `False`.

### Примеры
```python
checker = OTPChecker()
checker.validate_code("123456", "123456")  # True
checker.validate_code("123456", "654321")  # False
checker.validate_code("12ab56", "12ab56")  # False
checker.validate_code("12345", "12345")    # False
```

## Проверка
Мы будем запускать автотесты из файла `test_otp_checker.py`:

```bash
pytest -q
```

Все тесты должны пройти успешно.
