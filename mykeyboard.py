import numpy as np
import readchar
from simpleaudio import WaveObject

from sin_oscillator import SineOscillator
from wave_adder import WaveAdder

frequency = {
    "a": 262,
    "s": 294,
    "d": 330,
    "f": 349,
    "g": 392,
    "h": 440,
    "j": 494,
    "b": 523,
    "n": 587,
    "m": 659,
    ",": 698,
    ".": 783,
    "/": 880,
    "\\": 987
}


def get_sine_oscillator(freq: int, amp=0.1):
    sin = SineOscillator(freq=freq)
    return sin


def setup():

    oscillator_dict = {}
    for k, v in frequency.items():
        wav = get_sine_oscillator(v)
        oscillator_dict[k] = wav

    return oscillator_dict


print("========   system message   =========")
print("keyboard software has been activated!")
print("If you want to exit, press `q`")
print("=====================================")

oscillator_dict = setup()

while 1:
    kb = readchar.readchar()
    print(kb)
    if kb == "q":
        print("qが入力されたので終了します")
        break

    oscillator_list = [oscillator_dict.get(s, False) for s in kb]

    if not all(oscillator_list):
        continue

    wave = WaveAdder(*oscillator_list)

    iter(wave)
    wav = [next(wave) for _ in range(int(44100 * 1))]
    wav = np.array(wav)
    wav = np.int16(wav * 0.1 * (2 ** 15 - 1))
    wav_obj = WaveObject(wav)
    play_obj = wav_obj.play()
