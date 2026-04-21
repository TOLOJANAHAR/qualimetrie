from main import compute_final_price

def test_business():
    assert compute_final_price({
        "base_price": 100,
        "class": "Business",
        "baggage": 0
    }) == 300

def test_baggage_25():
    assert compute_final_price({
        "base_price": 100,
        "baggage": 25
    }) == 150

def test_baggage_35():
    assert compute_final_price({
        "base_price": 100,
        "baggage": 35
    }) == 200