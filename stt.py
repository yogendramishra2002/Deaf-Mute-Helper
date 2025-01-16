import speech_recognition as sr

def convert_speech_to_text():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Open the microphone and start recording
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    try:
        # Use Google Speech Recognition to convert speech to text
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#convert_speech_to_text()
