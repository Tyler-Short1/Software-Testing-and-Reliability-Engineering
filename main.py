from Car import Car

car_1 = Car(118, 120, 0)
car_2 = Car(20, 90, 80)

print(f"""Car_1 has a top speed of {car_1.maxspeed}mph. It is currently travelling {car_1.currentspeed}mph. 
It has {car_1.fuellevel} fuel left.""")

print(f"""Car_2 has a top speed of {car_2.maxspeed}mph. It is currently travelling {car_2.currentspeed}mph. 
It has {car_2.fuellevel} fuel left.""")

car_1.accelerate(5)
car_2.accelerate(15)
car_2.brake(10)
car_2.refuel(30)

print("")

print(f"""Car_1 has a top speed of {car_1.maxspeed}mph. It is currently travelling {car_1.currentspeed}mph. 
It has {car_1.fuellevel} fuel left.""")

print(f"""Car_2 has a top speed of {car_2.maxspeed}mph. It is currently travelling {car_2.currentspeed}mph. 
It has {car_2.fuellevel} fuel left.""")