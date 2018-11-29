def main():
    menu()
def read():
    readFile = open("FroggyBooks.txt", "r")
    bookList = readFile.readlines()
    readFile.close()
    books=[]
    for bookNum in bookList:
        bookNum = bookNum.strip()
        aryTemp = bookNum.split(",")
        books.append(aryTemp)
    return books
def write(selcetion,quantity,subTotal,books):
    username = name()
    write_file = open (f"{username}.txt","w")
    price = float(books[selcetion][2] * quantity)
    book =(f"{books[selection], X {quantity}, = [price] ")
def cart(selection,quantity,books):
    
    print(f"QTY: {quantity} ")
    print (f"Item: {books[selection][1]}")
    print(f"Price: {books[selection][2]}")
    price = float(books[selection][2])
    subTotal = float(price * quantity)
    print(subTotal)
    return subTotal


def name():
    userName= str(input("What is your name?"))
    return userName
def menu():
    subTotal = 0
    print("WELCOME TO FROGGY'S BOOK STORE")
    userName = name()
    books = read()
    answer =("Y")
    while (answer == ("Y")):
        print("Here are the books we have:")
        listNum = 1 
        for book in books:
            listBooks = f" {listNum}) {book[0]},{book[1]},"
            print (listBooks)
            listNum+=1
        selection = int(input("Which would you like ?"))
        quantity = int(input(f"You chose{books[selection][1]} How many would you like?"))
        subTotal += cart(selection,quantity,books)
        answer = str.upper(input("Would you like another? Y/N"))
        write(selection,quantity,subTotal,books)

main()