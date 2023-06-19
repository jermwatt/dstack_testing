# dstack.ai + whisper example

This repo contains a simple test example in `processor.py` employing [dstack.ai](https://github.com/dstackai/dstack) for a speech-to-text translation task using a few example videos (in `/test_data/input_data`).

To run this example a `./dstack/profile.yaml` file must be defined as described in the [dstack documentation](https://dstack.ai/docs/reference/profiles.yml/).

For the test run here a very small CPU only machine on AWS was used via the following `profile.yaml` template:

```yaml
profiles:
  - name: small_test
    project: aws_test
    resources:
       memory: 8GB
    default: true
```

## Example overview

The main logic of the `processor.py` function for a given example video - given below - is to first strip off the audio portion of the file, and then employ whisper via the `transformers` library for processing.

```python
# create pipeline
pipe = pipeline(model="openai/whisper-base", device_map="auto")

# video name
video_name = video_file.split('/')[-1].split('.')[0]

# Save the audio clip as an MP3 file
audio_file = audio_directory + '/' + video_name + '.mp3'

# extract audio from video
extract_audio(video_file, audio_file)

# process audio
output = pipe(audio_file, chunk_length_s=30)
```
