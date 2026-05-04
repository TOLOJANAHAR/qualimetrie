from main import compute_final_price, validate_data


# 🔹 Tests prix Business
def test_business_price():
    data = {"base_price": 100, "class": "Business", "baggage": 0}
    assert compute_final_price(data) == 300


# 🔹 Tests bagage
def test_baggage_25():
    data = {"base_price": 100, "baggage": 25}
    assert compute_final_price(data) == 150


def test_baggage_35():
    data = {"base_price": 100, "baggage": 35}
    assert compute_final_price(data) == 200


def test_baggage_0():
    data = {"base_price": 100, "baggage": 0}
    assert compute_final_price(data) == 100


# 🔹 Cas sans classe
def test_no_class():
    data = {"base_price": 100}
    assert compute_final_price(data) == 100


# 🔹 Bagage invalide
def test_invalid_baggage():
    data = {"base_price": 100, "baggage": "abc"}
    assert compute_final_price(data) == 100


# 🔹 Validation données
def test_validate_data_none():
    assert validate_data(None) == "body manquant"


def test_validate_data_invalid_base_price():
    assert validate_data({"base_price": "abc"}) == "base_price invalide"


def test_validate_data_valid():
    assert validate_data({"base_price": 100}) is None
