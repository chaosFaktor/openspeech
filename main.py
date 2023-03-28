from vosk import Model, KaldiRecognizer, SetLogLevel
SetLogLevel(0)
import pyaudio
import json
import os

import threading

##   own    ##
import modules.ANSIcolour as ansi
import config
import commands


model = Model('./model')
rec = KaldiRecognizer(model, config.Audio.samplerate)


pa = pyaudio.PyAudio()
audio_stream = pa.open(rate=config.Audio.samplerate, channels=1, format=pyaudio.paInt16,
                       input=True, frames_per_buffer=config.Audio.frames_per_buffer)

os.system('clear')
print(ansi.Bold.RED+'Ready!'+ansi.RESET)


if config.listen==True:
    while True:
        pcm = audio_stream.read(config.Audio.frames_per_buffer)
        if rec.AcceptWaveform(pcm):

            #task_thread = threading.Thread(target=commands.task, args=(rec,))
            cmd = json.loads(rec.Result())
            
            if len(cmd['text'])>0:
                print(cmd)            
            commands.run(cmd['text'])

else:
    while True:
        inp=input('->')
        commands.run(inp)
'''
except KeyboardInterrupt:
    exit()
except Exception as e:
    print(ansi.Bold.RED+'Exception  occured:' + e + ansi.RESET)
'''