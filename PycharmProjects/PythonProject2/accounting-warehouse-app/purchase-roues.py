from flask import request, jsonify
from models import Stock, db

def create_purchase():
    data = request.get_json()
    if not data or "quantity" not in data:
        return jsonify({"error": "Missing quantity"}), 400
    try:
        stock = Stock.query.first()
        if not stock:
            stock = Stock(item_name="Default", quantity=0)
            db.session.add(stock)
        stock.quantity += int(data["quantity"])
        db.session.commit()
        return jsonify({"message": "Purchase recorded", "new_stock": stock.quantity})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500