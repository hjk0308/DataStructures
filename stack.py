class stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty.")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty.")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self) == 0