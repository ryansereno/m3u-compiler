import os

music_path = input()
full_path = os.path.join(os.path.expanduser("~"), music_path)

ext = [".mp3"]

files = os.scandir(full_path)
playlist = []

for entry in files:
    if entry.is_file():
        if os.path.splitext(entry.name)[1].lower() in ext:
            playlist.append(entry.name + " \n")


file = open(os.path.join(full_path, "{}.m3u".format(
    os.path.basename(full_path)
)), "w")

file.writelines(playlist)
file.close()
