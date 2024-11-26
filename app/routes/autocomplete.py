@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query')
    suggestions = []

    if query:
        regex_query = {"$regex": query, "$options": "i"}
        song_data = mongo.db.songs.find({
            "$or": [
                {"title": regex_query},
                {"artist": regex_query},
                {"album": regex_query}
            ]
        }, {"title": 1, "_id": 0}).limit(5)

        suggestions = list(song_data)

    return jsonify({"suggestions": suggestions})