from flask import jsonify
from models import Stock, Account

def get_stock():
    try:
        stock = Stock.query.first()
        account = Account.query.first()
        stock_level = stock.quantity if stock else 0
        balance = account.balance if account else 0.0
        return jsonify({"stock": stock_level, "balance": balance})
    except Exception as e:
        return jsonify({"error": str(e)}), 500