car_models = []
sales_data = []
revenue = []
top_models = []

for i in range(3):
    model = input("Enter the name of car model " + str(i + 1) + ": ")
    car_models.append(model)
print("Car models in the dealership:", car_models)

print(car_models)

for i in range(3):
    while True:
        sold = int(input("Enter cars sold for " + car_models[i] + ": "))
        returned = int(input("Enter cars returned: "))
        serviced = int(input("Enter cars serviced: "))
        if sold >= returned:  # validate that more cars can't be returned than sold
            sales_data.append([sold, returned, serviced])
            break
        else:
            print("Returned cars cannot exceed sold cars. Please re-enter.")

print(sales_data)

for data in sales_data:
    sold, returned, serviced = data
    model_revenue = (sold * 20000) - (returned * 20000)
    revenue.append(model_revenue)
print("Revenue for each car model:", revenue)


max_revenue = revenue[0][1]
for data in revenue:
    if data[1] > max_revenue:
        max_revenue = data[1]

top_models = []
for data in revenue:
    if data[1] == max_revenue:
        top_models.append(data[0])

print("\nModel(s) with the highest revenue:", top_models)

