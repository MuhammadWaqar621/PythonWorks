class Artist:
    def __init__(self,name):
        self.name=name
        self.artsongs=[]
    def add_song(self,song):
        self.artsongs.append(song)
    def showAllSongs(self):
        for s in self.artsongs:
            s.showSong()
    def getArtSongs(self):
        return self.artsongs
    
class Song:
    def __init__(self,title,artlist):
        self.title=title
        self.artlist=artlist
    def showSong(self):
        print ("Title : ",self.title,"\t Artlist :" ,self.artlist.name)
        
class Playlist:
    def __init__(self,title):
        self.playlist_title=title
        self.playlist=[]
    def add_songs(self,artsonglist):
        self.playlist=artsonglist
    def add_song(self,song):
        self.playlist.append(song)
    def showPlistSongs(self):
        print ("PlayList Title: ",self.playlist_title," \n")
        for s in self.playlist:
            s.showSong()
    
        
# Test Cases
# Create artist and their songs 
newband = Artist("A&H")
newband.add_song(Song("Beginning",newband))
newband.add_song(Song("Turn",newband)) 
newband.add_song(Song("Light",newband)) 
newband.add_song(Song("Forever",newband)) 
newband.add_song(Song("New Life",newband)) 
newband.add_song(Song("Supernatural",newband)) 
newband.add_song(Song("Miracles",newband))
# Show all songs of the artist
newband.showAllSongs()
# Create artist and two songs
band2 = Artist("Race") 
song1 = Song("Fast", band2) 
song2 = Song("Finish Line", band2)
# Create playlist
playlist1 = Playlist("My Favorite Songs") 
# Add all artist songs to playlistplaylist1.add_artSongs(newband.getArtSongs()) 
# Add one song to playlist playlist1.add_song(song2)
# Show all songs in playlist
playlist1.showPlistSongs()