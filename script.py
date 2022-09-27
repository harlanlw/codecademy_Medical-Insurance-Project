#Python Dictionaries: Medical Insurance Project
# Add your code here

medical_costs = {"Marina":6607.0, "Vinay":3225.0}

#Adding 3 new paitents with one line of code.
medical_costs.update({"Connie":8886.0, "Isaac":16444.0, "Valentina":6420.0})

#Printing Medical_Costs to test.
print("Medical Costs Dict at Step 4: " + str(medical_costs))

#Vinay's cost was inputed wrong.  Corrected and printed.
medical_costs["Vinay"] = 3325.0
print("This is step 5: " + str(medical_costs))

#Step 6
total_cost = 0

for value in medical_costs.values():
  total_cost += value

print("The total cost for all medical costs is: " + str(total_cost))

#Step 7
medical_cost_length = len(medical_costs)

average_costs = total_cost / medical_cost_length
print("Average Insurance Cost: " + str(average_costs))

#Step 8
names = ["Marnia", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

#Step 9
zipped_ages = list(zip(names, ages))

#Step 10
names_to_ages = {key: value for key, value in zipped_ages}

print(names_to_ages)

#Step 11
marina_age = (names_to_ages.get("Marnia", None))
print("Marnia's age is " + str(marina_age))

#Step 12 Creading the medical database
medical_records = {}

#Step 13 & 14
medical_records.update({"Marina": {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}})

medical_records.update({"Vinay": {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3325.0}})

medical_records.update({"Connie": {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}})

medical_records.update({"Isaac": {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}})

medical_records.update({"Valentina": {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}})

#Step 15
print(medical_records)

#Step 16
print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")

#Step 17
medical_records.pop("Vinay")

#Step 18
for item in medical_records.items():
  #print(item[0])
  print(item[0] + " is a " + str(item[1]["Age"]) + " year old " + item[1]["Sex"] + " " + item[1]["Smoker"] + " with a BMI of " + str(item[1]["BMI"]) + " and insurance cost of " + str(item[1]["Insurance_cost"]))



