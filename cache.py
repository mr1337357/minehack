#a python map that wraps a python map
#note that if you update something inside the cache it doesn't know
#call dirty with the object's key or you'll have a bad time
class cache:
    class cacheitem:
        def __init__(self):
            self.age=0
            self.dirty=False
            self.item=None

        def __str__(self):
            return '{} {}'.format(self.age,self.dirty)

    def __init__(self,container,size=16):
        self.size=size
        self.container=container
        self.storage={}
    
    def __getitem__(self,key):
        try:
            return self.storage[key].item
        except:
            pass
        for _,elem in self.storage.items():
            elem.age +=1
        if self.size == len(self.storage):
            #cache is full. delet an entry

            oldest=cache.cacheitem()
            oldkey=None

            for k,v in self.storage.items():
                if v.age > oldest.age:
                    oldest = v
                    oldkey = k

            if oldest.dirty:
                self.container[oldkey]=oldest.item
            self.storage.pop(oldkey)
        self.storage[key]=cache.cacheitem()
        self.storage[key].item=self.container[key]
        return self.storage[key].item

    def __str__(self):
        out='cache:\n'
        for k,v in self.storage.items():
            out+='   '+str(k)+' '+str(v)+'\n'
        return out

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'test':
        s = [i for i in range(100)]
        c = cache(s)
        for i in range(100):
            print(c[i])
            print(c)

        print(c[15])
        print(c)
