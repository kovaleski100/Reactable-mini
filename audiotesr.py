from pydub import AudioSegment

sound1 = AudioSegment.from_file("1.wav")
sound2 = AudioSegment.from_file("2.wav")

combined = sound1.overlay(sound2)

combined.export("result.wav", format='wav')
