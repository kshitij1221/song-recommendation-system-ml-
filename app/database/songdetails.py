def save_song(title, artist, album, file_path):
   song_data = {
        'title': title,
        'artist': artist,
        'album': album,
        'file_path': file_path
    }
   songs_collection.insert_one(song_data)

def get_all_songs():
    return list(songs_collection.find())

def search_song(query):
    return songs_collection.find_one({
        '$or': [
            {'title': {'$regex': query, '$options': 'i'}},
            {'artist': {'$regex': query, '$options': 'i'}}
        ]
    })