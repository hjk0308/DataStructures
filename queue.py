class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty.")
            return None;
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x

    def isEmpty(self):
        return self.front_index == len(self.items)

    def front(self):
        if self.front_index == len(self.items):
            print("Queue is empty.")
            return None;
        else:
            x = self.items[self.front_index]
            return x

    def __len__(self):
        return len(self.items)

    