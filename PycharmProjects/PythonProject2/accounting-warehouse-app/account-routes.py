from flask import request, jsonify
from models import Account
from models import db

def update_balance():
    data = request.get_json()
    if not data or "amount" not in data:
        return jsonify({"error": "Missing amount"}), 400
    try:
        account = Account.query.first()
        if not account:
            account = Account(account_name="Main", balance=0.0)
            db.session.add(account)
        account.balance += float(data["amount"])
        db.session.commit()
        return jsonify({"message": "Balance updated", "new_balance": account.balance})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500