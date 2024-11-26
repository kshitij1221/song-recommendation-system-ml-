# Define and fit clustering pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()), 
    ('kmeans', KMeans(n_clusters=10, random_state=42))
])
pipeline.fit(X)
data['cluster_label'] = pipeline.predict(X)

@app.route('/recommend', methods=['GET'])
def recommend_songs():
    song_title = request.args.get('song_title')
    n_recommendations = int(request.args.get('n_recommendations', 5))

    if song_title not in data['Track.Name'].values:
        return jsonify({"message": f"Song '{song_title}' not found in the dataset."})

    song_cluster = data[data['Track.Name'] == song_title]['cluster_label'].values[0]
    similar_songs = data[data['cluster_label'] == song_cluster]
    similar_songs = similar_songs[similar_songs['Track.Name'] != song_title]
    recommendations = similar_songs.head(n_recommendations)

    
    result = recommendations[['Track.Name']].to_dict(orient='records')
    return jsonify(result)