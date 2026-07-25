# class creation

class vehicle:
    color="black"                 #attributes
    petrolOrDiesel = "petrol"     #attributes
    mileage = "10"                #attributes

    def start():   # methods
        print("When you press clutch and accelerator then vehicle is started")
 
# Object Creation

car = vehicle()
print(car.color)

bike = vehicle()
print(bike.color)

airoplane = vehicle()
print(airoplane.mileage)
print(airoplane.color)

# We created one class and 3 objects of that class