class book:
    def __init__(self,title,total_pages,total_read):
        self.title = title
        self.total_pages = total_pages
        self.total_read = total_read

    def read_pages(self,pages):
        if pages < 0:
            raise ValueError("Cannot read a negative number of pages.")
        
        if self.total_read + pages > self.total_pages:
            self.total_read = self.total_pages
        else:
            self.total_read += pages

    def remaining_pages(self):
        remaining = self.total_pages - self.total_read
        return remaining

    def progress_percentage(self):
        return (self.total_read / self.total_pages) * 100
    
    def display_progress(self):
        print(f"Book title:{self.title}")
        print(f"Total Pages: {self.total_pages}")
        print(f"Pages read: {self.total_read}")
        print(f"Remaining pages: {self.remaining_pages()}")
        print(f"Progress: {self.progress_percentage()  }%")
        

my_book = book("Python basics", 150, 0)
my_book.display_progress()
my_book.read_pages(45)
my_book.display_progress()