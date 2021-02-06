class HashTable:
    def __init__(self,length):
        self.length=length#Length of the hashtable
        self.data=[[] for i in range(self.length)]#HashMap as an array for Hashing values
    
    
    def Get_Array(self):#getting the whole hashmap array
        return self.data
    
    
    def __Get_Hash(self,key):#Hashing using key to find the index on the hashmap
        Hash_key=0#hashkey to be find
        for i in key:
            Hash_key+=ord(i)
        return Hash_key%self.length#finding hash according to array size
    
    
    def Get_Item(self,key):#searching using key on hashmap
        Hash=self.__Get_Hash(key)#finding location using hash
        Get=[]#storing all elements having same key
        for i in self.data[Hash]:#itterating to find the element
            if i[0]==key:#checking condition for matching key
                Get.append(i[1])#append in the get list
        return Get#getting the list as output
    
    
    def Set_Item(self,key,value):#putting value using hash function on the basis of key in the hashmap
        Hash=self.__Get_Hash(key)
        flag=False
        for k,v in enumerate(self.data[Hash]):#itterating through whole hash
            if len(v)==1 and v[0]==key:
                self.data[Hash][k]=(key,value)#putting both keys and values on the hashmap
                flag=True
        if not flag:#flag for checking if the value hash location is found or not
            self.data[Hash].append((key,value))
            
            
    def Del_Item(self,key):#deleting values on hashmap using 
        Hash=self.__Get_Hash(key)
        for i in range(len(self.data[Hash])):
            k, v = self.data[Hash][i]#Hashmap index point
            if k == key:
                self.data[Hash][i] = 'del'#after deleting keeping the del value to indicate that value has been deleted
                return v#returning the value that has been deleted
obj=HashTable(10)
obj.Set_Item("84","Muhammad_Waqar")
obj.Get_Array()
obj.Set_Item("116","Muneeb_Mirza")
obj.Get_Array()
obj.Get_Item("116")
obj.Del_Item("116")
obj.Get_Array()
