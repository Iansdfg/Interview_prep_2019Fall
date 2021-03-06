# fill the output you need at least O(U * G) operations. 
# To process the input user data you need at least O(U * S) operations. 
# It should therefore be impossible to do better than O(U * (S + G))
# Time: O((S + G) + U * (S + G)) => O((U + 1) * (S + G)) => O(U * (S + G))
# Space: O(S + G)
def fav_genra_old(userMap, genreMap):
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
            if genra_to_cnt[genra] == max_value:
                result[user].append(genra)
            
    return result
    # userMap = {"David": ["song1", "song2", "song3", "song4", "song8"],
    #            "Emma": ["song5", "song6", "song7"]
    # }
    # genreMap = {
    #     "Rock": ["song1", "song3"],
    #     "Dubstep": ["song7"],
    #     "Techno": ["song2", "song4"],
    #     "Pop": ["song5", "song6"],
    #     "Jazz": ["song8", "song9"]
    # }
def fav_genra(userMap, genreMap):
    output = {user:[] for user in userMap}

    song_to_genre = {}
    for genre in genreMap:
        for song in genreMap[genre]:
            song_to_genre[song] = genre

    for user in userMap:
        genre_to_cnt = {}
        max_val = float('-inf')
        for song in userMap[user]:
            genre = song_to_genre[song]
            if genre in genre_to_cnt:
                genre_to_cnt[genre] += 1
            else:
                genre_to_cnt[genre] = 0
            max_val = max(genre_to_cnt[genre], max_val)
        
        for genre in genre_to_cnt:
            if genre_to_cnt[genre] == max_val:
                output[user].append(genre)
    return output



    # output = {user:[] for user in userMap}

    # song_to_genre = {}
    # for genre in genreMap:
    #     for song in genreMap[genre]:
    #         song_to_genre[song] = genre

    # for user in userMap:
    #     genre_to_cnt = {}
    #     songs = userMap[user]
    #     for song in songs:
    #         genre = song_to_genre[song]
    #         genre_to_cnt[genre] = genre_to_cnt.get(genre, 0)+1

    #     for genre in genre_to_cnt:
    #         if genre_to_cnt[genre] == max(genre_to_cnt.values()):
    #             output[user].append(genre)
    # return output



    # output = {user:[] for user in userMap}

    # if userMap == {} or genreMap == {}:
    #     return output

    # song_to_genre = {}
    # for genre in genreMap:
    #     if genreMap[genre] == []:
    #         continue
    #     for song in genreMap[genre]:
    #         song_to_genre[song] = genre

    # if song_to_genre == {}:
    #     return output

    # for user in userMap:
    #     genre_to_cnt = {}
    #     for song in userMap[user]:
    #         genre = song_to_genre[song]
    #         genre_to_cnt[genre] = genre_to_cnt.get(genre, 0)+1

    #     output[user] = [key for key,val in genre_to_cnt.items() if val == max(genre_to_cnt.values())]
    
    # return output

# O(U*G*S)
import collections
def favGenres(userMap, genreMap):
    output = {}
    for user in userMap:
        songs = userMap[user]
        genre_to_count = collections.defaultdict(int)
        for song in songs:
            for k,v in genreMap.items():
                if song in v:
                    genre_to_count[k]+=1

        print(genre_to_count)
        output[user]=[key for key,val in genre_to_count.items() if val == max(genre_to_count.values())]
    return output

if __name__ == '__main__':
    # 1
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
    # # 2
    # userMap = {
    #     "David": ["song1", "song2"],
    #     "Emma": ["song3", "song4"]
    # }
    # genreMap = {}
    # # 3
    # userMap = {
    # }
    # genreMap = {}
    # # 4
    # userMap = {
    # }
    # genreMap = {
    #     "Rock": ["song1", "song3"],
    #     "Dubstep": ["song7"],
    #     "Techno": ["song2", "song4"],
    #     "Pop": ["song5", "song6"],
    #     "Jazz": ["song8", "song9"]
    # }
    # # 5
    # userMap = {"David": [],
    #            "Emma": []
    # }
    # genreMap = {
    #     "Rock": ["song1", "song3"],
    #     "Dubstep": ["song7"],
    #     "Techno": ["song2", "song4"],
    #     "Pop": ["song5", "song6"],
    #     "Jazz": ["song8", "song9"]
    # }
    # # 6
    # userMap = {"David": ["song1", "song2", "song3", "song4", "song8"],
    #            "Emma": ["song5", "song6", "song7"]
    # }
    # genreMap = {
    #     "Rock": [],
    #     "Dubstep": [],
    #     "Techno": [],
    #     "Pop": [],
    #     "Jazz": []
    # }
    print(fav_genra(userMap, genreMap))
