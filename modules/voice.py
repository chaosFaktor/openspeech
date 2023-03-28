
import modules.ANSIcolour as ansi
import os
import sys

##  own ##


#   Modules one directory up    #


import config as cfg
vccfg = cfg.Audio.Voices    




if cfg.Audio.Voices.voice=='espeak':
    base=' -s '+str(vccfg.espeak.speed)+' -p '+str(vccfg.espeak.pitch)+' -a '+str(vccfg.espeak.amplitude)+' -g '+str(vccfg.espeak.word_gap)
    def speak_de(txt):
        print(ansi.BLUE + 'AI   | ' + ansi.RESET + txt)
        os.system('espeak -v de'+base+' \"'+str(txt)+'\"')
        return True
    def speak_de_noEnd(txt):
        print(ansi.BLUE + 'AI   | ' + ansi.RESET + txt, end='')
        os.system('espeak -v de -z'+base+' \"'+str(txt)+'\"')
        return True
    def speak_de_noDialog(txt):
        print(txt)
        os.system('espeak -v de -z'+base+' \"'+str(txt)+'\"')
        return True

    def speak_en(txt):
        print(ansi.BLUE + 'AI   | ' + ansi.RESET + txt)
        os.system('espeak -v en'+base+'  \"'+str(txt)+'\"')
        return True

    def say_name():
        print('Motoko', end='')
        os.system('espeak -v ja もとこ')
    def say_nameln():
        print('Motoko')
        os.system('espeak -v ja もとこ')

    

else:
    raise NotImplementedError



##          Testing         ##
if __name__=='__main__':
    say_name()
