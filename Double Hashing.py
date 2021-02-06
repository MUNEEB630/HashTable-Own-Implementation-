class DoubleHashing:
    def __init__(self,data,factor=0.75):#load factor decides to increase hashmap capacity it it is filled 75%
        self.counter=1#here 1 means occupied , 0 means empty and -1 means item is deleted
        self.data=data#size of hashmap 
        self.factor=factor
        self.Table=[None]*self.data#size of hashmap for values
        self.keys=[0]*self.data#size of hashmap for keys
        
    def __Hash_Function(self,key,data=None):#hash function for finding the keys 
        if not data:#if no lenth is being geven then it will take previous table length for finding hash
            data=len(self.Table)
        return key%data
    """for resizing the whole process(size will be increase by double and each previous will be shifted to new value table hashmap to the respected location)"""
    def __ReHash(self):
        Ntabel=[None]*len(self.Table)*2
        Nkeys=[0]*len(self.Table)*2
        for i in self.Table:
            if not i:
                continue
                self.__insert(i,Ntable,Nkeys)
        return Ntable,Nkeys
    
    def __insert(self,key,Table=None,keys=None):#insert finding using two hashes when required to maintain no worst case
        if not Table:
            Table=self.Table
        if not keys:
            keys=self.keys
        index=self.__Hash_Function(key)
        h=1
        Hash_2=self.__Hash_Function(key)
        while self.keys[index]==1:#after checking the key using it will run untill at gets the empty slot or location
            index=(index+h*Hash_2)%len(self.Table)
            h+=1
        Table[index],keys[index]=key,1
        
    def keys(self):#checking keys you can ignore not required for checking if keys are deleted or not can run this to
        return self.keys
    
    def insert(self,key):#inserting into the hashmap using hashfunction by key
        self.counter+=1
        factor=self.counter/len(self.Table)
        if factor>self.factor:#checking the factor that the rehash has to be use for resize or not
            self.Table,self.keys=self.__ReHash()
            self.factor=factor
        self.__insert(key)
    
    def search(self,key):#searching in hashmap using key 
        index=self.__Hash_Function(key)
        h=1
        Hash_2=self.__Hash_Function(key)
        while (self.Table[index] != key or self.keys[index]==-1) and self.keys[index]==1:#condition for checking if the item is deleted or not and if it it is present or not
            index=(index+h*hash_2)%len(self.Table)
            h+=1
        if self.Table[index]==key:
            return index
        return -1
    
    def delete(self,key):#deleting the value from the hashmap and also at the same location -1 is being placed to indicate that element is being deleted
        index=self.search(key)
        self.keys[index]=-1

obj=DoubleHashing(10)
obj.insert(10)
obj.search(10)
obj.delete(10)
print(obj.keys)
