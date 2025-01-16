import pyttsx3

def convert_text_to_speech(text):
    # Initialize the Text-to-Speech engine
    engine = pyttsx3.init()

    # Convert the text to speech
    engine.say(text)

    # Play the speech message
    engine.runAndWait()

if __name__ == "__main__":
    
    convert_text_to_speech("Hello, how are you?")