car_models = []
for i in range(3):
    model = input("Enter the name of car model " + str(i + 1) + ": ")
    car_models.append(model)
print("Car models in the dealership:", car_models)


sales_data = []
for i in range(3):
    while True:
        print("\nEnter data for car model:", car_models[i])
        sold = int(input("Enter number of cars sold: "))
        returned = int(input("Enter number of cars returned: "))
        serviced = int(input("Enter number of cars serviced: "))

        # Validation check
        if sold >= returned:
            # Append the data with model name to sales_data
            sales_data.append([car_models[i], sold, returned, serviced])
            break
        else:
            print("Error: Returned cars cannot exceed sold cars. Please re-enter.")

print("\nValidated Sales Data for each model:")
for data in sales_data:
    print("Model:", data[0], "- Sold:", data[1], "Returned:", data[2], "Serviced:", data[3])

