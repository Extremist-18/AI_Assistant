# NOVA – Next-gen Operating Virtual Assistant

**NOVA** (Next-gen Operating Virtual Assistant) is a desktop-based AI assistant powered by voice recognition, intelligent automation, and a modern PyQt6 interface. It enables hands-free control over tasks such as email management, calendar scheduling, music playback, weather updates, web search, and more.

---

## 🎬 Demo

Watch a live demo of NOVA in action on YouTube:

[![Watch the Demo](https://img.youtube.com/vi/c39VS2pI5Mo/0.jpg)](https://www.youtube.com/watch?v=c39VS2pI5Mo)

---

## Key Features

### Voice-Enabled Interaction
- Natural and intuitive hands-free control using voice commands.
- Real-time speech transcription using Google's speech recognition engine.

### Smart Assistant Capabilities
- Provides current time and date on request.
- Retrieves information from Wikipedia for people, places, or topics.
- Performs Google searches and returns summarized results.

### Productivity Tools
- Compose and send emails using voice via the Gmail API.
- Integrate with Google Calendar to create and schedule events.
- Record and manage voice notes and reminders.
- Makes important notes just with your voice commands.

### Media & Web Integration
- Play any song using YouTube voice search.
- Capture screenshots with voice-directed naming and location.
- Deliver current news headlines based on user-defined limits.
- Report local weather conditions and temperature updates.

### Custom Voice Output
- Option to use high-quality voice synthesis via ElevenLabs API.
- Fallback to offline TTS using pyttsx3 when no API is available.
- Supports personalized voice responses (currently using a predefined API key and voice ID).

---

## Graphical User Interface (GUI)

- Developed with PyQt6 for a responsive and modern desktop experience.
- Displays real-time date, time, and weather in a clean HUD-style layout.
- Features an animated assistant panel for visual engagement.
- Styled with a dark theme, neon highlights, and soft shadows for a polished and futuristic aesthetic.

---

## Technology Stack

| Component            | Description                                  |
|----------------------|----------------------------------------------|
| Python               | Core programming language                    |
| PyQt6                | GUI framework                                |
| SpeechRecognition    | Voice input processing                       |
| pyttsx3              | Offline text-to-speech engine                |
| ElevenLabs API       | Cloud-based custom voice synthesis           |
| Google APIs          | Gmail, Calendar, and Search integration      |
| OpenWeatherMap API   | Weather data provider                        |
| Wikipedia API        | Access to encyclopedic information           |

---
