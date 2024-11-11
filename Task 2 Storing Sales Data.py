car_models = []
for i in range(3):
    model = input("Enter the name of car model " + str(i + 1) + ": ")
    car_models.append(model)
print("Car models in the dealership:", car_models)

sales_data = []

for i in range(3):
    print("\nEnter data for car model:", car_models[i])
    sold = int(input("Enter number of cars sold: "))
    returned = int(input("Enter number of cars returned: "))
    serviced = int(input("Enter number of cars serviced: "))

    # Add the model name along with its sales data to the sales_data array
    sales_data.append([car_models[i], sold, returned, serviced])

print("\nSales Data for each model:")
for data in sales_data:
    print("Model:", data[0], "- Sold:", data[1], "Returned:", data[2], "Serviced:", data[3])
