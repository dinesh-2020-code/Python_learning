
albums = [
    ("Welcome  to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Song1"),
         (2, "Song2"),
         (3, "Song3"),
     ]
     ),
    ("Bad company", "Bad Company", 1974,
     [
         (1, "Song4"),
         (2, "Song5"),
         (3, "Song6"),
     ]
     ),
    ("More Mayhem", "Emilda May", 2011,
     [
         (1, "Song7"),
         (2, "Song8"),
         (3, "Song9"),
     ]
     ),
    ("Ride the lightening", "Metallica", 1984,
     [
         (1, "Song10"),
         (2, "Song11"),
         (3, "Song12"),
     ]
     ),
    ]


for name, artist, year, songs in albums:
    print("Album: {}\nArtist: {}\nYear: {}\nSongs: {}\n"
          .format(name, artist, year, songs))
    
print(albums[2][3][1])   # (2,'Song8')