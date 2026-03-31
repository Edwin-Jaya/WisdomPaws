# Wisdom Paws 🐾: Gesture-Controlled Uncensored AI Virtual Pet (LLM · Mediapipe · Pygame)

An interactive uncensored AI-powered virtual pet that responds to your **open palm gestures** and returns **contextual wisdom**. Built using Mediapipe for real-time hand tracking and LLMs for generating meaningful responses—blending computer vision, human interaction, and generative AI into a playful emotional experience.

**Pet the AI → receive wisdom back.**

---

# Table of contents
1. Highlights  
2. Demo  
3. Tech stack  
4. Repository layout  
5. Quick start (local)  
6. Flow and Architecture  
7. Troubleshooting & gotchas  
8. Contact  
9. License  

---

# Highlights
- Real-time **hand gesture recognition** via Mediapipe Hands  
- Open palm detection to trigger interaction with the pet  
- **LLM-powered responses** that generate contextual “wisdom”  
- Smooth integration between CV input → AI reasoning → UI feedback  
- Interactive virtual pet built with Pygame  
- Clean modular pipeline for gesture-to-response systems  

---

# Demo
As seen on TikTok: [Click Here](https://www.tiktok.com/@edwinjaya.py/video/7557233096576355591)  

---

# Tech Stack
- Python 3.9  
- Mediapipe (Hand Tracking)  
- OpenCV  
- Pygame  
- Wizuna Vicuna 7b
- NumPy   

**Tip:** Open your palm clearly and steadily—the calmer your gesture, the wiser the response 🐾  

---

# Repository layout
```
.
├── Assets/
│   ├── Idle/
│   │   └── Idle.png
│   ├── walk/
│   │   ├── kucing ewing1.png
│   │   ├── kucing ewing2.png
│   │   ├── kucing ewing3.png
│   │   └── kucing ewing4.png
│   ├── background-1.png
│   ├── background.png
│   └── Idle.png
│
├── Model/
│   └── gesture_recognizer.task
│
├── app.py
├── controller.py
├── game.py
├── llm.py
├── README.md
```
---

# Quickstart (Local)

## 1️⃣ Create and activate environment
<code>conda create -n wisdompaws python=3.9
conda activate wisdompaws
</code>

## 2️⃣ Install dependencies  
<code>pip install -r requirements.txt</code>

## 3️⃣ Run the app  
<code>python main.py</code>

---

# Flow and Architecture
1. **Camera Input** → Capture real-time video via OpenCV  
2. **Gesture Detection** → Mediapipe detects hand landmarks  
3. **Gesture Classification** → Identify open palm gesture  
4. **Trigger Event** → Send interaction signal to system  
5. **LLM Processing** → Generate contextual “wisdom”  
6. **Pet Response** → Display message + animation via Pygame  

---

# Troubleshooting & Gotchas
- **Gesture not detected?**  
  Ensure good lighting and keep your palm fully visible to the camera.  

- **High latency in responses?**  
  LLM calls may take time—consider caching or using a faster/local model.  

- **Webcam not working?**  
  Close other apps that might be using your camera.  

- **Pet not responding?**  
  Check API keys or LLM connection inside `llm.py`.  

---

# Contact
- LinkedIn: [Click Here](https://www.linkedin.com/in/edwin-jaya/)  
- Email: [Click Here](mailto:edwinlionaj@gmail.com)  
- TikTok: [Click Here](https://www.tiktok.com/@edwinjaya.py)  
- Portfolio: [Click Here](https://www.edwinlionajaya.tech/)  

---

# License
MIT License — feel free to use, modify, and build on this project.
