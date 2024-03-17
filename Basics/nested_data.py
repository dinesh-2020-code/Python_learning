from albums_data import albums

for name, artist, year, songs in albums:
    print("Album: {}\nArtist: {}\nYear: {}\nSongs: {}\n"
          .format(name, artist, year, songs))
    
print(albums[2][3][1])   # (2, "Keeping a Rendezvous")
