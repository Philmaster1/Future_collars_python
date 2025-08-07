from datetime import datetime


def log_operation(func):
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__} with args={args[1:]}, kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper


def format_info(func):
    def wrapper(*args, **kwargs):
        print(f"=============================================================================")
        return func(*args, **kwargs)

    return wrapper


class DataStore:
    def __init__(self, name, description="No description"):
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self._data = {}

    # @log_operation
    def __setitem__(self, key, value):
        self._data[key] = value

    # @log_operation
    def __getitem__(self, key):
        return self._data[key]

    # @log_operation
    def __iter__(self):
        return iter(self._data)

    # @log_operation
    def items(self):
        return self._data.items()

    @format_info
    def __str__(self):
        return f"DataStore(name={self.name}, description={self.description}, created_at={self.created_at}, size={len(self._data)})"


class LoggingDataStore(DataStore):

    @log_operation
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    @log_operation
    def __getitem__(self, key):
        return super().__getitem__(key)


if __name__ == "__main__":
    store = DataStore(name="My store 1", description="Holding some example data")
    store['a'] = 10
    store['b'] = 20

    # print(store['a'])
    # print(store['b'])

    for key in store:
        print(f"{key} = {store[key]}")

    for k, v in store.items():
        print(f"{k}: {v}")

    print(store)

    print("\n\n")

    store = LoggingDataStore(name="My store 2", description="Holding some example data with logs")
    store['a'] = 10
    store['b'] = 20

    # print(store['a'])
    # print(store['b'])

    for key in store:
        print(f"{key} = {store[key]}")

    for k, v in store.items():
        print(f"{k}: {v}")

    print(store)




