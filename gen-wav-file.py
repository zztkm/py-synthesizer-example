import librosa
import numpy as np

from save_wav import wave_to_file
from sawtooth_oscillator import SawtoothOscillator
from sin_oscillator import SineOscillator
from square_oscillator import SquareOscillator
from triangle_oscillator import TriangleOscillator
from wave_adder import WaveAdder


def get_val(osc, sample_rate=44100):
    return [next(osc) for i in range(sample_rate)]


def get_seq(osc, notes=["C4", "E4", "G4"], note_lens=[0.5, 0.5, 0.5]):
    samples = []
    osc = iter(osc)
    for note, note_len in zip(notes, note_lens):
        osc.freq = librosa.note_to_hz(note)
        for _ in range(int(44100 * note_len)):
            samples.append(next(osc))
    return samples


# NOTE: そのうち関数にしてすでにファイルが作りたいやつを指定できるようにする
gen = WaveAdder(
    SineOscillator(freq=440),
    TriangleOscillator(freq=220, amp=0.8),
    SawtoothOscillator(freq=110, amp=0.6),
    SquareOscillator(freq=1000, amp=0.4),
)

sin_440 = WaveAdder(
    SineOscillator(freq=440),
)
# シとドの間
sin_512 = WaveAdder(
    SineOscillator(freq=512),
)

sin_530 = WaveAdder(
    SineOscillator(freq=530),
)

sin_880 = WaveAdder(
    SineOscillator(freq=880),
)

iter(gen)
wav = [next(gen) for _ in range(44100 * 4)]
wave_to_file(wav, fname="prelude_one.wav")

iter(sin_440)
wav = [next(sin_440) for _ in range(44100 * 4)]
wave_to_file(wav, fname="sin-440.wav")

iter(sin_512)
wav = [next(sin_512) for _ in range(44100 * 4)]
wave_to_file(wav, fname="sin-512.wav")

iter(sin_530)
wav = [next(sin_530) for _ in range(44100 * 4)]
wave_to_file(wav, fname="sin-530.wav")
iter(sin_880)
wav = [next(sin_880) for _ in range(44100 * 4)]
wave_to_file(wav, fname="sin-880.wav")

dur = 10
osc = WaveAdder(
    SineOscillator(librosa.note_to_hz("A2")),
    SineOscillator(librosa.note_to_hz("A2") + 3),
    TriangleOscillator(librosa.note_to_hz("A4"), amp=0.6),
    TriangleOscillator(librosa.note_to_hz("E5"), amp=0.8),
)
wav = get_val(iter(osc), 44100 * dur)

osc2 = WaveAdder(
    SineOscillator(librosa.note_to_hz("A2")),
    SineOscillator(librosa.note_to_hz("A2") + 3),
    TriangleOscillator(librosa.note_to_hz("C5"), amp=0.8),
    TriangleOscillator(librosa.note_to_hz("F5"), amp=0.6),
)
wav2 = get_val(iter(osc2), 44100 * dur)


wave_to_file(wav, wav2, fname="a_min6.wav")

dur = 10
s1 = ["C4", "E4", "G4", "B4"] * dur
l1 = [0.25, 0.25, 0.25, 0.25] * dur

s2 = ["C3", "E3", "G3"] * dur
l2 = [0.333334, 0.333334, 0.333334] * dur

s3 = ["C2", "G2"] * dur
l3 = [0.5, 0.5] * dur

wavl = (
    np.array(get_seq(TriangleOscillator(amp=0.8), notes=s1, note_lens=l1))
    + np.array(get_seq(SineOscillator(), notes=s2, note_lens=l2))
    + np.array(get_seq(TriangleOscillator(amp=0.4), notes=s3, note_lens=l3))
)

wavr = (
    np.array(get_seq(TriangleOscillator(amp=0.8), notes=s1[::-1], note_lens=l1))
    + np.array(get_seq(SineOscillator(), notes=s2[::-1], note_lens=l2))
    + np.array(get_seq(TriangleOscillator(amp=0.4), notes=s3[::-1], note_lens=l3))
)

wave_to_file(wavl, wavr, fname="c_maj7.wav")
