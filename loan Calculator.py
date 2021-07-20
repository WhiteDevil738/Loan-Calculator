while True:
    #welcome
    print("Welcome To loan Calculator")
    #input
    p = int(input("Principle: "))
    r = int(float(input("Rate of interest in %: ")))
    n = int(input("Loan Tenure in Month: "))

    #(1+r)^n = c
    a = r/(12*100)
    b = 1+a
    c = b**n

    #((1+r)^n)-1 = z
    x = 1+a
    y = x**n
    z = y-1

    #p*r*(1+r)^n/((1+r)^n)-1
    emi = p*a*c/z
    total = emi*n
    interest = total-p
    print("Loan EMI: ₹",emi)
    print("Total Payment(Principal + Interest): ₹",total,)
    print("Total Interest Payable: ₹",interest)
    print("To Exite press 1 else 2:")
    exit_ = int(input())
    if exit_ == 2:
        pass
    else:
        print("Thank's For Using")
        break
      
        
    
        







