from flask import Flask, jsonify, request
from flask_cors import CORS
from db import conn, record_metric

app = Flask(__name__)
CORS(app)

# Get all products
@app.route("/products", methods=["GET"])
def get_products():
    record_metric("/products")
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()
    return jsonify(products)

# Add to cart (simplified, just simulates order creation)
@app.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    user_id = data.get("user_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    record_metric("/cart")

    with conn.cursor() as cur:
        # Get product price
        cur.execute("SELECT price, stock FROM products WHERE id=%s", (product_id,))
        product = cur.fetchone()
        if not product:
            return jsonify({"error": "Product not found"}), 404
        if product["stock"] < quantity:
            return jsonify({"error": "Not enough stock"}), 400

        total_price = product["price"] * quantity

        # Create order
        cur.execute(
            "INSERT INTO orders (user_id, product_id, quantity, total_price) VALUES (%s,%s,%s,%s)",
            (user_id, product_id, quantity, total_price)
        )

        # Reduce stock
        cur.execute(
            "UPDATE products SET stock = stock - %s WHERE id=%s",
            (quantity, product_id)
        )

        conn.commit()

    return jsonify({"message": "Added to cart", "total_price": total_price})

# Checkout endpoint (optional summary)
@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.get_json()
    user_id = data.get("user_id")
    record_metric("/checkout")

    with conn.cursor() as cur:
        cur.execute(
            "SELECT SUM(total_price) AS total_spent FROM orders WHERE user_id=%s",
            (user_id,)
        )
        total = cur.fetchone()["total_spent"]
    return jsonify({"message": f"User {user_id} spent {total}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)