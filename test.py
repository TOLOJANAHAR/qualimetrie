from main import calculate_final_price


def test_business_price():
    data = {"base_price": 100, "class": "Business", "baggage": 0}
    assert calculate_final_price(data) == 300


def test_baggage_25kg():
    data = {"base_price": 100, "class": "Economy", "baggage": 25}
    assert calculate_final_price(data) == 150


def test_baggage_35kg():
    data = {"base_price": 100, "class": "Economy", "baggage": 35}
    assert calculate_final_price(data) == 200
