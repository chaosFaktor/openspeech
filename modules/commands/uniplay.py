import os


if config.Audio.musicPlayer == 'vlc':
    import vlc

else:
    raise NotImplementedError



if config.Audio.musicPlayer=='vlc':
    class MediaPlayer:
        def __init__(self, tracklist=[]):
            self.service = config.Audio.musicPlayer
            self.player = vlc.Instance()
            self.sources = config.Audio.musicPlayerPaths
            self.medialist = vlc.MediaList()


        def load(self, name, artist=None):
        #   Find name
            for i in self.sources:
                for file in os.listdir(i):
                    if name in file:
                        self.medialist.add_media(self.player.media_new(i+name))




        def play(self):
            self.player.set_media_list(self.medialist)
            self.player.play()
            time.sleep(self.player.get_length())
            

else:
    raise NotImplementedError
