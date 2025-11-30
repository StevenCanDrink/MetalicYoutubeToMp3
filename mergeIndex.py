import os
from pydub import AudioSegment

# Specify your directory path
directory_path = "/home/six/Documents/project/tubetomp3/downloads"

# Initialize an empty list to store AudioSegments
audio_segments = []

# Retrieve all MP3 files in the directory
for file_name in os.listdir(directory_path):
    if file_name.endswith(".mp3"):
        file_path = os.path.join(directory_path, file_name)
        audio_segment = AudioSegment.from_mp3(file_path)
        audio_segments.append(audio_segment)

# Check if there are MP3 files to merge
if audio_segments:
    # Start with the first file
    merged_audio = audio_segments[0]

    # Append each subsequent file to the merged audio
    for segment in audio_segments[1:]:
        merged_audio += segment

    # Export the merged audio to a new MP3 file
    output_path = os.path.join(directory_path, "merged_output.mp3")
    merged_audio.export(output_path, format="mp3")
    print(f"MP3 files have been merged successfully! Output file saved at: {output_path}")
else:
    print("No MP3 files found in the specified directory.")
