import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Helps reduce background noise
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return ""
    except sr.RequestError:
        print("Network error. Please check your internet connection.")
        return ""

def main():
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How are you?")
        elif "your name" in command:
            speak("I am Jarvis, your voice assistant.")
        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif command != "":
            speak("You said " + command)

if __name__ == "__main__":
    main()
