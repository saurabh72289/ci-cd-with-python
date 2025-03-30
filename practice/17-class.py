# __init__ is name as constructor in python
# self is consider as this   in pyton
# name is the parameter taking during initialization of constructor

class myClass:
    def __init__(self, name):
        # create member variable
        self.name = name
        self.size = len(self.name)
        
    def callName(self):
        return self.name
    
    def callSize(self):
        return self.size

vari = myClass("saurabh")
print(vari.callName()) 
print(vari.callSize())
