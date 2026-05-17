#Fuel Management System
def menu():
    print("1.Oil")
    print("2.Diesel")
    print("3.Kerosene")

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
    print("-----MONEY OF DIESEL-----")
    litre1=120
    while True:
        print("1 Litre Diesel=",litre1,'TK')
        money=int(input("Enter money:"))
        total=money/litre1
        if money>=100:
         print(f"Total litre of Diesel:{total:.4}",'Litre')
         break
        else:
            print("Insufficient money")
def Dlitre():
     print("-----LITRE DIESEL-----")
     litre1=120
     print("1 Litre Diesel=",litre1,'TK')
     litre=int(input("Enter litre:"))
     tlitre=litre1*litre
     print("Total money of Diesel:",tlitre,'TK')



def kamount():
    print("-----MONEY OF KEROSENE-----")
    litre1=110
    while True:
        print("1 Litre kerosene=",litre1,'TK')
        money=int(input("Enter money:"))
        total=money/litre1
        if money>=100:
         print(f"Total litre of kerosene:{total:.4}",'Litre')
         break
        else:
            print("Insufficient money")
def klitre():
     print("-----LITRE OF KEROSENE-----")
     litre1=110
     print("1 Litre kerosene=",litre1,'TK')
     litre=int(input("Enter litre:"))
     tlitre=litre1*litre
     print("Total money of kerosene:",tlitre,'TK')


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
                 kamount()
                 klitre()
        else:
            print("Invalid choice!")
            break
main()
