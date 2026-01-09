import pvporcupine
import pyaudio
import struct
import os

def wait_for_wake_word():
    access_key = os.getenv("PICOVOICE_ACCESS_KEY")

    if not access_key:
        raise RuntimeError(
            "Picovoice access key not found. "
            "Set PICOVOICE_ACCESS_KEY environment variable."
        )

    porcupine = pvporcupine.create(
        access_key=access_key,
        keywords=["jarvis"]
    )

    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🛑 Waiting for wake word: 'Hey Jarvis'")

    try:
        while True:
            pcm = stream.read(
                porcupine.frame_length,
                exception_on_overflow=False
            )
            pcm = struct.unpack_from(
                "h" * porcupine.frame_length,
                pcm
            )

            if porcupine.process(pcm) >= 0:
                print("✅ Wake word detected")
                break

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()
