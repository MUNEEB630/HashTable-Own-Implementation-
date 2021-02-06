#Collissions Using Linear Probing
class HashTable:
    def __init__(self,data):
        self.data=data#Size of the hashtable
        self.values=[None for i in range(self.data)]#To store hashValues
        self.keys=[None for i in range(self.data)]#To store hashkeys
        self.elements=0#to keep record to element for using resize function
        
    def __GetHash(self,key):
        var=key%self.data#calculating index using hash for values using division method there are many others also.
        return var#returning index for the key
    
    def __ReHash(self,Var):
        Value=(Var+2)%self.data#if index is filled or not found then we will use this
        return Value
    
    def Get_Item(self,key):#geting the value using key for finding data related to it        
        index=self.__GetHash(key)
        while self.keys[index] is not None:
            if self.keys[index]==key:
                return self.values[index]
            index.__ReHash(index)
        return None
    
    def Set_Item(self,key,value):#putting the value into the location of hash
        index=self.__GetHash(key)
        while self.keys[index] is not None and self.keys[index] is not "Del":
            if self.keys[index]==key:
                #if the value already exist then we replace
                Remove=self.values[index]
                self.values[index]=value
                return Remove
            #probing continuation
            index=self.__ReHash(index)
        #Got empty slot then placing values and keys
        self.keys[index]=key
        self.values[index]=value
        self.elements+=1
        if self.elements==self.data:
            self.ResizeHash()
    
    def Remove(self,key):#Removing the value using key from Hash
        index=self.__GetHash(key)
        if self.values[index] is not None:
            if self.keys[index]==key and self.values[index] is not "Del":
                value=self.values[index]
                self.values[index]="Del"
                self.elements-=1
                return value
    
    def IsEmpty(self):#checking if Hashtable is empty or not
        return self.elements==0
    
    def Keys(self):#Getting all keys for values of hashtable
        if not self.IsEmpty():
            keys=[i for i in self.keys if i!=None and i!="Del"]
            return keys
        return self.keys
    
    def Values(self):#Getting all values in the HashTable
        if not self.IsEmpty():
            values=[i for i in self.values if i is not None]
            return values
        return self.values
    
    def Size(self):#Getting the size of values present currently In HashTable
        return self.elements
    
    def Entries(self):#getting all key values in the hashtable:
        Values=[]
        for i in self.keys:
            for j in self.values:
                Values+=Values+[(i,j)]
        return Values
    
    def ResizeHash(self):#Resizing the whole HashTable
        self.data*=2#size equals to double
        #Copying the previous elements
        Nkeys=[None for i in range(self.data)]
        Nvalues=[None for i in range(self.data)]
        for i in self.keys:
            for j in self.values:
                if i is not None:
                    index=self.__GetHash(i)
                    while Nkeys[index]is not None:
                        index=self.__ReHash(index)
                    Nkeys[index]=i
                    Nvalues[index]=j
        #now replacing old arrays
        self.keys=Nkeys
        self.values=Nvalues
        Nkey=None
        NValues=None
H=HashTable(10)
H.Set_Item(84,"Muhammad Waqar")
H.Get_Item(84)
H.Remove(84)
H.Keys()
H.Values()
