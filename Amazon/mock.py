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

def fav_genre(userMap, genreMap):
    result = {user: [] for user in userMap}

    song_to_genre = {}
    for genre in genreMap:
        for song in genreMap[genre]:
            song_to_genre[song] = genre

    for user in userMap:
        genre_to_cnt = {}
        max_val = float('-inf')
        for song in userMap[user]:
            genre = song_to_genre[song]
            genre_to_cnt[genre] = genre_to_cnt.get(genre, 0)+1
            max_val = max(max_val, genre_to_cnt[genre])

        for genre in genre_to_cnt:
            if genre_to_cnt[genre] == max_val:
                result[user].append(genre)
    return result

print(fav_genre(userMap, genreMap))


numOfWarehouses = 6
numOfRoads = 5
roads = [[1,2], [2,3], [3,4], [4,5], [6,3]]


from collections import defaultdict
def criticalConnection(numOfWarehouses, numOfRoads, roads):
    node_to_children = defaultdict(list)
    for x, y in roads:
        node_to_children[x].append(y)
        node_to_children[y].append(x)

    visited =[0] * (numOfWarehouses+1)
    dfn = [float('inf')] * (numOfWarehouses+1)
    low = [float('inf')] * (numOfWarehouses+1)
    parent = [-1] * (numOfWarehouses+1)
    count = 1
    result = []
    for node in range(1, numOfWarehouses+1):
        if not visited[node]:
            tarjan(node, node_to_children, visited, dfn, low, parent, count, result)
    return sorted(result)

def tarjan(node, node_to_children, visited, dfn, low, parent, count, result):
    visited[node] = 1
    dfn[node] = count
    low[node] = count
    count += 1
    for child in node_to_children[node]:
        if not visited[child]:
            parent[child] = node
            tarjan(child, node_to_children, visited, dfn, low, parent, count, result)
            low[node] = min(low[node], low[child])

            if low[child] > dfn[node]:
                former, later = min(child, node), max(child, node)
                result.append([former, later])

        if parent[node] != child:
            low[node] = min(low[node], dfn[child])

            
print(criticalConnection(numOfWarehouses, numOfRoads, roads))
