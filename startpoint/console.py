import pdb
import repositories.brand_repository as brand_repository
import repositories.car_repository as car_repository
from models.brand import Brand
from models.car import Car

car_repository.delete_all()
brand_repository.delete_all()

brand1 = Brand("BMW")
brand_repository.save(brand1)

brand2 = Brand("Ferrari")
brand_repository.save(brand2)

brand3 = Brand("Ford")
brand_repository.save(brand3)

brand4 = Brand("Mercedes Benz")
brand_repository.save(brand4)

brand5 = Brand("McLaren")
brand_repository.save(brand5)

brand6 = Brand("Toyota")
brand_repository.save(brand6)

brand7 = Brand("Peugeot")
brand_repository.save(brand7)

brand8 = Brand("Honda")
brand_repository.save(brand8)

brand9 = Brand("Dodge")
brand_repository.save(brand9)

brand10 = Brand("Audi")
brand_repository.save(brand10)


car1 = Car(brand1, "SUV", "X6", 34500, 37000, 8)
car_repository.save(car1)

car2 = Car( brand2 ,"Sport", "F150", 118000, 119500, 4)
car_repository.save(car2)

car3 = Car(brand3,"SUV", "Bronco", 80000, 81200, 9 )
car_repository.save(car3)

car4 = Car( brand4 ,"Sedan", "E-Class", 28000, 29500, 3)
car_repository.save(car4)

car5 = Car(brand5,"Sport", "720s", 120000, 132000, 5 )
car_repository.save(car5)

car6 = Car( brand6 ,"Sport", "Supra", 58000, 60000, 1)
car_repository.save(car6)

car7 = Car(brand7,"SUV", "5008SW", 12000, 13200, 8 )
car_repository.save(car7)

car8= Car(brand8,"SUV", "HRV", 18000, 19500, 3)
car_repository.save(car8)

car9 = Car(brand9,"SUV", "Durango", 22000, 23200, 2 )
car_repository.save(car9)

car10 = Car( brand10 ,"Saloon", "A6", 32000, 33500, 10)
car_repository.save(car10)


car = car_repository.cars_in_inventory(brand3)

pdb.set_trace()
