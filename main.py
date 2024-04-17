AllowedVehicles = open("AllowedVehicles.txt", "r")
EditVehicles = open("AllowedVehicles.txt", "a")


def menu():
  print("\n********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print("Please Enter the following number below from the following menu:")
  print()
  print("1. PRINT all Authorized Vehicles")
  print("2. Search for Authorized Vehicles")
  print("3. ADD Authorized Vehicle")
  print("4. DELETE Authorized Vehicle")
  print("5. Exit")
  print("********************************\n")


def printVehicles():
  print(
      "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:\n"
  )
  print(AllowedVehicles.read())
  AllowedVehicles.seek(0)


def searchVehicles():
  searchChoice = input("\nPlease Enter the full Vehicle name: \n")
  found = False
  for line in AllowedVehicles:
    if searchChoice.strip() in line.strip():
      found = True
      break
  if found:
    print(searchChoice, "is an authorized vehicle\n")
  else:
    print(
        searchChoice,
        "is not an authorized vehicle, if you received this in error please check the spelling and try again\n"
    )


def addVehicles():
  addChoice = input(
      "\nPlease Enter the full Vehicle name you would like to add: (Make, model)\n"
  )
  EditVehicles.write(f'\n{addChoice}')
  print("\nYou have added " + addChoice + " as an authorized vehicle")


def deleteVehicles():
  removeChoice = input(
      "\nPlease Enter the full Vehicle name you would like to REMOVE: ")
  lines = AllowedVehicles.readlines()
  found = False
  for line in lines:
    if removeChoice.strip() in line.strip():
      found = True
      break
  if found:
    sureCheck = input("Are you sure you want to remove " + removeChoice +
                      " from the Authorized Vehicles List? yes/no\n")
    if sureCheck == "yes":
      lines.remove(line)
      EditVehicles = open("AllowedVehicles.txt", "w")
      EditVehicles.write("\n".join(lines))
      EditVehicles.close()
      print("You have REMOVED " + removeChoice + " as an authorized vehicle")
    elif sureCheck == "no":
      print("Removal canceled")
    else:
      print("Invalid input, please try again")
  else:
    print(
        "The vehicle you are trying to remove is not found in the Authorized Vehicles List"
    )


def program():
  menu()
  menuChoice = input()
  if menuChoice == "1" or menuChoice == "2" or menuChoice == "3" or menuChoice == "4" or menuChoice == "5":
    if menuChoice == "1":
      printVehicles()
    if menuChoice == "2":
      searchVehicles()
    if menuChoice == "3":
      addVehicles()
    if menuChoice == "4":
      deleteVehicles()
    if menuChoice == "5":
      quit("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
  else:
    print("\nInvalid choice\n")
  program()


program()
AllowedVehicles.close()
EditVehicles.close()
