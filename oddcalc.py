question1 = float(input("Give me a number"))
question2 = float(input("Give me another number"))
question3 = (input("What kind of operation do you want? Mul, Div, Mod"))
if (question3 == "Mul" or question3 == "mul"):
    mul = float(question1 * question2)
    print ("Your answer is " , mul)
elif (question3 == "Div" or question3 == "div"):
    div = float(question1 / question2)
    print ("Your answer is " , div)
elif (question3 == "Mod" or question3 == "mod"):
    mod = float(question1 % question2)
    print (("Your answer is ") , mod)
else:
    print ("ERROR")
