import subprocess
import re


class Listener:
    def __init__(self, model_name: str, audio_name: str):
        self.model_name = model_name
        self.audio_path = "audio"
        self.audio_name = audio_name
        self.audio_file = f"{self.audio_path}/{self.audio_name}"
        self.transcription_path = "transcription"
        self.transcription_file = (
            f"{self.transcription_path}/{self.audio_name.split('.')[0]}.txt"
        )

        self.model_path_dict = {
            "base.en": "models/ggml-base.en.bin",
            "medium.en": "models/ggml-medium.en.bin",
        }
        self.model_path = self.model_path_dict[self.model_name]

    def transcribe(self):
        # print(f"Transcribing {self.audio_name} with {self.model_name}")
        command = [
            "./build/bin/whisper-cli",
            "-m",
            f"{self.model_path}",
            "-f",
            f"../{self.audio_file}",
        ]

        result = subprocess.run(
            command, cwd="whisper.cpp", capture_output=True, text=True
        )

        # Print the output and errors
        if result.stdout:
            text = re.sub(r"\[.*?\]", "", result.stdout)
            text = text.lstrip()
            with open(f"{self.transcription_file}", "w") as f:
                print(text, file=f)
                return text
        else:
            raise ValueError("STDERR:", result.stderr)
