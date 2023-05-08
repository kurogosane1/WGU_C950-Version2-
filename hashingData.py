# Syed Khurshid, SID:010081191


# Creating a HashTable class using chaining
class HashingData:
    # Constructor with optional initial capacity parameter
    # Buckets are assigned to an empty list
    def __init__(self, initial_capacity=10):
        self.data = []
        for _ in range(initial_capacity):
            self.data.append([])

    # Generating hash-key which is a O(1)
    def hash_key_generator(self, key):
        return hash(key) % len(self.data)

    # Inserting a new item into the hash table
    def insert(self, key, item):
        Hkey = self.hash_key_generator(key)
        # First to check if the Hash Key does exist of not
        if self.data[Hkey] == None:
            self.data[Hkey] = [key, item]
            return True  # End the function to continue to add more later
        else:
            for keyValue in self.data[Hkey]:
                if keyValue[0] == key:
                    keyValue[1] = item
                    return True

            self.data[Hkey].append([key, item])
            return True

    # Searching for an item with matching key in the hash table
    # Returns the item if not found, or None if not found

    def search(self, key):
        # get the bucket list where the key is located
        Hkey = self.hash_key_generator(key)
        # In case the key doesn't exist
        if self.data[Hkey] != None:
            for items in self.data[Hkey]:
                if items[0] == key:
                    return items[1]
            return None

    # Removes an item with matching key from hash table.
    def delete(self, key):
        Hkey = self.hash_key_generator(key)
        bucket_list = self.data[Hkey]
        if self.data[Hkey] == None:
            return False
        else:
            for keyValue in bucket_list:
                if keyValue[0] == key:
                    bucket_list.remove(keyValue[0], keyValue[1])
                    return True
            return False

    # To Update the item in a key
    def update(self, key, value):
        Hkey = self.hash_key_generator(key)
        # Now to search for hashed line item if its been found or not
        if self.data[Hkey] != None:
            # Now  if they match then we update the second list in the data
            for items in self.data[Hkey]:
                if items[0] == key:
                    items[1] = value
                    return True  # This should stop any further updates
        # In case the key doesn't match
        return None

    # This is to get the self table
    def get_hash_Table(self):
        return self.data
