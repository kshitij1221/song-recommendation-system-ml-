@app.route('/search', methods=['GET'])
def search_results():
    query = request.args.get('query')
    song = mongo.db.songs.find_one({
        "$or": [
            {"title": query},
            {"artist": query},
            {"album": query}
        ]
    })

    if song:
        return render_template('index.html', song=song)
    else:
        flash('No song found!', 'error')
        return redirect(url_for('index'))