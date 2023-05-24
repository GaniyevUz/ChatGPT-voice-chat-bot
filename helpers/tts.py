import os

from gtts import gTTS
from playsound import playsound

from test import speech


def tts(text, role='friend'):
    roles = {
        'friend': ('Mike', 'en-us'),
        'girlfriend': ('Mary', 'en-us')
    }
    file = 'tts.mp3'
    r = speech({
        'key': 'bb690371babf4fed993df435a191c0d8',
        'hl': roles.get(role)[1],
        'v': roles.get(role)[0],
        'src': text,
        'r': '0',
        'c': 'mp3',
        'f': '44khz_16bit_stereo',
        'ssml': 'false',
        'b64': 'false',
        'filename': file
    })
    # output = gTTS(text=gpt, lang=lang)
    # output.save(file)
    if not r.get('response'):
        output = gTTS(text=text)
        output.save(file)
    playsound(file)
    if os.path.exists(file):
        os.remove(file)
