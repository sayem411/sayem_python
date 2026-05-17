#Fuel Price and litre Calculator
def amount():
    print("-----MONEY-----")
    litre1=140
    while True:
        money=int(input("Enter money:"))
        total=money/litre1
        if money>=100:
         print(f"Total litre of fuel:{total:.4}",'Litre')
         break
        else:
            print("Insufficient money")
def litre():
     print("-----LITRE-----")
     litre1=140
     litre=int(input("Enter litre:"))
     tlitre=litre1*litre
     print("Total money of fuel:",tlitre,'TK')

amount()
litre()