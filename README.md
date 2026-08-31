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


## Important

VibeNest does not claim to diagnose mental health or accurately infer a person's emotional state. It is an entertainment/music recommendation project.
