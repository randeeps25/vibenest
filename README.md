# VibeNest 🎧

**VibeNest** is a beginner-friendly Flask web app that turns a short mood description into a personalized mini music mix.

Instead of using a paid AI service, VibeNest uses simple Python keyword scoring to classify text into one of six moods:

- Happy
- Calm
- Sad
- Stressed
- Motivated
- Hopeful

It then recommends five songs from a small built-in catalog, optionally giving priority to the user's preferred genre. Each result includes Spotify and YouTube search links.

## Why this is a good student project

- Uses Python in a real website
- Easy enough to explain in an interview
- No paid API or API key required
- Includes text processing, recommendation logic, Flask, HTML and CSS
- Easy to extend later with a real ML emotion classifier or Spotify API
- Can be hosted publicly on Render

## Project structure

```text
VibeNest/
├── app.py
├── requirements.txt
├── render.yaml
├── README.md
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Run it on your computer

### 1. Open a terminal in the project folder

```bash
cd VibeNest
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the packages

```bash
pip install -r requirements.txt
```

### 4. Start the website

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Deploy on Render

1. Create a GitHub repository, for example `vibenest`.
2. Upload all files from this folder to the repository.
3. Sign in to Render.
4. Choose **New → Web Service**.
5. Connect your GitHub repository.
6. Choose the **Free** instance type.
7. Use:

```text
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

8. Deploy.

Render will provide a public `onrender.com` URL.

> Note: Render's free web services can go to sleep after a period of inactivity, so the first visit after inactivity may take longer to load.

## How the mood detection works

The function `detect_mood()` converts the user's text to lowercase and checks it against lists of mood-related keywords.

Example:

```text
"I am stressed about finals but hopeful for summer"
```

Possible keyword matches:

```text
stressed → stressed, finals
hopeful  → hopeful
```

The mood with the highest score wins. If there is no match, VibeNest chooses a calm mix.

This is intentionally simple. It is a **rule-based text classifier**, not a trained AI model.

## Easy upgrades for later

Once the basic version works, you can add:

1. A Hugging Face sentiment/emotion model
2. Spotify API integration
3. User accounts and saved mixes
4. A "day/night" preference
5. More songs and genres
6. A mood history chart
7. An image-based mood feature

## Resume / LinkedIn description

**VibeNest — Mood-Based Music Recommender**

Built a Flask web app that analyzes user-written mood descriptions with a lightweight rule-based text classifier and generates personalized five-song recommendations across six mood categories. Added genre-aware recommendation logic, responsive UI, and direct Spotify/YouTube discovery links, with deployment designed for Render's free web hosting.

## Important

VibeNest does not claim to diagnose mental health or accurately infer a person's emotional state. It is an entertainment/music recommendation project.
