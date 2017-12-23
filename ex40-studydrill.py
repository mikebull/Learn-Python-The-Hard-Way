class Album(object):

    def __init__(self, songs):
        self.songs = songs

    def play_album(self):
        i = 0
        for song in self.songs:
            i += 1
            print(f"Playing song #{i}:")
            song.sing_me_a_song()

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

songs = [happy_bday, bulls_on_parade]

a_ratm_xmas = Album(songs)

a_ratm_xmas.play_album()