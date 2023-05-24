import re

import openai

openai.api_key = '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'
roles = {
    'girlfriend': "You are this user's girlfriend. You should be some funny and act like human",
    'friend': 'You are this user\'s friend. You should be some funny and act like human',
    'listener': 'You are this user\'s listener. You should listen to the user and '
                'respond with some advice give some motivation and be some funny',
}


def ask_chatgpt(prompt: str, role: str, old_messages='', language=None):
    try:
        promptRaw = f'Conversation theme: {roles.get(role)}\n{old_messages}\nUser: {prompt}'
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=promptRaw,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = completion.choices[0].text.strip()

        # Remove leading newline characters and words before them
        # output = re.sub(r'^\n*[^A-Za-z\n]*', '', output)
        output = re.sub(r'^.*\n+', '', output).replace(f'{role.capitalize()}: ', '')
        return output
    except openai.error.OpenAIError as e:
        print('Open AI error: %s' % e)
        exit()
