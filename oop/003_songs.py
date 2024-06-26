class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=None) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an Album, using it's track list
    
    Attributes:
        name (str): The name of the album
        year (int): The year album was released
        artist: (Artist): The artist responsible for the album. 
            If not specified, the artist will default to an artist with the name
            "Various Artists".
        tracks (List[Song]): A list of the songs on the album. 

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): The title of a song to add
            position (int, optional): If specified, the song will be added to that position in the track list - inserting it between
            other songs if necessary. Otherwise, the song will be added to the end of the list. Defaults to None.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            if position is None:
                self.tracks.append(song)
            else:
                self.tracks.insert(position, song)


class Artist:
    """Basic class to store Artist details.

    Attributes:
        name (str): The name of the artist
        albums (list(Album)): A list of the albums by this artist.
            The list includes only those albums in this collection,
            it is not an exhaustive list of the artist's published items.

    Methods:
        add_album: Use to add a new album to the artist's albums list.
    """

    def __init__(self, name) -> None:
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present in the list,
                it will not be added again (although this is yet to be implemented)
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """Add a new song to the collections of albums
        
        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doesn't already exists. 

        Args:
            name (str): The name of the album
            year (int): The year the album was produced
            title (str): The title of the song.
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(f"{name} not found")
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print(f"Found album {name}")

        album_found.add_song(title)


def find_object(field, object_list):
    """Check `object_list` to see if an object with a `name` attribute equal to `field` exists, return it if so.

    Args:
        field (_type_): _description_
        object_list (_type_): _description_
    """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []
    with open('albums.txt', 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)   
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            
            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file name

    Args:
        artist_list (list[Artist]): Contains the list of artist names
    """
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)
