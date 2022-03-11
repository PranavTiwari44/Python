from albums_Data import albums

SONG_PLACE = 3
SONG_NAME = 1

while True:
    print("My Music System!")
    for index, (album_Name, singer, year, song) in enumerate(albums):
        print("{} : {}".format(index+1, album_Name))
    album_Number = int(input("Choose an album (Invalid choice exit) :  "))
    if 1 <= album_Number <= len(albums):
        for numbers, song_Name in albums[album_Number-1][SONG_PLACE]:
            print("{}: {}".format(numbers, song_Name))
        song_Number = int(input("Choose a song (Invalid choice exit) :  "))
        print("Playing {}!".format(albums[album_Number-1][SONG_PLACE][song_Number-1][SONG_NAME]))
    print("============================================================================================================")