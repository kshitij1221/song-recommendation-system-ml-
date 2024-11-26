@app.route('/test')
@login_required
def index():
    songs = get_all_songs()
    last_five_played = get_last_five_played()
    return render_template('index.html', songs=songs, last_five_played=last_five_played)