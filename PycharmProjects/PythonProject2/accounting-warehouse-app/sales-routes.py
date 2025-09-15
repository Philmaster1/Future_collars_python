from flask import request, jsonify
from models import Stock, db

def create_sale():
    data = request.get_json()
    if not data or "quantity" not in data:
        return jsonify({"error": "Missing quantity"}), 400
    try:
        stock = Stock.query.first()
        if not stock or stock.quantity < int(data["quantity"]):
            return jsonify({"error": "Not enough stock"}), 400
        stock.quantity -= int(data["quantity"])
        db.session.commit()
        return jsonify({"message": "Sale recorded", "new_stock": stock.quantity})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500