import asyncio
import threading
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from time import sleep
import sys
import speech_recognition as SR 
import model

r = SR.Recognizer()

comandos_de_saludo = ['hola', 'cómo estás', 'cómo te va']
comandos_de_despedida = ['terminar la sesión', 'cerrar la sesión']

def animate_text(text, delay=0.08):
    for line in text.splitlines():
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(delay)
        print('')

async def async_animate_text(text, delay=0.08):
    for line in text.splitlines():
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            await asyncio.sleep(delay)
        print('')

def play_sound_threaded(sound):
    threading.Thread(target=play, args=(sound,)).start()
async def saludo():
    saludo = 'hola caballero, como le va?'
    tts = gTTS(saludo, lang='es')
    tts.save("output.mp3")
    sound = AudioSegment.from_mp3("output.mp3")
    await asyncio.gather (asyncio.to_thread(play_sound_threaded, sound),async_animate_text(saludo))
async def despedida():
    tts = gTTS('se cerró la sesión', lang='es')
    tts.save('output.mp3')
    await async_animate_text('Se cerró la sesión')
    play_sound_threaded(AudioSegment.from_mp3('output.mp3'))
    await asyncio.sleep(2)


async def escuchar_analizar():
    tts = gTTS('sea bienvenido caballero', lang='es')
    tts.save('output.mp3')
    play_sound_threaded(AudioSegment.from_mp3('output.mp3'))
    await asyncio.gather(async_animate_text('sea bienvenido caballero'))
    while True:
        with SR.Microphone() as source:
            await async_animate_text('Ya puedes hablar', 0.01)
            audio = r.listen(source)
            try:
                await async_animate_text('Analizando texto', 0.02)
                text = r.recognize_google(audio, language='es-ES')
                text = str(text).lower()
                if any(palabras in text for palabras in comandos_de_despedida):
                    await despedida()
                    break
                elif any(palabras in text for palabras in comandos_de_saludo):
                    await saludo()
                else:
                    try:
                        # leer lectura de voz. cambiar con la api de la ia
                        

                        llm = model.load_model()
                        response = model.query(text, llm)

                        tts = gTTS(response, lang='es')
                        tts.save("output.mp3")
                        sound = AudioSegment.from_mp3("output.mp3")
                        await asyncio.gather(async_animate_text(response),asyncio.to_thread(play_sound_threaded, sound))
                    except Exception as e:
                        print(e)
            except Exception as e:
                print('Ocurrió un error', e)

asyncio.run(escuchar_analizar())
