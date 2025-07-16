from src.recorder import Recorder
from src.listener import Listener


if __name__ == "__main__":

    audio_name = "test.wav"
    model_name = "base.en" 

    if input("Record audio? (y/n): ") == "y":
        recorder = Recorder(audio_name)
        p, frames = recorder.record()
        recorder.save(p, frames)

    listener = Listener(model_name, audio_name)
    listener.transcribe()