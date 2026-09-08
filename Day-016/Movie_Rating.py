class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}")
        print() 

    
    def update_rating(self, new_rating):
        if 0 <= new_rating <= 10:
            print(f"Updating rating to {new_rating}...\n")
            self.rating = new_rating
        else:
            print(f"Cannot update: {new_rating} is invalid. Rating must be between 0 and 10.\n")

movie1 = Movie("Interstellar", "Sci-Fi", 8.7)

movie1.display_info()
movie1.update_rating(9.0)
movie1.display_info()

print("-" * 20 + "\n") 


movie2 = Movie("Spirited Away", "Animation", 8.6)

movie2.display_info()
movie2.update_rating(12.5) 
movie2.display_info()