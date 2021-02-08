# HashTable (own Implementation)
HashTable is a data structure that implements an associative array of abstract data type, a structure that can maintain (keys, values) in a hashmap. A hash table uses a hash function through the key to store its value at the location of the hashmap respected index.  

# Avoiding coliison using HashTable!

  - Chaining method. 
  - Linear probing(open adressing).

# Some keypoints:
  -The load factor of the hash table is 0.75. It means the capacity and the number of buckets that are inside hashtable to be filled and by the load factor, we can calculate it if needs to increased or not.
The complexity of the hash function is O(1) average but, it can suffer a worst-case in o(n) due to two reasons:
  - If two many elements hashed into the same index. Looking for the key is o(n) times.
  - Once it passes its load factor, it needs to be resized. So, the rehashing might take in o(n). It depends upon values if too many values have the same key finding them may take time.
  - Hash function has many methods, such as the division method,  multiplication method, universal hashing, and perfect hashing.
  - But, it is quite rare that many elements will be hashed to the same key. If it is a better hash function.
