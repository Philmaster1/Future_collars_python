from flask import jsonify
from models import Transaction

def get_history(line_from=None, line_to=None):
    try:
        query = Transaction.query.order_by(Transaction.timestamp)
        transactions = query.all()
        # If range is provided, slice the list
        if line_from is not None and line_to is not None:
            line_from = int(line_from) - 1
            line_to = int(line_to)
            transactions = transactions[line_from:line_to]
        result = [
            {
                "id": t.id,
                "type": t.type,
                "item_name": t.item_name,
                "quantity": t.quantity,
                "amount": t.amount,
                "timestamp": t.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
            for t in transactions
        ]
        return jsonify({"history": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500