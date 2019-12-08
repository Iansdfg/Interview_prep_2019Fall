# def favGenres(userSongs, songGenres):
#     output = {}
#     d_song = {}
    
#     for genre in songGenres:
#         for song in songGenres[genre]:
#             d_song[song] = genre
            
#     for user in userSongs:
#         song_list = userSongs[user]
#         count = {}

#         for song in song_list:
#             genre = d_song[song]
#             count[genre] = count.get(genre,0) + 1

#         output[user] = [key for key, val in count.items() if val == max(count.values())]
    
#     return output
def fav_genra(userMap, genreMap):
    result = { user: [] for user in userMap}
    if not userMap or not genreMap:
        return result 

    song_to_genra = dict()
    for genre in genreMap:
        songs = genreMap[genre]
        for song in songs:
            song_to_genra[song] = genre

    for user in userMap:
        genra_to_cnt = dict()
        max_value = float('-inf')
        for song in userMap[user]:
            genra = song_to_genra[song]

            if genra in genra_to_cnt:
                genra_to_cnt[genra] += 1
            else:
                genra_to_cnt[genra] = 1

            max_value = max(genra_to_cnt[genra], max_value)

        for genra in genra_to_cnt:
            # print(genra, genra_to_cnt[genra], max_value)
            if genra_to_cnt[genra] == max_value:
                result[user].append(genra)
    return result

if __name__ == '__main__':
    userMap = {"David": ["song1", "song2", "song3", "song4", "song8"],
               "Emma": ["song5", "song6", "song7"]
              }
    genreMap = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]
    }

    # userMap = {
    #     "David": ["song1", "song2"],
    #     "Emma": ["song3", "song4"]
    # }
    # genreMap = {}

    print(fav_genra(userMap, genreMap))

