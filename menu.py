from re import L


print ("option 1")
print ("option 2")
print ("option 3")
opch = input ("choose what option by number ")

opchnc = "no"


if opch == "1":
    print ("option 1 chosen")
    opchnc = "yes"
elif opch == "2":
    print ("option 2 chosen")
    opchnc = "yes"
elif opch == "3":
    print ("option 3 chosen")
    opchnc = "yes"
elif opchnc == "no":
    print ("invalid option please retry")
