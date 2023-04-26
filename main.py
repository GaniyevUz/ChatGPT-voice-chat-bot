import os
from gtts import gTTS
from playsound import playsound

from config.models import ChatHistory
from helpers import ask_chatgpt, recognize

if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    print("""Welcome to the chatbot! 
          Available roles:
          1. Friend - A friend who can chat with you like best friends
          2. Girlfriend - A funny girlfriend for you 
          3. Listener - A person who you can talk your problems ot any other messages and he listens you and can give some advices""")
    role_selection = input('Choice one role for chatting: ')
    roles = {
        '1': 'friend',
        '2': 'girlfriend',
        '3': 'listener'
    }
    role = roles.get(role_selection, 'friend')
    file = f'tts.mp3'
    lang = 'en-US'
    try:
        while True:
            status, text = recognize(5)
            if not status:
                output = gTTS(text=text, lang=lang)
                output.save(file)
                playsound(file)
                ChatHistory.create('', text, role)
                continue
            old_messages = ChatHistory.get_old_messages(role, 5)
            print('Input:', text)
            gpt = ask_chatgpt(text, role, old_messages)
            output = gTTS(text=gpt, lang=lang)
            output.save(file)
            print('Output:', gpt)
            ChatHistory.create(text, gpt, role)
            playsound(file)
            if os.path.exists(file):
                os.remove(file)
    except AssertionError as e:
        print('Error:', e)
    except KeyboardInterrupt:
        # playsound(f"tts.mp3")
        pass
