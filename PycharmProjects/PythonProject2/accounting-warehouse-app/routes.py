from models import Transaction

def register_routes(app):
    from . import stock_routes, account_routes, purchase_routes, sale_routes, history_routes

    app.add_url_rule('/stock', view_func=stock_routes.get_stock, methods=['GET'])
    app.add_url_rule('/purchase', view_func=purchase_routes.create_purchase, methods=['POST'])
    app.add_url_rule('/sale', view_func=sale_routes.create_sale, methods=['POST'])
    app.add_url_rule('/balance', view_func=account_routes.update_balance, methods=['PUT'])
    app.add_url_rule('/history/', view_func=history_routes.get_history, methods=['GET'])
    app.add_url_rule('/history/<line_from>/<line_to>/', view_func=history_routes.get_history, methods=['GET'])