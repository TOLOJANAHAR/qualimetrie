from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/flight-price', methods=['POST'])
def calculate_price():
    data = request.json

    price = 0

    if data is not None:
        if "base_price" in data:
            if isinstance(data["base_price"], (int, float)):
                price = data["base_price"]

                if "class" in data:
                    if data["class"] == "Business":
                        price = price * 3
                    else:
                        if data["class"] == "Economy":
                            price = price
                        else:
                            price = price

                else:
                    price = price

                if "baggage" in data:
                    if isinstance(data["baggage"], (int, float)):
                        if data["baggage"] > 20:
                            if data["baggage"] > 30:
                                price = price + 100
                            else:
                                price = price + 50
                        else:
                            if data["baggage"] <= 20:
                                price = price
                            else:
                                price = price
                    else:
                        price = price
                else:
                    price = price

            else:
                return jsonify({"error": "base_price invalide"}), 400
        else:
            return jsonify({"error": "base_price manquant"}), 400
    else:
        return jsonify({"error": "body manquant"}), 400

    return jsonify({"final_price": price})


if __name__ == '__main__':
    app.run(debug=True)