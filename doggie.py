import whisper
import sounddevice as sd
import scipy.io.wavfile as wav
import pyautogui
import time

model = whisper.load_model("small") # used multiple ones small is the best 

print("Say something...")
while True:
    audio = sd.rec(5 * 16000, samplerate=16000, channels=1) # record for 5 seconds at 16kHz
    sd.wait() # record finished

    wav.write("test.wav", 16000, audio)# saves file as test.wav

    result = model.transcribe( #whisper turns audio to text using expected prompts
        "test.wav",
        fp16=False,
        language = "en",
        temperature=0, # gives better decoding
        initial_prompt="Hey doggy. Clip the last 30 seconds. Analyze my death. Quit.", # this is prompts it should expect

    )

    print("You said:", result["text"])

    command = result["text"].lower()
    if "doggy" in command or "doggie" in command:
        print("Doggy: I'm listening.")

        audio = sd.rec(5 * 16000, samplerate=16000, channels=1)
        sd.wait()

        wav.write("command.wav", 16000, audio)

        result = model.transcribe(
            "command.wav",
            initial_prompt="Commands include clip the last 30 seconds, analyze my death, and quit."
        )

        command = result["text"].lower()

        print("You said:", command)

        # Process the command
        print("DEBUG - Command received:", repr(command))

        if "clip" in command or "clipping" in command:
            print("Doggy: Saving the last 30 seconds!")
            pyautogui.hotkey("alt", "]")
            print("Doggy: Hotkey sent!")

        elif "analyze" in command or "analyse" in command:
            print("Doggy: Analyzing your death!")

        elif "quit" in command:
            print("Doggy: Shutting down.")
            break

        else:
            print("Doggy: I didn't recognize that command.")