myVar = input("Does it move? (yes/no) ")
if myVar == "yes":
  myNextVar = input("Should it be moving? (yes/no) ")
  if myNextVar == "yes":
    print("Thats okay!")
  elif myNextVar == "no":
    print("Use some duct tape")
  else:
    print("Answer my question! You didn't type yes or no.")
elif myVar == "no":
  print("then your all good!")
else:
  print("Answer my question! You didn't type yes or no.")
