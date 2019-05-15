score = input("Enter Score: ")
try :
    sc = float(score)
    if sc>=0.9 :
        print("A")
    elif sc>=0.8 :
        print("B")
    elif sc>=0.7 :
        print("C")
    elif sc>=0.6 :
        print("D")
    else :
        print("F")
    
except :
    sc = -1
    print("Error in your input")