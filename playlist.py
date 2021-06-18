playlist = {
	'title': 'My Playlist',
	'author': 'Mike',
	'songs': [
		{'title': 'Highway to Hell', 'artist': ['AC/DC'], 'duration': 2.5},
		{'title': 'Song 2', 'artist': ['Blur'], 'duration': 2},
		{'title': 'Call Me Maybe', 'artist': [], 'duration': 1}
	]
}

for song in playlist['songs']:
	print(song['title'])

total_duration = 0

for song in playlist['songs']:
	total_duration += song['duration']

print(total_duration)