#!bin/python3

class Address:
    def __init__(self, address):
        self.address = address
        
    def remove_address(self):
        del self.address
        
my_address = Address("7, Jolly Star Close")         
print(my_address.address)
ire_address = Address("Frekete Shekpern")
print(ire_address.address)       
