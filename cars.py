import json

filePath = "cars.json"
def addcar(cars):
    model = input("Enter car model: ")
    for i in cars:
        if i["model"] == model:
            print("Car already exists")
            break
    else:
        cars.append({"model": model, "brand": input("Insert brand: ")})
        print("car added")
        print(cars)

def deletecar(cars):
    model = input("Enter car model: ")
    for i in cars:
        if i["model"] == model:
            cars.remove(i)
            print(f"{model} has been deleted.")
            break
    else:
        print(f"{model} not found.")

def editcar(cars):
    model = input("Enter car model: ")
    for i in cars:
        if i["model"] == model:
            i["model"] = input("Insert new model: ")
            i["brand"] = input("Insert new brand: ")
            print(f"{model} has been updated.")
            break
    else:
        print(f"{model} not found.")

def exitprog():
    with open(filePath, 'w') as file:
        json.dump(cars, file, indent=4)
    print("Data saved. Exiting program.")
    exit()

try:
    with open(filePath, 'r') as file:
        cars= json.load(file)
except: 
    cars = []

while True:
    
    print("Menu:")
    print("1 - Add new car")
    print("2 - Delete a car")
    print("3 - Edit a car")
    print("4 - Show all cars")
    print("X - Exit program")

    selection = input("Selection: ")
    if selection == "X": 
        exitprog()
    elif selection == "1": 
        addcar(cars)
    elif selection == "2": 
        deletecar(cars)
    elif selection == "3": 
        editcar(cars)
    elif selection == "4": 
        print(cars)
    else:
        print("Invalid selection. Please try again.")