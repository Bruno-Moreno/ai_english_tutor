from src.recorder import Recorder
from src.listener import Listener
from src.analyser import Analyser


def writing_iteraction(analyser, number_of_interactions):
    analyser.generate_response("Hello! what's your name?")
    for _ in range(number_of_interactions):
        analyser.generate_response(input("Response: "))


def speaking_iteraction(recorder, listener, analyser, number_of_interactions):
    analyser.generate_response("Hello! what's your name?")
    for _ in range(number_of_interactions):
        p, frames = recorder.record()
        recorder.save(p, frames)
        response = listener.transcribe()
        print(f"\nResponse: {response}")
        analyser.generate_response(response)


if __name__ == "__main__":
    # tmp_audio_name = "jfk.wav"
    tmp_audio_name = "tmp_audio.wav"
    whisper_model_name = "base.en"
    analyser_model_name = "llama3"
    number_of_interactions = 3

    analyser = Analyser(analyser_model_name)
    listener = Listener(whisper_model_name, tmp_audio_name)
    recorder = Recorder(tmp_audio_name)

    mode = input("Writing or Speaking? (w/s): ")
    if mode.lower() == "w":
        print("Writing Mode Initialized")
        writing_iteraction(analyser, number_of_interactions=number_of_interactions)

    elif mode.lower() == "s":
        print("Speaking Mode Initialized")
        speaking_iteraction(
            recorder, listener, analyser, number_of_interactions=number_of_interactions
        )

    else:
        raise ValueError("w/s must be provided")
