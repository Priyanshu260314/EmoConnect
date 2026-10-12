
from flask import Flask, render_template, request
from feeling_model import model
import re

app = Flask(__name__)

# --------- EMOTION REPLY ---------

def get_reply(emotion):
    replies = {
        "Romantic": "Your words carry a little romance. Keep spreading the love! 💌",
        "Happy": "Your words bring sunshine! Keep smiling. 💖",
        "Sad": "Every feeling matters. Be gentle with your heart. 🌷",
        "Neutral": "Thank you for sharing your thoughts. 🤍",
        "Friendly": "Your message carries warmth and friendship! 💕"
    }

    return replies.get(
        emotion,
        "Thank you for sharing your message. 💗"
    )

# --------- TEXT PROCESSING ---------

def tokenize(text):
    return set(re.findall(r"\b[a-z]+\b", text.lower()))

# --------- HOME / EMOTION ANALYZER ---------

@app.route("/", methods=["GET", "POST"])
def home():
    emotion = None
    response = None
    message = ""

    if request.method == "POST":
        message = request.form.get("text", "").strip()

        if message:
            emotion = model.predict(message)
            response = get_reply(emotion)

    return render_template(
        "index.html",
        emotion=emotion,
        response=response,
        message=message
    )
# --------- LOVE COMPATIBILITY PAGE ---------

@app.route("/similarity", methods=["GET", "POST"])
def similarity():
    score = None
    emotion1 = None
    emotion2 = None
    common_words = "No shared words"
    text1 = ""
    text2 = ""

    # GET: Open the Compatibility page
    # POST: Compare the two messages
    if request.method == "POST":
        text1 = request.form.get("text1", "").strip()
        text2 = request.form.get("text2", "").strip()

        if text1 and text2:
            words1 = tokenize(text1)
            words2 = tokenize(text2)

            union = words1 | words2
            intersection = words1 & words2

            # Jaccard similarity
            score = (
                round(len(intersection) / len(union) * 100)
                if union else 0
            )

            common_words = (
                ", ".join(sorted(intersection))
                if intersection else "No shared words"
            )

            emotion1 = model.predict(text1)
            emotion2 = model.predict(text2)

    return render_template(
        "compatibility.html",
        similarity=score,
        score=score,
        emotion1=emotion1,
        emotion2=emotion2,
        common_words=common_words,
        text1=text1,
        text2=text2
    )

# --------- LOVE LETTER GENERATOR PAGE ---------

@app.route("/letter", methods=["GET", "POST"])
def letter():

    # GET: Open the Love Letter page
    if request.method == "GET":
        return render_template("letter.html")

    # POST: Generate the letter
    mood = request.form.get("mood", "Romantic")
    relationship = request.form.get("relationship", "Partner")
    tone = request.form.get("tone", "Sweet")
    name = request.form.get("recipient", "").strip()

    # Validate submitted choices
    if mood not in ["Romantic", "Happy", "Grateful", "Missing"]:
        mood = "Romantic"

    if relationship not in [
        "Partner", "Crush", "Spouse", "Long-distance"
    ]:
        relationship = "Partner"

    if tone not in ["Sweet", "Cute", "Deep", "Poetic"]:
        tone = "Sweet"

    recipient = name if name else "My Dear"

    openings = {
        "Romantic":
            "You have a special place in my heart that no one else could ever fill.",

        "Happy":
            "Every moment with you gives me another reason to smile.",

        "Grateful":
            "I feel truly grateful to have someone as special as you in my life.",

        "Missing":
            "Even when you are far away, you remain close to my heart."
 
    }

    relationship_lines = {
        "Partner":
            "Thank you for being my partner, my comfort, and my favorite person.",

        "Crush":
            "Whenever I think of you, a little smile finds its way onto my face.",

        "Spouse":
            "I would choose you again and again, through every chapter of life.",

        "Long-distance":
            "Distance may separate our places, but it cannot decide the depth of my feelings."
    }

    tone_endings = {
        "Sweet":
            "I hope this little letter reminds you how much you mean to me. With love, always. 💗",

        "Cute":
            "You are my favorite notification, my happiest thought, and my biggest smile. Sending you a thousand hugs! 🧸",

        "Deep":
            "Whatever tomorrow brings, I hope we keep choosing kindness, honesty, and each other. You mean more than words can explain. ❤️",

        "Poetic":
            "If my heart could write the stars, every one would spell your name across the night sky. 🌹"

    }

    generated_letter = (
        f"Dear {recipient},\n\n"
        f"{openings[mood]}\n\n"
        f"{relationship_lines[relationship]}\n\n"
        f"{tone_endings[tone]}"
    )

    return render_template(
        "letter.html",
        letter=generated_letter,
        generated_letter=generated_letter,
        selected_mood=mood,
        selected_relationship=relationship,
        selected_tone=tone,
        recipient=name
    )
# --------- RUN APPLICATION ---------

if __name__ == "__main__":
    app.run(debug=True, port=8000)
