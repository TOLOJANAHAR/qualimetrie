

from flask import Flask, request, jsonify
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    pass  # en CI, on ignore

app = Flask(__name__)

# 🔹 Récupérer la clé API depuis .env
API_KEY = os.getenv("API_KEY", "my-secret-key")


# 🔹 Vérification clé API
def check_api_key(req):
    key = req.headers.get("x-api-key")
    return key == API_KEY


# 🔹 Validation des données
def validate_data(data):
    if not data:
        return "body manquant"

    if "base_price" not in data:
        return "base_price manquant"

    if not isinstance(data["base_price"], (int, float)):
        return "base_price invalide"
    return None


# 🔹 Calcul prix classe
def apply_class_price(base_price, flight_class):
    if flight_class == "Business":
        return base_price * 3
    return base_price


# 🔹 Calcul bagage
def apply_baggage_fee(price, baggage):
    if not isinstance(baggage, (int, float)):
        return price
    if baggage > 30:
        return price + 100
    if baggage > 20:
        return price + 50
    return price


# 🔹 Fonction principale métier
def compute_final_price(data):
    price = data["base_price"]

    price = apply_class_price(price, data.get("class"))
    price = apply_baggage_fee(price, data.get("baggage", 0))
    return price


# 🔹 Route API
@app.route('/api/flight-price', methods=['POST'])
def calculate_price():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    error = validate_data(data)
    if error:
        return jsonify({"error": error}), 400

    final_price = compute_final_price(data)
    return jsonify({"final_price": final_price})


if __name__ == '__main__':
    app.run(debug=True)
