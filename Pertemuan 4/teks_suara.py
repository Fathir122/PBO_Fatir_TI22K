rom gtts import gTTS
import os

def text_to_speech(text, language='id', output_file='hasil.mp3'):
    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the audio file
        tts.save(output_file)

        # Play the audio file
        os.system(f'start {output_file}')

    except Exception as e:
        print(f"Error converting text to speech: {e}")

if _name_ == "_main_":
    text = "Punten, boleh pinjam seratus dulu ngga?"
    language = 'id'
    output_file = 'hasil.mp3'

    text_to_speech(text, language, output_file)