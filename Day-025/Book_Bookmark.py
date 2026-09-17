class Bookmark:
    def __init__(self,book_title,page_number):
        if page_number <=0:
            raise ValueError("Invalid page number")
        self.book_title = book_title
        self.page_number = page_number


    def go_to_page(self):
        return self.page_number

    def move_to_page(self,new):
        if new <=0:
            raise ValueError
        self.page_number = new

    def display(self):
        print(f"Book title : {self.book_title}")
        print(f"Page Number: {self.page_number}")


book = Bookmark("python",10)

book.display()
print("\n")

book.move_to_page(15)
print("\n")

book.display()

print("\n")

print(f"The page number is {book.go_to_page()}")
        