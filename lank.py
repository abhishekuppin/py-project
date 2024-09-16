import webbrowser
import pyttsx3
import speech_recognition as sr

class Lank:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_and_respond(self):
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            print("Catching up...")
            user_input = self.recognize_audio(audio)
            print("You:", user_input)
            if user_input.lower() == 'exit':
                return "Goodbye!"
            response = self.generate_response(user_input.lower())
            print("LANK:", response)
            self.speak(response)
            return response
        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            self.speak("Sorry, there was an error processing your request.")
        except Exception:
            self.speak("An error occurred.")
        return ""

    def recognize_audio(self, audio):
        return self.recognizer.recognize_google(audio, language='en-IN')

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    @staticmethod
    def generate_response(user_input):
        if any(greeting in user_input for greeting in ['hello', 'hi', 'namaste',]):
            return "Hello! How can I assist you?"
        elif "youtube" in user_input:
            webbrowser.open("https://www.youtube.com/")
            return "Opening YouTube."
        elif "google" in user_input:
            webbrowser.open("https://www.google.com/")
            return "Opening Google."
        elif "wikipedia" in user_input:
            webbrowser.open("https://www.wikipedia.org/")
            return "Opening Wikipedia."
        elif "exit" in user_input:
            return "Goodbye!"
        else:
            return "I'm sorry, I didn't understand that."

lank = Lank()

while True:
    response = lank.listen_and_respond()
    if response == "Goodbye!":
        print("See You Later,Have a Good Time!")
        break
