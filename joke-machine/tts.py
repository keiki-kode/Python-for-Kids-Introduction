"""Synthesizes speech from the input string of text or ssml. Can play the returned audio without having to save it to a file.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
    export export GOOGLE_APPLICATION_CREDENTIALS=<your_credentials>.json
    sudo pip3 install --upgrade google-cloud-texttospeech
https://cloud.google.com/text-to-speech/docs/reference/libraries#client-libraries-install-python
"""
from google.cloud import texttospeech
import pygame
import io
import os
os.putenv('DISPLAY', ':0.0')
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/<your_credentials>.json")

def speak(mytext):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    # response = client.list_voices()
    # print(response)

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=mytext)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Wavenet-F',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # # The response's audio_content is binary.
    # with open('output.mp3', 'wb') as out:
    #     # Write the response to the output file.
    #     out.write(response.audio_content)
    #     print('Audio content written to file "output.mp3"')

    freq = 24000    # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 2048   # number of samples (experiment to get right sound)
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.set_volume(1.0)
    pygame.display.set_mode((1, 1))

    pygame.init()  # this is needed for pygame.event.* and needs to be called after mixer.init() otherwise no sound is played
    with io.BytesIO() as f:  # use a memory stream
        f.write(response.audio_content)
        f.seek(0)
        pygame.mixer.music.load(f)
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.event.set_allowed(pygame.USEREVENT)
        pygame.mixer.music.play()
        pygame.event.wait()  # play() is asynchronous. This wait forces the speaking to be finished before closing f and returning
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
