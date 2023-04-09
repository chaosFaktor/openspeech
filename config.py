listen = False
speak = False

class Audio:
    samplerate = 44100*2
    #samplerate = 22050
    frames_per_buffer = 4096
    #frames_per_buffer = 2048

    musicPlayer='vlc'
    mediaPlayer='vlc'
    musicPlayerPaths=['./archive/music/']   #   Entrys must end with '/'

    class Voices:
        voice='espeak'
        class espeak:
            speed = 150 #   Unit: Words Per Minute
            pitch   = 45
            amplitude=100
            word_gap = 1 #  Gap in *10ms between words

class Personality:
    names=['motto', 'moto'] # Motoko

