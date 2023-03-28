import os
import json
import random
import config

##  own ##
import modules.voice as voice
import modules.ANSIcolour as ansi
from modules.math import *



class Command:
    def __init__(self, raw_cmd) -> None:
        self.commands=raw_cmd.split(' und ')
        self.legitimated = None
    
    class CmdWalker:
        def __init__(self, cmd):
            self.cmd=cmd
            self.index=0
        def __enter__(self):
            return self
        def __exit__(a, b, c, d):
            return

        def next(self):
            self.index+=1
        def check(self, arr):
            for i in arr:
                if i in self.cmd.commands[self.index]:
                    return True
            return False

        

    
    




            

def is_arrinstr(arr1, string):
    for i in arr1:
        if i in string:
            return True
    return False



override_legitimation=False
cli=''
def run(raw_cmd):
    ## Parsing command
    cmd_object = Command(raw_cmd)
    if not override_legitimation:
        cmd_object.legitimated= is_arrinstr(config.Personality.names, cmd_object.commands[0])
        for i in config.Personality.names:
            cmd_object.commands[0]=cmd_object.commands[0].replace(i+' ', '').replace(i, '')
    else:
        cmd_object.legitimated=True

    if cmd_object.legitimated:
        with Command.CmdWalker(cmd_object) as walker:
            while walker.index < len(cmd_object.commands):

                if walker.check(['stelle dich vor', 'stell dich vor', 'sage hallo', 'sag hallo']):
                    voice.speak_de_noEnd('Hallo ich bin ')
                    voice.say_name()
                    voice.speak_de(', ein sprachassistent basierend auf freier software.'),
                
                if walker.check(['fresse', 'klappe', 'maul']):
                    voice.speak_de_noEnd('Selber, Du ')

                    voice.speak_de_noDialog(config.Personality.curses_friendly[random.randint(0, len(config.Personality.curses_friendly)-1)])


                walker.next()

