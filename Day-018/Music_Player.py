class musicPlayer:
    def __init__(self,song,volume,status="playing"):
        self.song = song
        self.volume = volume
        self.is_playing = status

    def play(self):
        self.is_playing = "playing"
        return  self.is_playing

    def pause(self):
        self.is_playing = "paused"
        return self.is_playing

    def increase_volume(self,amount):
        self.volume += amount

    def decrease_volume(self,amount):
        self.volume -= amount


    def show_status(self):
        print(f"current song : {self.song}")
        print(f"Volumn: {self.volume}")
        print(f"Status: {self.is_playing}")

my_music_player = musicPlayer(song = "Shape of You",volume = 50 ,status = "playing")

my_music_player.show_status()
my_music_player.increase_volume(20)
my_music_player.decrease_volume(10)
my_music_player.show_status()

my_music_player.pause()
my_music_player.show_status()

my_music_player.play()
my_music_player.show_status()