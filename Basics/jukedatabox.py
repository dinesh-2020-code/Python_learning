"""
    Jukedata module
    used in demojukebox.py file
"""
SONGS_LIST_INDEX = 3 # Constant
SONG_TITLE_INDEX = 1

def getData():
    """This function returns the albums list"""
    albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
    ]
    return albums


def albumList():
    """This functions prints the list of albums available (invalid choice exits):"""
    print('=' * 72)
    print("please Choose your album")
    albums = getData()
    # for index, (title, artist, year, songs) in enumerate(albums):
    #     print("{}: {}".format(index + 1, title))
    
    for index, album in enumerate(albums):
        print("{}: {}".format(index + 1, album[0]))


def selectSong(ch, albums):
    """This function selects the song and play that."""
    songs_lst = albums[ch][SONGS_LIST_INDEX]
    for track_no, song_name in songs_lst:
        print("{}: {}".format(track_no, song_name))
        
    song_no = int(input())
    if 1 <= song_no <= len(songs_lst):
        print("Playing {}".format(songs_lst[song_no - 1][SONG_TITLE_INDEX]))
    else:
        pass
    
