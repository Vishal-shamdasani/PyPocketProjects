class Library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0
    def addbook(self,n):
        print(1)
        self.n=n
        while self.n!=0:
            self.name=input(f"what is the name of your {n} book" )
            self.books.append(self.name)
            self.no_of_books+=1
            self.n-=1
    def name_of_all_books(self):
        return self.books
        # pass
    def total_no_of_books(self):
        return self.no_of_books
    def check_for_the_no_of_books(self):
        return(f"the length of the list of books is {len(self.books)} and the total no of books in the library are {self.total_no_of_books()}")




def purpous():
    b=int(input('''\nwelcome to the Library what do you want to do \nif you want to exite press 0\nif you want to check all the avilable book press 1
if you want to add to to our library press 2\nif you want to see the total no. of book avilable press 3 \n'''))
    return b
a=Library()

while True:
    c=purpous()
    if c==0:
        print("thank you for comming")
        break
    elif c==1:
        print(a.name_of_all_books())
    elif c==2:
        how_many_books_to_add=int(input("enter the no of book you want to add "))
        a.addbook(how_many_books_to_add)
    elif c==3:
        print(a.total_no_of_books())
    # a.addbook(3)

    