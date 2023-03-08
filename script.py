import os

# Set the directory containing the MP3 files
print("input directory: ")
directory = input()

# Create an empty list to store the filenames
filenames = []

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        # Add the filename to the list
        filenames.append(filename)

# Create a new .m3u playlist file with the name of the directory
playlist_name = os.path.basename(directory) + ".m3u"
with open(os.path.join(directory, playlist_name), "w") as f:
    # Write each filename to the playlist file
    for filename in filenames:
        f.write(filename + "\n")
