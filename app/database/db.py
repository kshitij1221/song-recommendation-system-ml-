from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from datetime import datetime
from bson.objectid import ObjectId


from app.database.user import User
MONGO_URI="mongodb+srv://test:test@chatweb.1niledn.mongodb.net/songsr"
# client = MongoClient("mongodb+srv://test:test@chatweb.1niledn.mongodb.net/")
client = MongoClient(MONGO_URI)


chat_db = client.get_database("songsr")
users_collection = chat_db.get_collection("user")
songs_collection = chat_db.get_collection("songs")
play_history_collection = chat_db.get_collection("play_history")






def save_user(username, email, password):
    password_hash = generate_password_hash(password)
        
        # 
    
    
    users_collection.insert_one({'username': username, 'email': email, 'password': password_hash})
    
"""save_user("kshitij","singhkshitij.com","kshitij")"""
    
    

def get_user(username):
    user_data = users_collection.find_one({'username': username})
    return User(user_data['username'], user_data['email'], user_data['password']) if user_data else None

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

def save_play_history(song_id):
    play_history_collection.insert_one({
        'song_id': ObjectId(song_id),
        'played_at': datetime.utcnow()
    })


def get_last_five_played():
    last_five_played = play_history_collection.aggregate([
        {"$sort": {"played_at": -1}},  # Sort by most recent plays
        {"$limit": 5},  # Get the last 5 entries
        {
            "$lookup": {
                "from": "songs",
                "localField": "song_id",
                "foreignField": "_id",
                "as": "song_details"
            }
        },
        {"$unwind": "$song_details"}  # Unwind the song details array
    ])

    return list(last_five_played)  # Convert the cursor to a list