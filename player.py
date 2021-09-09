import sys

import simpleaudio

wave_obj = simpleaudio.WaveObject.from_wave_file(sys.argv[1])
play_obj = wave_obj.play()
play_obj.wait_done()
