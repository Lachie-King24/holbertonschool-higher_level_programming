#!/usr/bin/python3
"""Module that defines the VerboseList class"""

class VerboseList(list):
    """List subclass that prints messages on modifications"""

    def append(self, item):
        """Add an item to the list and print a notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from an iterable and print a notification"""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove an item from the list and print a notification"""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Pop an item from the list and print a notification"""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
