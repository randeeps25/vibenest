from flask import Flask, render_template, request
from urllib.parse import quote_plus
import random

app = Flask(__name__)

MOOD_KEYWORDS = {
    "happy": [
        "happy", "great", "good", "amazing", "excited", "joy", "joyful",
        "fun", "celebrate", "celebrating", "smile", "awesome", "fantastic",
        "love", "loved", "winning", "proud"
    ],
    "calm": [
        "calm", "peaceful", "relaxed", "relax", "chill", "quiet", "cozy",
        "comfortable", "slow", "rest", "resting", "easy", "content"
    ],
    "sad": [
        "sad", "down", "upset", "hurt", "lonely", "cry", "crying",
        "heartbroken", "miss", "missing", "bad", "rough", "empty"
    ],
    "stressed": [
        "stressed", "stress", "anxious", "anxiety", "worried", "overwhelmed",
        "pressure", "deadline", "deadlines", "exam", "exams", "finals",
        "busy", "panic", "nervous", "tired"
    ],
    "motivated": [
        "motivated", "motivation", "focused", "focus", "grind", "gym",
        "workout", "study", "studying", "productive", "determined",
        "goals", "goal", "hustle", "energy"
    ],
    "hopeful": [
        "hopeful", "hope", "better", "future", "fresh", "new", "optimistic",
        "progress", "healing", "ready", "tomorrow", "believe", "dream"
    ],
}

MOOD_INFO = {
    "happy": {
        "emoji": "☀️",
        "tagline": "Bright, upbeat, and ready to move.",
        "message": "Your words sound positive and energetic."
    },
    "calm": {
        "emoji": "🌿",
        "tagline": "Soft sounds for a slower moment.",
        "message": "Your words suggest a relaxed, peaceful vibe."
    },
    "sad": {
        "emoji": "🌧️",
        "tagline": "A little space to feel what you feel.",
        "message": "Your words sound reflective or a little low."
    },
    "stressed": {
        "emoji": "🌙",
        "tagline": "Music to help turn the volume down.",
        "message": "Your words suggest pressure, tiredness, or worry."
    },
    "motivated": {
        "emoji": "⚡",
        "tagline": "Momentum music. Keep going.",
        "message": "Your words sound focused and driven."
    },
    "hopeful": {
        "emoji": "🌅",
        "tagline": "Forward-looking songs with some light in them.",
        "message": "Your words suggest optimism and a fresh-start feeling."
    },
}

# A small local catalog keeps the project free and avoids API keys.
# "genres" are intentionally broad so recommendations stay flexible.
SONGS = {
    "happy": [
        ("Good as Hell", "Lizzo", ["pop"]),
        ("Sunday Best", "Surfaces", ["pop", "indie"]),
        ("Walking on a Dream", "Empire of the Sun", ["indie", "pop"]),
        ("September", "Earth, Wind & Fire", ["rnb", "pop"]),
        ("Levitating", "Dua Lipa", ["pop"]),
        ("Electric Feel", "MGMT", ["indie"]),
        ("I Wanna Dance with Somebody", "Whitney Houston", ["pop", "rnb"]),
        ("Feel It Still", "Portugal. The Man", ["indie", "pop"]),
    ],
    "calm": [
        ("Bloom", "The Paper Kites", ["indie"]),
        ("Best Part", "Daniel Caesar feat. H.E.R.", ["rnb"]),
        ("Sunset Lover", "Petit Biscuit", ["electronic", "indie"]),
        ("Holocene", "Bon Iver", ["indie"]),
        ("Japanese Denim", "Daniel Caesar", ["rnb"]),
        ("Pink + White", "Frank Ocean", ["rnb"]),
        ("Coffee", "beabadoobee", ["indie"]),
        ("Space Song", "Beach House", ["indie"]),
    ],
    "sad": [
        ("The Night We Met", "Lord Huron", ["indie"]),
        ("when the party's over", "Billie Eilish", ["pop"]),
        ("Self Control", "Frank Ocean", ["rnb"]),
        ("Somebody Else", "The 1975", ["indie", "pop"]),
        ("All I Want", "Kodaline", ["indie"]),
        ("Liability", "Lorde", ["pop"]),
        ("Slow Dancing in the Dark", "Joji", ["rnb", "pop"]),
        ("Motion Sickness", "Phoebe Bridgers", ["indie"]),
    ],
    "stressed": [
        ("Weightless", "Marconi Union", ["ambient", "electronic"]),
        ("Intro", "The xx", ["indie"]),
        ("River Flows in You", "Yiruma", ["instrumental"]),
        ("Awake", "Tycho", ["electronic", "ambient"]),
        ("Mystery of Love", "Sufjan Stevens", ["indie"]),
        ("Experience", "Ludovico Einaudi", ["instrumental"]),
        ("A Walk", "Tycho", ["electronic", "ambient"]),
        ("Show Me How", "Men I Trust", ["indie"]),
    ],
    "motivated": [
        ("Stronger", "Kanye West", ["hiphop"]),
        ("Remember the Name", "Fort Minor", ["hiphop"]),
        ("POWER", "Kanye West", ["hiphop"]),
        ("Till I Collapse", "Eminem", ["hiphop"]),
        ("Can't Hold Us", "Macklemore & Ryan Lewis", ["hiphop", "pop"]),
        ("Lose Yourself", "Eminem", ["hiphop"]),
        ("Don't Start Now", "Dua Lipa", ["pop"]),
        ("The Less I Know the Better", "Tame Impala", ["indie"]),
    ],
    "hopeful": [
        ("Dog Days Are Over", "Florence + The Machine", ["indie", "pop"]),
        ("Unwritten", "Natasha Bedingfield", ["pop"]),
        ("Vienna", "Billy Joel", ["pop"]),
        ("Golden", "Harry Styles", ["pop"]),
        ("Good Days", "SZA", ["rnb"]),
        ("Sweet Disposition", "The Temper Trap", ["indie"]),
        ("I Lived", "OneRepublic", ["pop"]),
        ("Daylight", "David Kushner", ["pop"]),
    ],
}

def detect_mood(text):
    cleaned = text.lower()
    scores = {mood: 0 for mood in MOOD_KEYWORDS}
    matched = {mood: [] for mood in MOOD_KEYWORDS}

    for mood, words in MOOD_KEYWORDS.items():
        for word in words:
            if word in cleaned:
                scores[mood] += 1
                matched[mood].append(word)

    best_score = max(scores.values())
    if best_score == 0:
        # Friendly default when no keywords are found.
        return "calm", []

    # If there is a tie, choose the mood whose keyword was found first.
    winners = [mood for mood, score in scores.items() if score == best_score]
    for mood in MOOD_KEYWORDS:
        if mood in winners:
            return mood, matched[mood]

    return "calm", []

def recommend_songs(mood, genre, count=5):
    choices = SONGS[mood][:]
    if genre and genre != "any":
        preferred = [song for song in choices if genre in song[2]]
        other = [song for song in choices if genre not in song[2]]
        random.shuffle(preferred)
        random.shuffle(other)
        choices = preferred + other
    else:
        random.shuffle(choices)

    results = []
    for title, artist, genres in choices[:count]:
        query = quote_plus(f"{title} {artist}")
        results.append({
            "title": title,
            "artist": artist,
            "genres": genres,
            "youtube_url": f"https://www.youtube.com/results?search_query={query}",
            "spotify_url": f"https://open.spotify.com/search/{quote_plus(title + ' ' + artist)}",
        })
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = ""
    genre = "any"

    if request.method == "POST":
        text = request.form.get("mood_text", "").strip()
        genre = request.form.get("genre", "any")

        if text:
            mood, matched_words = detect_mood(text)
            result = {
                "mood": mood,
                "matched_words": matched_words,
                "info": MOOD_INFO[mood],
                "songs": recommend_songs(mood, genre),
            }

    return render_template("index.html", result=result, text=text, genre=genre)

if __name__ == "__main__":
    app.run(debug=True)
