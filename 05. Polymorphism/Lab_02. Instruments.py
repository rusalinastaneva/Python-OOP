def play_instrument(object):
    return object.play()

class Piano:
    def play(self):
        print("playing the piano")
piano = Piano()
play_instrument(piano)

