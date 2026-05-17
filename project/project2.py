#Fuel Price and litre Calculator
def menu():
    print("1.Oil")
    print("2.Dizel")
    print("3. Carosin")

def Oamount():
    print("-----MONEY OF OIL-----")
    litre1=140
    while True:
        print("1 Litre Oil=",litre1,'TK')
        money=int(input("Enter money:"))
        total=money/litre1
        if money>=100:
         print(f"Total litre of oil:{total:.4}",'Litre')
         break
        else:
            print("Insufficient money")
def Olitre():
     print("-----LITRE OF OIL-----")
     litre1=140
     print("1 Litre Oil=",litre1,'TK')
     litre=int(input("Enter litre:"))
     tlitre=litre1*litre
     print("Total money of oil:",tlitre,'TK')


def Damount():
    print("-----MONEY OF DIZEL-----")
    litre1=120
    while True:
        print("1 Litre Dizel=",litre1,'TK')
        money=int(input("Enter money:"))
        total=money/litre1
        if money>=100:
         print(f"Total litre of Dizel:{total:.4}",'Litre')
         break
        else:
            print("Insufficient money")
def Dlitre():
     print("-----LITRE DIZEL-----")
     litre1=120
     print("1 Litre Dizel=",litre1,'TK')
     litre=int(input("Enter litre:"))
     tlitre=litre1*litre
     print("Total money of Dizel:",tlitre,'TK')



def Camount():
    print("-----MONEY OF CAROSIN-----")
    litre1=100
    while True:
        print("1 Litre Carosin=",litre1,'TK')
        money=int(input("Enter money:"))
        total=money/litre1
        if money>=100:
         print(f"Total litre of Carosin:{total:.4}",'Litre')
         break
        else:
            print("Insufficient money")
def Clitre():
     print("-----LITRE OF CAROSIN-----")
     litre1=100
     print("1 Litre Carosin=",litre1,'TK')
     litre=int(input("Enter litre:"))
     tlitre=litre1*litre
     print("Total money of Carosin:",tlitre,'TK')


def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            Oamount()
            Olitre()
        elif choice == "2":
              Damount()
              Dlitre()
        elif choice == "3":
                 Camount()
                 Clitre()
        else:
            print("Invalid choice!")
            break
main()
