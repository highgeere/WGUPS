# HashTable class using chaining.
class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.root = []
        for i in range(capacity):
            self.root.append([])

    def bucket_hash(self, key):
        return key % len(self.root)

    # Inserts a new item into the hashtable.
    def insert(self, key, item):
        # get the bucket list where this item will go.
        bucket = self.bucket_hash(key)
        self.root[bucket].append(item)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def lookup(self, key):
        # get the bucket item where this key would be.
        bucket = self.bucket_hash(key)
        bucket_items = self.root[bucket]

        # search for the key in the bucket list
        for item in bucket_items:
            if item.package_id == key:
                # find the item's index and return the item that is in the bucket list.
                index = bucket_items.index(item)
                return bucket_items[index]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = self.bucket_hash(key)
        bucket_items = self.root[bucket]

        for item in bucket_items:
            if item.package_id == key:
                bucket_items.remove(item)

    def table_size(self):
        count = 0
        for i in range(10):
            bucket_items = self.root[i]
            for item in bucket_items:
                count += 1
        return count
