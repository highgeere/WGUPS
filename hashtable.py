# Required hash table class
# Implemented with nested lists
class HashTable:
    # Initialize the hash table with empty buckets
    # Use 10 buckets as default
    def __init__(self, capacity=10):
        self.root = []
        for i in range(capacity):
            self.root.append([])

    # Very basic hash function, using just the package ID as key - O(1)
    def bucket_hash(self, key):
        return key % len(self.root)

    # Insert a new item into the hash table - O(1)
    def insert(self, key, item):
        # Get bucket ID from hash function
        bucket = self.bucket_hash(key)
        # Store the item in that bucket
        self.root[bucket].append(item)

    # Search for an item by key, and return the item - O(n)
    def lookup(self, key):
        # Get bucket ID from hash function
        bucket = self.bucket_hash(key)
        bucket_items = self.root[bucket]

        # Look at each package object and match the search key if present
        for item in bucket_items:
            if item.package_id == key:
                # Find the index and return the item at index
                index = bucket_items.index(item)
                return bucket_items[index]
        else:
            return None

    # Remove an item with matching key from the hash table - O(n)
    def remove(self, key):
        # Get bucket ID from hash function
        bucket = self.bucket_hash(key)
        bucket_items = self.root[bucket]

        # If the item key is present in the bucket, remove the item
        for item in bucket_items:
            if item.package_id == key:
                bucket_items.remove(item)

    # Helper function to return the number of items in the hash table
    # Used for range determination
    # O(n)
    def table_size(self):
        count = 0
        for i in range(10):
            bucket_items = self.root[i]
            for item in bucket_items:
                count += 1
        return count
