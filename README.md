# 🎧 VibeNest

**VibeNest** is a mood-based music recommendation website built with Python and Flask.

Describe how you're feeling, choose your preferred music style, and VibeNest will detect your mood and create a personalized 5-song mix.

## 🚀 Live Demo

### [Try VibeNest →](https://vibenest-v9yk.onrender.com/)

## Features

* Detects 6 different moods from text
* Generates personalized song recommendations
* Supports different music preferences
* Direct Spotify and YouTube links
* Works on desktop and mobile
* Free to use — no account required

## How It Works

VibeNest uses a simple Python keyword-scoring system to classify text into one of six moods:

**Happy · Calm · Sad · Stressed · Motivated · Hopeful**

It then combines the detected mood with the user's music preference to recommend five songs.

## Built With

**Python · Flask · HTML · CSS · GitHub · Render**

## Run Locally

```bash id="87j89y"
git clone https://github.com/randeeps25/vibenest.git
cd vibenest
pip install -r requirements.txt
python3 app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

Built as a personal project to explore Python web development, text classification, and recommendation systems.
