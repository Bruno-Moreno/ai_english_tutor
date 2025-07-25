import pyaudio
import wave
import threading


def recorder_text(text):
    return f'\n\033[32m{text}\033[0m'

def wait_for_enter(stop_flag):
    input(recorder_text("Press Enter to stop recording..."))
    stop_flag.append(True)


class Recorder:
    def __init__(self, audio_name: str):
        self.audio_name = audio_name
        self.audio_path = "audio"
        self.audio_file = f"{self.audio_path}/{self.audio_name}"
        self.chunk = 4096
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100


    def record(self):
        print(recorder_text(f"Recording to {self.audio_file}..."))
        input(recorder_text("Press Enter to start recording..."))

        p = pyaudio.PyAudio()

        stream = p.open(format=self.format,
                        channels=self.channels,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=self.chunk)

        frames = []
        stop_flag = []
        t = threading.Thread(target=wait_for_enter, args=(stop_flag,))
        t.start()

        while not stop_flag:
            try:
                data = stream.read(self.chunk, exception_on_overflow=False)
                frames.append(data)
            except Exception as e:
                print(f"Error: {e}")
                break

        stream.stop_stream()
        stream.close()
        p.terminate()
        
        return p, frames

    def save(self, p, frames):
        
        wf = wave.open(self.audio_file, 'wb')  
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        print(recorder_text(f"Recording stopped and saved to {self.audio_file}"))