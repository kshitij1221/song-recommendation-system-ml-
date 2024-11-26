
document.getElementById('searchBox').addEventListener('input', function () {
    const query = this.value;

    if (query.length > 2) {
        fetch(`/autocomplete?query=${query}`)
            .then(response => response.json())
            .then(data => {
                const suggestions = data.suggestions;
                const suggestionsList = document.getElementById('suggestions');
                suggestionsList.innerHTML = '';

                suggestions.forEach(song => {
                    const listItem = document.createElement('li');
                    listItem.textContent = song.title;
                    listItem.onclick = function() {
                        window.location.href = `/search?query=${song.title}`;
                    };
                    suggestionsList.appendChild(listItem);
                });
            });
    }
});
document.getElementById('toggleSongList').addEventListener('click', function() {
    var songList = document.getElementById('songList');
    if (songList.style.display === 'none') {
        songList.style.display = 'block';
        this.textContent = 'Hide Song List';
    } else {
        songList.style.display = 'none';
        this.textContent = 'Show Song List';
    }
});

async function searchSongs() {
    const songTitle = document.getElementById('songTitle').value;
    const response = await fetch(`/recommend?song_title=${encodeURIComponent(songTitle)}&n_recommendations=5`);
    const data = await response.json();

    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';

    if (data.message) {
        resultsContainer.innerHTML = `<p>${data.message}</p>`;
    } else {
        const list = document.createElement('ul');
        data.forEach(song => {
            const item = document.createElement('li');
            item.textContent = `${song['Track.Name']} by ${song['Artist.Name']} - Genre: ${song['Genre']} - Popularity: ${song['Popularity']}`;
            list.appendChild(item);
        });
        resultsContainer.appendChild(list);
    }
}

document.getElementById('recommendationForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const songName = document.getElementById('recommend_song_name').value;

    if (!songName) {
        alert("Please enter a song name.");
        return;
    }

    try {
        const response = await fetch('/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ song_name: songName }),
        });

        if (response.ok) {
            const data = await response.json();
            displayRecommendations(data);
        } else {
            const error = await response.json();
            alert(error.error || 'An error occurred');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred');
    }
});

function displayRecommendations(songs) {
    const recommendationsList = document.getElementById('recommendations');
    recommendationsList.innerHTML = ''; // Clear previous recommendations

    if (songs.length === 0) {
        recommendationsList.innerHTML = '<li>No recommendations found.</li>';
        return;
    }

    songs.forEach(song => {
        const listItem = document.createElement('li');
        listItem.textContent = song;
        recommendationsList.appendChild(listItem);
    });
}