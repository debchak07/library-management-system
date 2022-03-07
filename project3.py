class library():
    
    def __init__(self,listofbooks):
        self.books = listofbooks
    
    
    def displaybooks(self):
        print("The list of books present in the CENTRAL lIBRARY is given below:")
        for book in self.books:
            print(" * " + book)
    
    def requestbook(self,bookname):
        if bookname in self.books:
            print("The book of your request is present in the library. You can take it but you have to return it within 30 days!")
        else:
            print("The book has already been issued from the LIBRARY") 
        self.books.remove(bookname) 
        print("The books currently present in the LIBRARY are:")
        for book in self.books:
            print("* " + book)
        

    def returnbook(self,bookname):
        print("Thanks for returning the book to the LIBRARY, We hope you have enjoyed the book!")
        self.books.append(bookname)
        print("The books currently present in the LIBRARY are:")
        for book in self.books:
            print("* " + book)


class student():

    def requestbook(self):
        self.books=input("Enter the name of the book you want to take from the LIBRARY : ")
        return self.books

    def returnbook(self):
        self.books=input("Enter the name of the book you want to return to the LIBRARY : ")
        return self.books   

if __name__ == "__main__":
    centrallibrary=library(["Complete C","Python","Web Developement","Pysics"])
    Student=student()
    while(True):
        welcomemess=("        ********** WELCOME TO THE CENTRAL LIBRARY **********    ")
        print(welcomemess)
        print("Press 1 for requesting list of books present in the library.")
        print("Press 2 for requesting a book from the LIBRARY.")
        print("Press 3 for returning a book to the LIBRARY.")
        print("Press 4 to exit.")
        a=int(input("Enter your choice : "))
        if (a==1):
            centrallibrary.displaybooks() 
        elif (a==2):    
            centrallibrary.requestbook(Student.requestbook())
            
        elif (a==3):
            centrallibrary.returnbook(Student.returnbook())    
        elif(a==4):
            print("Thank you for using the LIBRARY SYSTEM")
            exit()

        else:
            print("Wrong choice has been provided")        
