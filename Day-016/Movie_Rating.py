class movie:
    def __init__(self, title,genre,rating):
        self.title = title
        self.genre = genre
        self.rating = rating
    
    def add_movies(self):
        self.title = input("Enter the Title: ")
        self.genre = input("Enter the Genre: ")
        rating = float(input("Enter the Rating: "))

        if rating <= 10:
            self.rating = rating
        else:
            print("Invalid Rating!")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}")
        
    def update_rating(self):
        rating = float(input("Enter the Rating: "))

        if rating <= 10:
            self.rating = rating
        else:
            print("Invalid Rating!")

my_movie = movie("interstellar","Drama",9.5)
my_movie2 = movie("avengers","scifi",8.6)

my_movie.update_rating()