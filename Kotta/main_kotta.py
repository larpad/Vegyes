import os
from music21 import converter, instrument, note, chord, stream
from midi2audio import FluidSynth
from gtts import gTTS
from pydub import AudioSegment

def generate_music_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            file_path = os.path.join(directory, filename)
            base_name = os.path.splitext(filename)[0]

            # Convert MusicXML to MIDI
            score = converter.parse(file_path)
            midi_file = os.path.join(directory, f"{base_name}.mid")
            score.write('midi', fp=midi_file)

            # # Convert MIDI to MP3
            # fs = FluidSynth()
            # mp3_file = os.path.join(directory, f"{base_name}.mp3")
            # fs.midi_to_audio(midi_file, mp3_file)

            # # Generate vocal track using gTTS
            # vocal_text = extract_lyrics(score)
            # tts = gTTS(text=vocal_text, lang='hu')
            # vocal_file = os.path.join(directory, f"{base_name}_vocal.mp3")
            # tts.save(vocal_file)

            # # Combine instrumental and vocal tracks
            # instrumental = AudioSegment.from_mp3(mp3_file)
            # vocal = AudioSegment.from_mp3(vocal_file)
            # combined = instrumental.overlay(vocal)
            # combined.export(mp3_file, format="mp3")

def extract_lyrics(score):
    lyrics = []
    for element in score.flat.notes:
        if isinstance(element, note.Note) and element.lyric:
            lyrics.append(element.lyric)
        elif isinstance(element, chord.Chord):
            for n in element.notes:
                if n.lyric:
                    lyrics.append(n.lyric)
    return " ".join(lyrics)

# Example usage
directory = r"F:\DEVEL\DATA\Kotta"
generate_music_files(directory)
