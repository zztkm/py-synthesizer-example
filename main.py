from save_wav import wave_to_file
from wave_adder import WaveAdder
from sin_oscillator import SineOscillator
from triangle_oscillator import TriangleOscillator
from sawtooth_oscillator import SawtoothOscillator
from square_oscillator import SquareOscillator

gen = WaveAdder(
    SineOscillator(freq=440),
    TriangleOscillator(freq=220, amp=0.8),
    SawtoothOscillator(freq=110, amp=0.6),
    SquareOscillator(freq=55, amp=0.4),
)

iter(gen)
wav = [next(gen) for _ in range(44100 * 7)]
wave_to_file(wav, fname="prelude_one.wav")
