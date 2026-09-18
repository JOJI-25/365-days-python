class Song:
    def __init__(self, title, artist, duration):
        if duration < 0:
            raise ValueError("Song duration cannot be negative.")
        self.title = title
        self.artist = artist
        self.duration = duration 

    def __str__(self):
        return f"{self.title} - {self.artist} - {self.duration} sec"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.current_index = None

    def add_song(self, song):
        for s in self.songs:
            if s.title.lower() == song.title.lower() and s.artist.lower() == song.artist.lower():
                print(f"'{song.title}' by {song.artist} is already in the playlist.")
                return

        self.songs.append(song)
        
        if self.current_index is None:
            self.current_index = 0
        print(f"Added: {song.title}")

    def remove_song(self, title, artist):
        found = False
        for i, song in enumerate(self.songs):
            if song.title.lower() == title.lower() and song.artist.lower() == artist.lower():
                self.songs.pop(i)
                found = True
                print(f"Removed: {title}")
                break

        if not found:
            print(f"Song '{title}' by {artist} not found in the playlist.")
            return

        if not self.songs:
            self.current_index = None
        elif self.current_index >= len(self.songs):
            self.current_index = len(self.songs) - 1

    def display_playlist(self):
        print(f"\nPlaylist: {self.name}")
        if not self.songs:
            print("Songs: (Playlist is empty)")
            return

        print("Songs:")
        for i, song in enumerate(self.songs, 1):
            marker = " (Current)" if (self.current_index is not None and i - 1 == self.current_index) else ""
            print(f"{i}. {song}{marker}")
        print(f"Total duration: {self.get_total_duration()} sec")

    def find_song(self, title):
        matches = [song for song in self.songs if title.lower() in song.title.lower()]
        if matches:
            print(f"\nFound {len(matches)} match(es) for '{title}':")
            for song in matches:
                print(f"- {song}")
        else:
            print(f"\nNo songs found matching '{title}'.")

    def get_total_duration(self):
        return sum(song.duration for song in self.songs)

    def next_song(self):
        if not self.songs:
            print("Playlist is empty. No next song.")
            return None

        if self.current_index < len(self.songs) - 1:
            self.current_index += 1
            print(f"Moved to next song: {self.songs[self.current_index].title}")
        else:
            print("Already at the final song. No next song.")
        return self.songs[self.current_index]

    def previous_song(self):
        if not self.songs:
            print("Playlist is empty. No previous song.")
            return None

        if self.current_index > 0:
            self.current_index -= 1
            print(f"Moved to previous song: {self.songs[self.current_index].title}")
        else:
            print("Already at the first song. No previous song.")
        return self.songs[self.current_index]



workout_playlist = Playlist("Workout")

song1 = Song("Song A", "Artist 1", 210)
song2 = Song("Song B", "Artist 2", 180)
song3 = Song("Song C", "Artist 3", 240)


workout_playlist.add_song(song1)
workout_playlist.add_song(song2)
workout_playlist.add_song(song3)

workout_playlist.add_song(Song("Song A", "Artist 1", 210))


workout_playlist.display_playlist()

print("\n--- Navigation ---")
workout_playlist.next_song()  
workout_playlist.next_song()  
workout_playlist.next_song()  
workout_playlist.previous_song()  
workout_playlist.previous_song()  
workout_playlist.previous_song()  

print("\n--- Searching ---")
workout_playlist.find_song("Song")

print("\n--- Removing ---")
workout_playlist.remove_song("Song B", "Artist 2")
workout_playlist.remove_song("Song D", "Artist 4")  

workout_playlist.display_playlist()

