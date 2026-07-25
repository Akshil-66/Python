# Create a class Laptop with attributes : brand , Ram , Price.
# Create 2 object with different values.

class Laptop:
    brand = "default"
    RAM = "8GB"
    price = "1 Lakh"

laptop1 = Laptop()
laptop1.brand = "Mackbook"
laptop1.RAM = "16GB"
print("Laptop1 brand :- " , laptop1.brand)

laptop2 = Laptop()
laptop2.brand = "HP"
print("Laptop2 brand :- " , laptop2.brand)
