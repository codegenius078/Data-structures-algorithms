# a basic hash table

class HashTable:
    def __init__(self, max_size=1):
        self.data_list = [None] * max_size

    def get_index(self, key):
        result = 0
        for k in key:
            number_character = ord(k)
            result += number_character
        list_index = result % len(self.data_list)
        return list_index

    def get_valid_index(self, key):
        idx = self.get_index(key)

        while True:
            kv = self.data_list[idx]
            if kv is None:
                return idx
            k, v = kv
            if k is key:
                return idx
            idx += 1

            if idx == len(self.data_list):
                idx = 0

    def insert(self, key, value):
        idx = self.get_valid_index(key)
        self.data_list[idx] = key, value

    def find(self, key):
        idx = self.get_index(key)
        kv = self.data_list[idx]
        return kv[1]

    def list_all(self):
        for k in self.data_list:
            if k is not None:
                print(k[0])


hash_table = HashTable(10)
hash_table.insert("John", 5)
hash_table.insert("Bison", 9)
hash_table.insert("Jay", 8)
hash_table.insert("listen", 99)
hash_table.insert("silent", 200)
hash_table.list_all()
print(hash_table.find("Bison"))

