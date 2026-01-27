
#!/usr/bin/env python3

# CountedIterator class
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Original iterator
        self.count = 0  # Counter for iterated items

    def __next__(self):
        # Fetch the next item and increment the counter
        item = next(self.iterator)  # Raises StopIteration when done
        self.count += 1
        return item

    def get_count(self):
        # Return the number of items iterated so far
        return self.count
