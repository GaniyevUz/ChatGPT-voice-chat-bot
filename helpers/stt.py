from random import choice

import speech_recognition as sr

r = sr.Recognizer()

errors = ("Why are you keeping silence?", "Please say something", "Are you there?", "I'm sorry, I didn't get that.")


def recognize(duration=3, lang='en'):
    with sr.Microphone() as source:
        try:
            print("Ask Something...")
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=duration)
            # audio_data = r.listen(source, phrase_time_limit=3)
            print("Recognizing...")
            # convert speech to text
            text = r.recognize_google(audio_data)
            return True, text
        except sr.UnknownValueError:
            return False, choice(errors)
