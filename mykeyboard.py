import sys

import numpy as np
import readchar
from simpleaudio import WaveObject

from sin_oscillator import SineOscillator

frequency = {
    "a": 262,
    "s": 294,
    "d": 330,
    "f": 349,
    "g": 392,
    "h": 440,
    "j": 494,
    "k": 523,
}


def get_wav_data(freq: int, amp=0.1):
    sin = SineOscillator(freq=freq)
    iter(sin)
    wav = [next(sin) for _ in range(44100 * 1)]
    wav = np.array(wav)
    wav = np.int16(wav * amp * (2 ** 15 - 1))
    return wav


print("========   system message   =========")
print("keyboard software has been activated!")
print("If you want to exit, press `q`")
print("=====================================")

while 1:
    kb = readchar.readchar()
    print(kb)
    if kb == "q":
        print("qが入力されたので終了します")
        break
    freq = frequency.get(kb)
    if freq is None:
        continue
    wav = get_wav_data(freq)
    wave_obj = WaveObject(wav)
    play_obj = wave_obj.play()
    play_obj.wait_done()
