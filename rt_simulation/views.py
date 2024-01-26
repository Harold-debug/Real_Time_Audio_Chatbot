import os
import uuid
from transformers import Conversation, pipeline
import speech_recognition as sr
from django.shortcuts import render
from django.http import JsonResponse
from gtts import gTTS
from aiclinic_simulation import settings
from aiclinic_simulation.settings import MEDIA_ROOT

# Initialize the conversational pipeline with both model and tokenizer
conversational_pipeline = pipeline("conversational", "facebook/blenderbot-400M-distill")
print(conversational_pipeline.model.config)
# Initialize the bot conversation only once
bot_conversation = Conversation()
i = 0

def speech_recognition_view(request):
    global bot_conversation  # Use the global bot_conversation variable
    global i

    # Check if the request method is POST
    if request.method == 'POST':
        # Initialize the speech recognizer
        recognizer = sr.Recognizer()
        try:
            # Use a microphone as the audio source
            with sr.Microphone() as mic:
                # Adjust the recognizer sensitivity to ambient noise and record audio from the microphone
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.record(mic, duration=4)
                # Transcribe the speech to text
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print("speech text: " + text)

                # Append user input to the conversation
                bot_conversation.add_user_input(text)

                # Use the conversational pipeline
                response_dict = conversational_pipeline(bot_conversation, min_length=10)
                print("Response Dict:", response_dict)

                # Check if 'generated_responses' is present in the response_dict
                if bot_conversation.generated_responses:
                    # Retrieve the bot's response
                    response_text = bot_conversation.generated_responses[i]
                    i += 1

                    # Convert text to speech
                    tts = gTTS(text=response_text, lang='en')
                    audio_filename = os.path.join(MEDIA_ROOT, f'{uuid.uuid4()}.mp3')
                    tts.save(audio_filename)

                    # Return the response text in a JSON response
                    audio_url = os.path.join(settings.MEDIA_URL, os.path.basename(audio_filename))
                    return JsonResponse({'text': response_text, 'audio_path': audio_url})

                else:
                    # Handle the case where 'generated_responses' is not present
                    return JsonResponse({'text': 'No generated responses found'})

        except sr.UnknownValueError:
            # Handle exception if no speech was detected
            return JsonResponse({'text': 'No speech detected'})
        except Exception as e:
            print(e)
            # Handle other exceptions
            return JsonResponse({'text': f'Error: {e}'})

    # Render the index.html template if the request method is not POST
    return render(request, 'index.html')
