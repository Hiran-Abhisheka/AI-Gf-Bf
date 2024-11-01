![AI GF/BF](https://ibb.co/qWRTfKX)

# Virtual Girlfriend/Boyfriend

A virtual assistant application that interacts with users as a virtual girlfriend or boyfriend. The application uses speech recognition to understand user input and text-to-speech to respond, creating a conversational experience.

## Features

- **Speech Recognition**: Understands user speech input using Google Web Speech API.
- **Text-to-Speech**: Responds to users with synthesized speech using the `pyttsx3` library.
- **Voice Selection**: Users can choose between a male or female voice for the assistant.
- **AI Interaction**: Generates responses using the Groq API based on user input.

## Requirements

- Python 3.x
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `groq`
  - `customtkinter`
  - `tkinter`
  
You can install the required libraries using pip:

```bash
pip install speech_recognition pyttsx3 groq customtkinter
```


## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/AI-Gf-Bf.git
   cd AI-Gf-Bf
   ```

2. Replace the `GROQ_API_KEY` in the `AI.py` file with your actual Groq API key.

3. Run the application:

   ```bash
   python AI.py
   ```

## Usage

1. Launch the application.
2. Select the desired voice (Male or Female).
3. Click the "Start" button to begin the conversation.
4. Speak to the assistant and receive responses based on your input.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for speech recognition capabilities.
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech functionality.
- [Groq](https://groq.com/) for AI response generation.
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for enhanced UI components.
