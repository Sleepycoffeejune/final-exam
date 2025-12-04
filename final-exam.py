class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}.")
    
class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.name = name
        self.address = address
        
        
    def place_order(self, item):
        new_order = DeliveryOrder(self.name, item, status="preparing")
        return new_order

class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.name = name
        self.vehicle = vehicle
    

    def deliver(self, order):
        order.status == "delivered"
        print(f"{self.name} is delivering {order.item} to {order.name} using {self.vehicle}.")
    

class DeliveryOrder:
    def __init__(self, customer, item, status):
        self.customer = customer
        self.item = item
        self.status = "preparing"
        self.driver = driver
    

    def assign_driver(driver):
        driver.deliver()
    

    def summary(self):
        print("Order Summary:")
        print(f"Item: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.driver.name}")

        


customer1 = Customer("Alice", "Address")
customer2 = Customer("Bob", "Address")
driver = Driver("David", "motorcycle")

customer1.introduce()
customer2.introduce()
driver.introduce()
print()
order1 = customer1.place_order("Laptop")
order2 = customer2.place_order("Headphones")

order1.summary()
print()
order2.summary()
print()
driver.deliver(order1)
driver.deliver(order2)


print("Final Status:")
print(f"Order for {order1.item} → {order1.status}")
print(f"Order for {order2.item} → {order2.status}")




