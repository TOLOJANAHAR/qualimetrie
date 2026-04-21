# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/api/flight-price', methods=['POST'])
# def calculate_price():
#     data = request.json

#     price = 0

#     if data is not None:
#         if "base_price" in data:
#             if isinstance(data["base_price"], (int, float)):
#                 price = data["base_price"]

#                 if "class" in data:
#                     if data["class"] == "Business":
#                         price = price * 3
#                     else:
#                         if data["class"] == "Economy":
#                             price = price
#                         else:
#                             price = price

#                 else:
#                     price = price

#                 if "baggage" in data:
#                     if isinstance(data["baggage"], (int, float)):
#                         if data["baggage"] > 20:
#                             if data["baggage"] > 30:
#                                 price = price + 100
#                             else:
#                                 price = price + 50
#                         else:
#                             if data["baggage"] <= 20:
#                                 price = price
#                             else:
#                                 price = price
#                     else:
#                         price = price
#                 else:
#                     price = price

#             else:
#                 return jsonify({"error": "base_price invalide"}), 400
#         else:
#             return jsonify({"error": "base_price manquant"}), 400
#     else:
#         return jsonify({"error": "body manquant"}), 400

#     return jsonify({"final_price": price})


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify

app = Flask(__name__)


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
    data = request.json
    # Validation
    error = validate_data(data)
    if error:
        return jsonify({"error": error}), 400
    # Calcul
    final_price = compute_final_price(data)
    return jsonify({"final_price": final_price})


if __name__ == '__main__':
    app.run(debug=True)
