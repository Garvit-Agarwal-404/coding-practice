x=int(input("Enter a number"))
match x:
    case 1:
        print("Number is 1")
    case _ if x%2==0:    # // is default case
        print("case 2")
    case _ if x%2!=0:
        print("case 3")