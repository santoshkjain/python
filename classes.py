import hello

class Computer:

    Screen = 1

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    
    def config(self):
        print("Config for this computer is", self.cpu , self.ram)


com1=Computer('i5',64)
com2=Computer('AMD',32)

com1.config()
com2.config()

Computer.Screen = 2

print(com1.Screen)
print(com2.Screen)