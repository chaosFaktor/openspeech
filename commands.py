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
        self.override_legitimation = False
    
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




cli=''
def run(raw_cmd):
    ## Parsing command
    cmd_object = Command(raw_cmd)
    if not cmd_object.override_legitimation:
        cmd_object.legitimated= is_arrinstr(config.Personality.names, cmd_object.commands[0])
        for i in config.Personality.names:
            cmd_object.commands[0]=cmd_object.commands[0].replace(i+' ', '').replace(i, '')
    else:
        cmd_object.legitimated=True

    if cmd_object.legitimated:
        with Command.CmdWalker(cmd_object) as walker:
            while walker.index < len(cmd_object.commands):
                if True: pass   #   First if Statement with highest priority

            #   Advanced-Legitimation-Detection (ALD) 
                elif walker.check(['hi', 'hey', 'hai', 'hallo']):
                    voice.speak_de(random.choice('hi', 'hey', 'hallo'))
                    cmd_object.override_legitimation=True
                elif walker.check(['bye', 'bei', 'schüss', 'schau', 'auf wiedersehen']):
                    if random.randint(0, 1)==0:
                        voice.speak_en('bye')
                    else:
                        voice.speak_de('auf wiedersehen')
            
            #   Intelligent curse counter offensive (ICCO)


            #   Novelty Questions
                elif walker.check(['stelle dich vor', 'stell dich vor', 'sage hallo', 'sag hallo']):
                    voice.speak_de_noEnd('Hallo ich bin ')
                    voice.say_name()
                    voice.speak_de(', ein sprachassistent basierend auf freier software.'),
                
                


                else:   #   Command could not be found
                    pass
                
                walker.next()

