# Hand Gesture Controlled Operating system

This Python script utilizes computer vision and speech recognition modules to create a hand gesture controlled voice assistant. The script allows users to perform various actions based on hand gestures detected through a webcam, and interact with the voice assistant through voice commands.

## Dependencies

- Python 3.x
- OpenCV (`cv2`)
- `cvzone` module (for Hand Tracking)
- `subprocess` module (for opening applications)
- `speech_recognition` module (for voice recognition)
- `pyttsx3` module (for text-to-speech conversion)
- `webbrowser` module (for opening URLs)

## How It Works

1. **Hand Detection**: The script uses OpenCV and the `cvzone` module to detect and track the user's hand in real-time using the webcam.

2. **Gesture Recognition**: It analyzes the hand gestures to recognize specific finger configurations. Each gesture corresponds to a particular action.

3. **Actions Supported**:
    - Five fingers up: Locks the computer (`shutdown /l /t 0`)
    - One finger up: Opens Google Chrome
    - Two fingers up: Opens Notepad
    - Three fingers up: Opens Calculator (`calc.exe`)
    - Four fingers up: Activates the voice assistant for further interaction

4. **Voice Assistant Interaction**: Upon recognizing the voice assistant gesture (four fingers up), the script initiates a conversation with the user through text-to-speech and speech recognition.
    - The assistant greets the user and awaits their command.
    - It listens to the user's voice input and performs a Google search based on the query.
    - The search results are displayed in Google Chrome, and the assistant bids farewell.

## How to Use

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Run the script using `python hand_gesture_voice_assistant.py`.
3. Perform hand gestures in front of the webcam to interact with the assistant.

## Note

- Ensure that the computer has a webcam connected and properly configured.
- Adjust the hand detection parameters and gestures as needed for optimal performance.
- Make sure to provide the necessary permissions for microphone access to enable voice recognition.

