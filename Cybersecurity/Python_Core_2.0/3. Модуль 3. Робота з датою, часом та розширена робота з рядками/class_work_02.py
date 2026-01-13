files = ['video.avi', 'music.mp3', 'image.png', 'document.pdf', 'archive.zip', 'folder']
for file in files:
    if '.' in file:
        name, extension = file.rsplit('.', 1)
        print(f"File: {name}, Extension: {extension}")
    else:
        print(f"File: {file} has no extension")