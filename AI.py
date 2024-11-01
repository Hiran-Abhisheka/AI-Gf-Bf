import speech_recognition as sr
import pyttsx3
from groq import Groq
import customtkinter as ctk
import tkinter as tk  # Import tkinter for StringVar
import threading  # Import threading to run listening in a separate thread
import time  # Import time for sleep function

# Your Groq API key
GROQ_API_KEY = ""

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)

# Initialize the speech recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Variable to store the selected voice
selected_voice = 'male'  # Default value

def set_voice(gender='male'):
    """Set the voice for the TTS engine."""
    global selected_voice
    selected_voice = gender  # Update the selected voice
    voices = tts_engine.getProperty('voices')
    if gender == 'male':
        tts_engine.setProperty('voice', voices[0].id)  # Typically male voice
    else:
        tts_engine.setProperty('voice', voices[1].id)  # Typically female voice

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def generate_response(prompt):
    """Generate a response using the Groq API."""
    completion = client.chat.completions.create(
        model="llama3-70b-8192",  # Specify the model you want to use
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    return response.strip()

def animate_response_label(text):
    """Animate the response label by changing its color."""
    response_label.configure(text=text, text_color="#00ffcc")  # Change to a bright color
    app.update()  # Update the UI
    time.sleep(0.5)  # Pause for half a second
    response_label.configure(text=text, text_color="#ffffff")  # Change back to white

def listen_and_respond():
    """Continuously listen for audio input and respond."""
    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... (Press 'Stop' to end)")

        while True:
            audio = recognizer.listen(source)

            try:
                # Recognize speech using Google Web Speech API
                transcription = recognizer.recognize_google(audio)
                print(f"Transcription: {transcription}")
                
                # Send the transcription to the AI model for a response
                response = generate_response(transcription)
                print(f"Generated Response: {response}")
                speak(response)  # Speak the AI's response
                animate_response_label(response)  # Animate the response label

            except sr.UnknownValueError:
                response_label.configure(text="Could not understand audio. Please try again.")
            except sr.RequestError as e:
                response_label.configure(text=f"Could not request results; {e}")

def start_listening():
    """Start the listening thread and prompt AI based on selected voice."""
    # Prompt the AI based on the selected voice
    
    # Start the listening thread
    listening_thread = threading.Thread(target=listen_and_respond)
    listening_thread.daemon = True  # Allow thread to exit when the main program exits
    listening_thread.start()
    if selected_voice == 'male':
        initial_response = generate_response("Can you act like my boyfriend?")
    else:
        initial_response = generate_response("Can you act like my girlfriend?")
    
    speak(initial_response)  # Speak the AI's initial response


# Create the main application window
app = ctk.CTk()
app.title("Virtual Girlfriend/Boyfriend")
app.geometry("800x400")
app.configure(bg="#1e1e2f")  # Dark background for a futuristic look

# Create a header label with a futuristic font
header_label = ctk.CTkLabel(app, text="Virtual Girlfriend/Boyfriend", font=("Helvetica", 24, "bold"), text_color="#00ffcc")
header_label.pack(pady=(20, 10))

# Create a label to display responses
response_label = ctk.CTkLabel(app, text="Press 'Start' to begin listening...", wraplength=300, text_color="#ffffff", font=("Helvetica", 14))
response_label.pack(pady=20)

# Create a button to start listening with rounded corners
start_button = ctk.CTkButton(app, text="Start", command=start_listening, fg_color="#00ffcc", hover_color="#00cc99", text_color="#000000", width=200)
start_button.pack(pady=(10, 5))

# Create a button to stop listening with rounded corners
stop_button = ctk.CTkButton(app, text="Stop", command=app.quit, fg_color="#ff4d4d", hover_color="#cc0000", text_color="#000000", width=200)
stop_button.pack(pady=(5, 20))

# Create radio buttons to select voice gender
voice_frame = ctk.CTkFrame(app, fg_color="#1e1e2f")
voice_frame.pack(pady=10)

voice_label = ctk.CTkLabel(voice_frame, text="Select Voice:", text_color="#ffffff", font=("Helvetica", 14))
voice_label.pack(side='left')

voice_var = tk.StringVar(value='male')  # Default value
male_voice_button = ctk.CTkRadioButton(voice_frame, text="Male", variable=voice_var, value='male', command=lambda: set_voice('male'), text_color="#ffffff", hover_color="#00cc99")
male_voice_button.pack(side='left')

female_voice_button = ctk.CTkRadioButton(voice_frame, text="Female", variable=voice_var, value='female', command=lambda: set_voice('female'), text_color="#ffffff", hover_color="#00cc99")
female_voice_button.pack(side='left')

# Start the application
app.mainloop()
