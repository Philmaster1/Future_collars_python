class Manager:
    def _init_(self):
        self.balance_amount = 0
        self.tasks = {}

    def assign(self, task_name, func):
        """Assign a function to a task name."""
        # self.tasks[task_name] = func
        self.task = task_name
        self.tasks[self.task] = func

    def execute(self, task_name, *args, **kwargs):
        """Execute the assigned task."""
        if task_name in self.tasks:
            return self.tasks[task_name](*args, **kwargs)
        else:
            raise ValueError(f"Task '{task_name}' not assigned.")

    def sale_decorator(self, func):
        def wrapper(amount):
            print(f"Processing sale of {amount}")
            self.balance_amount += amount
            return func(amount)
        return wrapper

    def purchase_decorator(self, func):
        def wrapper(amount):
            print(f"Processing purchase of {amount}")
            self.balance_amount -= amount
            return func(amount)
        return wrapper

    def balance_decorator(self, func):
        def wrapper():
            print(f"Current balance: {self.balance_amount}")
            return func()
        return wrapper

# Example usage and testing
if __name__ == "__main__":
    manager = Manager()

    @manager.sale_decorator
    def sale(amount):
        print(f"Sale completed: {amount}")

    @manager.purchase_decorator
    def purchase(amount):
        print(f"Purchase completed: {amount}")

    @manager.balance_decorator
    def balance():
        print("Balance checked.")

    # Assign tasks
    manager.assign('sale', sale)
    manager.assign('purchase', purchase)
    manager.assign('balance', balance)

    # Execute operations
    manager.execute('sale', 100)
    manager.execute('purchase', 40)
    manager.execute('balance')