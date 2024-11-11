car_models = []
sales_data = []

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

revenue = []

# Calculate revenue for each car model using the sales_data array
for data in sales_data:
    model, sold, returned, serviced = data
    model_revenue = (sold * 20000) - (returned * 20000)  # Calculate revenue
    revenue.append([model, model_revenue])

print("\nRevenue for each car model:")
for data in revenue:
    print("Model:", data[0], "- Revenue:", data[1])
