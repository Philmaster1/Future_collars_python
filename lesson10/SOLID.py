class Shop:  # Split Shop class to Shop and Product class
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.products = {}

    def add_product(self, name, price, price_model="qty"):
        self.products[name] = {"price": price, "name": name, "model": price_model}

    def get_product_price(self, product, qty):
        product = self.products[product]
        if product["model"] == qty:
            return product["price"] * qty
        else:
            return product["price"]


# SOLID - O
class ProductWrong:
    def __init__(self, name, price, model, discount_qty, discount_percent):
        self.name = name
        self.price = price
        self.model = model
        self.discount_qty = discount_qty
        self.discount_percent = discount_percent

    def get_price(self, qty):
        if qty < self.discount_qty:
            return self.price * qty
        return self.price * qty * (100 - self.discount_percent) / 100


# A quick lookup showed you that the object is created on around 40 different files, the get_price method is called on 70 different files.
# You destroyed rest of your code


class Product:
    def __init__(self, name, price, model):
        self.name = name
        self.price = price
        self.model = model

    def get_price(self, qty):
        return self.price * qty


# Wrapper function
class DiscountedQtyProduct(Product):
    def __init__(self, name, price, model, discount_qty, discount_percent):
        super().__init__(name, price, model)
        self.discount_qty = discount_qty
        self.discount_percent = discount_percent

    def get_price(self, qty):
        if qty < self.discount_qty:
            return self.price * qty
        return self.price * qty * (100 - self.discount_percent) / 100


# SOLID - L
# class SubscriptionProduct(Product):
#     def get_price(self, qty, months):   #WRONG (declaration of function not fit to base class)
#         return self.price * qty * months


class SubscriptionProduct(Product):
    def __init__(self, name, price, model, default_timespan):
        super().__init__(name, price, model)
        self.default_timespan = default_timespan

    def get_price(self, qty):
        return self.price * qty * self.default_timespan

    def get_price_by_timespan(self, qty, months):
        return self.price * qty * months


# SOLID - I

# One big interface for Product - wrong
def get_price(self, qty):  # product price
    pass


def get_price_by_timespan(self, qty):  # price of the subscription product
    pass


def get_weight(self, qty):  # package weight (for calculating the shipping price)
    pass


def estimated_delivery(self, qty):  # estimated delivery time
    pass


def tax_rate(self):  # default tax percentage
    pass


# Split to separate interfaces

# Methods for Product:
def get_price(self, qty):  # product price
    pass


def tax_rate(self):  # default tax percentage
    pass


# Methods for subscription product:
def get_price_by_timespan(self, qty):  # price of the subscription product
    pass


# Products for shipping
def estimated_delivery(self, qty):  # estimated delivery time
    pass


def get_weight(self, qty):  # package weight (for calculating the shipping price)
    pass


# SOLID - D
class Product(Product):
    ...

    def export_data(self):
        return self.__class__.__name___, self.__dict__


class AbstractExport:
    def __init__(self, filepath):
        ...


class JSONExport(AbstractExport):
    ...


class CSVExport(AbstracExport):