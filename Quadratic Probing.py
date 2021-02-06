class QuadraticProbing:
    def __init__(self,data,factor=0.75):#load factor decides to increase hashmap capacity it it is filled 75%
        self.data=data#size of hashmap
        self.counter=0#checking how many elements are in hashmap
        self.factor=factor
        self.Table=[None for i in range(self.data)]#hashmap of values
        self.keys=[0 for i in range(self.data)]#hashmap of keywords
        
    def __Hash_Function(self,key,data=None):#hash function hashing index using key
        if not data:
            data=len(self.Table)
        return key%data
    
    def keys(self):#checking keys you can ignore not required for checking if keys are deleted or not can run this too.
        return self.keys
    """for resizing the whole process(size will be increase by double and each previous will be shifted to new value table hashmap to the respected location)"""
    def __ReHash(self):
        Ntable=[None]*len(self.Table)*2
        Nkeys=[0]*len(self.Table)*2
        for i in self.Table:
            if not i:
                continue
                self.__insert(i,Ntable,Nkeys)
        return Ntable,Nkeys
    
    def __insert(self,key,Table=None,keys=None):#inserting into the hashmap using hashfunction by key
        if not Table:
            Table=self.Table
        if not keys:
            keys=self.keys
        index=self.__Hash_Function(key)
        H=1
        while self.keys[index]==1:
            index=(index+h*h)%len(self.Table)
            h+=1
        Table[index],keys[index]=key,1
    
    def insert(self,key):#inserting using key in the hashmap 
        self.counter+=1
        factor=self.counter/len(self.Table)
        if factor>self.factor:
            self.Table,self.keys=self.__ReHash()
            self.factor=factor
        self.__insert(key)
        
    def search(self,key):#searching by jey in the hashmap
        index=self.__Hash_Function(key)
        H=1
        while (self.Table[index]!=key or self.keys[index]==-1) and self.keys[index]==1:
            index=(index+h*h)%len(self.Table)
            h+=1
        if self.Table[index]==key:
            return index
        return -1
    
    def delete(self,key):#deleting by key in the hashmap
        index=self.search(key)
        self.keys[index]=-1#1 indicite occupied, 0 indicate empty spot, -1 indicate item deleted
obj=QuadraticProbing(10)
obj.insert(10)
obj.search(10)
obj.delete(10)
obj.search(10)
print(obj.keys)
