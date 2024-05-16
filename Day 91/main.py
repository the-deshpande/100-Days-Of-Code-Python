from pypdf import PdfReader
from google.cloud import texttospeech
from dotenv import load_dotenv

load_dotenv()

client = texttospeech.TextToSpeechClient()

voice = texttospeech.VoiceSelectionParams({
    'language_code': 'en-US',
    'ssml_gender': texttospeech.SsmlVoiceGender.FEMALE
})

audio_config = texttospeech.AudioConfig({
    'audio_encoding': texttospeech.AudioEncoding.MP3
})

path = f'content/{input("Enter the name of the pdf file: ")}.pdf'
reader = PdfReader(path)

with open('output.mp3', 'wb') as output:
    for page in reader.pages:
        print(page.extract_text())

        synthesis_input = texttospeech.SynthesisInput({
            'text': page.extract_text()
        })

        response = client.synthesize_speech({
            'input': synthesis_input,
            'voice': voice,
            'audio_config': audio_config
        })

        output.write(response.audio_content)
        print("Your audio file is ready!")
