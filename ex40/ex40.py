class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print line

bbhmm = Song(["Bitch, better have my money!",
            "Pay me what you owe me, don't act like you forgot",
            "...", "Shit, your wife in the backseat  of my brand new foreign car"])

bbhmm.sing()
