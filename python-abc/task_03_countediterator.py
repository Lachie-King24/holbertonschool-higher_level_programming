# task_03_countediterator.py

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # create an iterator from the iterable
        self.count = 0                  # initialize the counter

    def __next__(self):
        # Fetch the next item and increment the counter
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            # Re-raise StopIteration when the iterator is exhausted
            raise

    def get_count(self):
        return self.count
