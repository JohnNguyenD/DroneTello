#!/usr/bin/python3
from vosk import Model, KaldiRecognizer
import pyaudio
import time
import Tello

model = Model("/home/john/Downloads/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()


listening = False

def get_command_input():
    listening = True
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    while listening:
        stream.start_stream()
        try:          
            data = stream.read(4096)

            if recognizer.AcceptWaveform(data):
                res = recognizer.Result()
                response = res[14:-3]
                listening = False
                stream.close()
                return response
        except OSError:
            pass
                
def analyze_command(command):
    try:
        if __name__ == "__main__":  
            tello = Tello.Controller()
            if command == "take off":
                tello.send_command("takeoff")
            elif command == "okay":
                tello.send_command("land")
    except Exception:
        pass

while True:
    print("Wating for command")
    command = get_command_input()
    print(command)
    analyze_command(command)

# if __name__ == "__main__":    
#     tello = Tello.Controller()
#     tello.send_command("command")
#     time.sleep(2)
#     tello.send_command("takeoff")
#     time.sleep(10)
#     tello.send_command("cw 360")
#     time.sleep(7)
#     tello.send_command("land")
#     time.sleep(3)
    
