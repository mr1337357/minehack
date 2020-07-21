import os

class map:
    def __init__(self,directory):
        self.directory=directory
        index = os.path.join(directory,'index.map')
        chunk = os.path.join(directory,'chunk.map')
        self.chunktable={}
        with open(index,'rb') as indexfile:
            for line in indexfile.readlines():
                line = line.split(b' ')
                if len(line)<3:
                    break
                loc = (line[0],line[1])
                offs = line[2]
                self.chunktable[loc]=offs
        self.chunkfile= open(chunk,'rb')

    def get_chunk(self,chunkno):
        self.chunkfile.seek(chunkno*32*32*128)
        return chunkfile.read(32*32*128)


    def __getitem__(self,loc):
        try:
            return get_chunk(self.chunktable[loc])
        except:
            print('oof')

if __name__ == '__main__':
    m = map('testmap')
    print(m[(0,0)])
