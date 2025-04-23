# wake_word.py

import pvporcupine
import pyaudio
import struct

def detect_nyx_wake_word(access_key, ppn_path="wake_words/hey-nyx_en_windows_v3_0_0.ppn"):
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=[ppn_path]
    )

    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🔎 Listening for 'Nyx'...")

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            if porcupine.process(pcm) >= 0:
                print("🗣 'Nyx' wake word detected!")
                break
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()
