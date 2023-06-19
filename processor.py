
from transformers import pipeline
from moviepy.editor import VideoFileClip
import os

# create working directores
cwd = os.getcwd()
test_data_path = cwd + '/test_data'
input_data_path = test_data_path + '/input_data'
output_data_path = test_data_path + '/output_data'

# create directory to store temp audio files called '/audio_files'
audio_directory = '/audio_files'
if not os.path.exists(audio_directory):
    os.makedirs(audio_directory)

# create pipeline
pipe = pipeline(model="openai/whisper-base", device_map="auto")

# extract audio from video
def extract_audio(mp4_file, output_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(output_file)

def processor():
    # import filenames from input_data directory 
    file_paths_to_process = []
    for filename in os.listdir(input_data_path):
        file_paths_to_process.append(input_data_path + '/' + filename)
     
    # loop over files and process    
    for video_file in file_paths_to_process:

        # video name
        video_name = video_file.split('/')[-1].split('.')[0]

        # Save the audio clip as an MP3 file
        audio_file = audio_directory + '/' + video_name + '.mp3'

        # extract audio from video
        extract_audio(video_file, audio_file)

        # process audio
        output = pipe(audio_file, chunk_length_s=30)
        print(output, flush=True)

        # write to output
        with open(output_data_path + '/' +
                  video_file.split('/')[-1].split('.')[0] + '.txt', 'w') as f:
            f.write(output['text'])

if __name__ == '__main__':
    processor()