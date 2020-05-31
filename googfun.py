from googletrans import *
import random
import PySimpleGUIWx as sg
import json
import locale

if locale.getdefaultlocale()[0] == 'ru_RU':
    from ru_RU import *
else:
    from en_US import *

print(init)

langs = ['ru', 'es', 'en', 'tr', 'ja', 'zh-CN', 'zh-TW', 'fr', 'sr', 'cy', 'is', 'uk', 'ko', 'af', 'pl', 'nl', 'fi',
         'hi', 'ar']
global translating
translating = False

def translate(stringt):

    try:
        print(tr)
        victim = stringt
        translator = Translator()
        desiredlang = random.choice(langs)
        print(trlog + desiredlang)
        translation = translator.translate(victim, dest=desiredlang)
        sourcelang = translation.src
        desiredlang = random.choice(langs)
        print(trlog + desiredlang)
        translation = translator.translate(translation.text, dest=desiredlang)
        desiredlang = random.choice(langs)
        print(trlog + desiredlang)
        translation = translator.translate(translation.text, dest=desiredlang)
        desiredlang = random.choice(langs)
        print(trlog + desiredlang)
        translation = translator.translate(translation.text, dest=desiredlang)
        desiredlang = random.choice(langs)
        print(trlog + desiredlang)
        translation = translator.translate(translation.text, dest=desiredlang)
        desiredlang = random.choice(langs)
        print(trlog + desiredlang)
        translation = translator.translate(translation.text, dest=desiredlang)
        desiredlang = random.choice(langs)
        print(trlog + desiredlang)
        translation = translator.translate(translation.text, dest=desiredlang)
        desiredlang = random.choice(langs)
        print(trlog + desiredlang)
        translation = translator.translate(translation.text, dest=desiredlang)
        translation = translator.translate(translation.text, dest=sourcelang)
        global translating
        translating = False
        print(trdone)
        return translation.text
    except json.decoder.JSONDecodeError:
        translating = False
        return googlebannotice
    except Exception:
        translating = False
        return etcexception


sg.theme('DarkBrown1')

layout = [[sg.Text(title, size=(25, 1), justification='center')],
            [sg.Text(netspeednote, size=(30, 1), justification='center')],
            [sg.InputText(default_text=ttt, size=(30, 1))],
            [sg.Text(result, justification='center')],
            [sg.InputText(font=('Comic Sans MS', 10), key='-OUTPUT-', size=(30, 1))],
            [sg.T(' ' * 15 ), sg.Button('Translate', focus=True), sg.Quit()]]

window = sg.Window(wintitle, layout)

print(initdone)

while True:
    try:
        event, values = window.read(timeout=10)
        if event in (None, 'Quit'):
            break
        if event in 'Translate':
            if not translating:
                translating = True
                window['-OUTPUT-'].update(translate(values[0]))
    except RuntimeError:
        print('Dirty Hack')
        break

window.close()
