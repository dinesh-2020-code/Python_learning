import jukedatabox as jd

#----------------------------Main method----------------------------
choice_list = 1, 2, 3, 4
choice = 0
# print(dir(jd))
while True:
    jd.albumList()
    choice = int(input())
    
    if choice in choice_list:
        print("Please choose your song:")
        if choice == 1:
            jd.selectSong (choice - 1, jd.getData())
            
        elif choice == 2:
            jd.selectSong (choice - 1, jd.getData())
            
        elif choice == 3:
            jd.selectSong (choice - 1, jd.getData())
            
        elif choice == 4:
            jd.selectSong (choice - 1, jd.getData())
            
    else:
        print("\nInvalid Choice\n")
        print('=' * 72)
        break
