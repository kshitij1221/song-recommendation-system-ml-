@app.route('/play/<song_id>')
def play_song(song_id):
    song = songs_collection.find_one({'_id': ObjectId(song_id)})
    if song:
        save_play_history(song_id)  # Log the song play in the history
        return render_template('index.html', song=song, songs=get_all_songs(), last_five_played=get_last_five_played())
    else:
        flash('Song not found!', 'error')
        return redirect(url_for('index'))