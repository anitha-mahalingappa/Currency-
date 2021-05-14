

def my_curr (cash, bill):
    Denomination = [2000,500,200,100,50,20,10,5,2,1]
    Balance = 0
    i = 0
    den_list= [ 0,0,0,0,0,0,0,0,0,0]
    Balance = cash - bill
    while i < len(Denomination):
        if Denomination[i] <= Balance:
           den_list[i] = Balance // Denomination[i]   
           Balance %= Denomination[i]       
        i += 1
#    print(den_list)
    for  x in range(0, len(Denomination)):
            if den_list[x] > 0 :
                print (str(Denomination[x]) + " * " + str(den_list[x]))

    #2000 = 0
    

    
    
#Main prog
cash_paid = int(input("please enter the cash paid: "))  
bill_amount = int(input("please enter the total bill: "))
my_curr(cash_paid,bill_amount)



