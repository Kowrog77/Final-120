TAX = 0.076
def main():
    menu()
def read():
    readFile = open("FroggyBooks.txt", "r")
    bookList = readFile.readlines()
    readFile.close()
    books=[]
    for bookNum in bookList:
        bookNum = bookNum.strip()
        aryTemp = bookNum.split(,)
        books.append(aryTemp)
    return books
def write(write_file,selection,quantity,subTotal,books,userName,Total,price):
    
    ticket =(f"{quantity},                     {books[selection][1]},                     {books[selection][2]}\n" )
    taxAmt=(Total*TAX)
    
    write_file.write("Thank you" +(userName)+"for shopping with FROGGY'S BOOK STORE\n")
    write_file.write("Qty                     Item                                  Price\n")
    write_file.write("Order: "+str(ticket))
    write_file.write("-----------------------------\n")
    write_file.write("SubTotal: "+str(Total)+"\n")
    write_file.write("Tax: "+str(round(taxAmt,2))+"\n")
    write_file.write("-----------------------------\n")
    return taxAmt
def finalTotal(write_file,Total,taxAmt):
    
    finalTotal=(taxAmt + Total)
    write_file.write("Total: "+str(round(finalTotal,2))+"\n")
def cart(selection,quantity,books):
    
    print(f"QTY: {quantity} ")
    print (f"Item: {books[selection][1]}")
    price = float(books[selection][2])
    print(f"Price: {price}")
    
    subTotal = float(price * quantity)
    print("SubTotal:",round(subTotal,2))
    return subTotal, price


def name():
    userName= str(input("What is your name?"))
    return userName
def menu():
    
    basket = 0
    Total= 0
    print("WELCOME TO FROGGY'S BOOK STORE")
    userName = name()
    books = read()
    answer =("Y")
    write_file = open (f"{userName}.txt","w")
    while (answer == ("Y")):
        print("Here are the books we have:")
        listNum = 1 
        for book in books:
            listBooks = (f" {listNum}) {book[0]},{book[1]},")
            print (listBooks)
            listNum+=1
        selection = int(input("Which would you like ?"))
        selection -= 1
        quantity = int(input(f"You chose{books[selection][1]} How many would you like?"))
        basket = cart(selection,quantity,books)
        subTotal= (basket[0])
        price = (basket[1])
        #print(price,subTotal)
        Total+= subTotal
        answer = str.upper(input("Would you like another? Y/N"))
    
        taxAmt =write(write_file,selection,quantity,subTotal,books,userName,Total,price)
    finalTotal(write_file,Total,taxAmt)
    print(f"Your Rece is in a txt file named {userName}")
    write_file.close()
main()
