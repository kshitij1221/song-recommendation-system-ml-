@app.route('/upload', methods=['GET', 'POST'])
def upload_song():
    if request.method == 'POST':
        title = request.form.get('title')
        artist = request.form.get('artist')
        album = request.form.get('album')
        file = request.files['file']

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Save only the filename in the database, not the full file path
            save_song(title, artist, album, filename)
            
            flash('Song uploaded successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Failed to upload the song!', 'error')
    return render_template('upload.html')
