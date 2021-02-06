#Simple Hashing
class HashTable:
    def __init__(self,length):#length of array for hashing table
        self.length=length
        self.data=[None for  i in range(length)]#making a none array 
    
    def Get_Array(self):
        return self.data
    
    def __Get_Hash(self,key):
        Hash_key=0
        for i in key:
            Hash_key+=ord(i)
        return Hash_key%self.length
    
    def Get_Item(self,index):#index for returning the item using hash
        Hash=self.__Get_Hash(index)
        return self.data[Hash]
    
    def Set_Item(self,key,value):#Setting item through key in hashtable
        Hash=self.__Get_Hash(key)
        self.data[Hash]=(key,value)
    
    def Del_Item(self,key):#deleting item from hashtable using key
        Hash=self.__Get_Hash(key)
        self.data[Hash]=None
obj=HashTable(10)
obj.Get_Array()
obj.Set_Item("84","Muhammad_Waqar")
obj.Get_Array()
obj.Get_Item("84")
obj.Del_Item("84")
obj.Get_Array()
