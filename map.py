class map:
    def __init__(self,filename):
        self.filename=filename
        self.file = open(filename,'r+b')
        self.chunktable = {}

