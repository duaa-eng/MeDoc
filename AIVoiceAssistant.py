import openai
import pyttsx3
import speech_recognition as sr
from api_secrets import API_KEY

def initialize_text_to_speech():
    return pyttsx3.init()

def initialize_speech_recognition():
    mic_index = 1
    mic = sr.Microphone(device_index=mic_index)
    print(sr.Microphone.list_microphone_names())
    return sr.Recognizer(), mic

def listen_to_user(recognizer, microphone):
    with microphone as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
    print("No longer listening.\n")
    return audio

def transcribe_audio(recognizer, audio):
    try:
        return recognizer.recognize_google(audio)
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    return None

def contains_specific_words(text, words_to_check):
    """
    Check if any of the specified words are present in the given text.
    """
    return any(word in text.lower() for word in words_to_check)


def generate_openai_response(prompt):
    try:
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)
        return response["choices"][0]["text"].replace("\n", "")
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def main():
    openai.api_key = API_KEY
    engine = initialize_text_to_speech()
    recognizer, microphone = initialize_speech_recognition()

    conversation = ""
    user_name = "You"
    bot_name = "Hamada"

    while True:
        audio = listen_to_user(recognizer, microphone)
        user_input = transcribe_audio(recognizer, audio)

        if user_input:
            prompt = f"{user_name}: {user_input}\n{bot_name}: "
            conversation += prompt
            
            # Check if certain words are present in the user's input
            specific_words_to_check = ['book appointment', 'show schedule', 'bla bla']
            if contains_specific_words(user_input, specific_words_to_check):
                # should be directed to specific flows
                print("User mentioned specific words!")
                
            # Check if the word "bye" is mentioned in the user's input
            if contains_specific_words(user_input, ['bye']):
                print("User said 'bye'. Exiting...")
                break

            response_str = generate_openai_response(conversation)
            if response_str:
                conversation += response_str + "\n"
                print(response_str)

                engine.say(response_str)
                engine.runAndWait()

if __name__ == "__main__":
    main()
