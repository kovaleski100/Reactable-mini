from pydub import AudioSegment
from pydub import generators

sound1 = generators.Sine(440).to_audio_segment(duration=10000)
sound1 = sound1.overlay(generators.Sine(240).to_audio_segment(duration=10000))
sound1.export("result.wav", format='wav')
