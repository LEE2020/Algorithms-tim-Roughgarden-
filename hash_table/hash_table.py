class HashTable:
    def __init__(self):
        self.array = dict()
    def __getitem__(self, item):
        return item in self.array
    def __setitem__(self, key, value):
        self.array[key] = value
    def insert(self, keys):
        for key in keys:
            self.array[key] = 1 # hash funciton f(x) =1 
        #return self.array 

def  load_data():
    data=[]
    with open('./2sum.txt') as f:
        for row in f:
            data.append(int(row.strip().split()[0]))
    return data

data = load_data()
ht = HashTable()
ht.insert(data)

#print(ht.array)
print("after hash funciton map") 
def target(t):
    for element in ht.array:
        other = t - element 
        if other in ht.array  and other != element:
            return 1 
    return 0 	


count = 0 
for i in range(-10000,10001):
    if target(i):
        count +=1 
    if i%100 ==0 : print("now iiiiii   " +str(i))

print(count) 


