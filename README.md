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

# Functions Used in HashTable:

  - Get_Hash() : Geting hashmap location using key to store value.
  - ReHash() or Resize() : When hashmap crosses load factor or filled upto 75% then we use rehash or resize.
  - Search(Get_Item())   : Finding value from the Hashtable using key.
  - Delete(Del_Item())   : deleting value from the Hashtable using key.
  - Put(Set_Item())      : Setting value in Hashtable using the key.
  - IsEmpty()            : Checking if Hashtable is empty or not.
  - Keys()               : To extract all keys that are store for the values respectively.
  - Entries()            : To extract all the entries that are stored in Hashtable as key,value pair.
### Working Process
No dependencies of any library. The main HashTable class has to be initialized first.

### Group Members:

 - Muneeb Sikandar (19B-083-SE)
 - Muhammad Waqar (19B-116-SE)

#### Reference

See [Open data Structures](https://opendatastructures.org/)

See [Introduction to algorithm third-edition](https://www.amazon.com/Introduction-Algorithms-Eastern-Economy-Thomas/dp/8120340078/ref=pd_lpo_14_t_0/145-4997158-2592204?_encoding=UTF8&pd_rd_i=8120340078&pd_rd_r=b721bd17-aac9-4e4c-afc8-817fd7fc1378&pd_rd_w=JrnOd&pd_rd_wg=HYh5m&pf_rd_p=16b28406-aa34-451d-8a2e-b3930ada000c&pf_rd_r=YG963B6NAV7J3QGKVSE6&psc=1&refRID=YG963B6NAV7J3QGKVSE6)

License
----

MIT
