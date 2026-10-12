
import re
import math
from collections import Counter, defaultdict


class LoveEmotionModel:
    def __init__(self):
        self.word_counts = defaultdict(Counter)
        self.class_counts = Counter()
        self.vocabulary = set()
        self.total_samples = 0

    def tokenize(self, text):
        """Basic NLP text preprocessing."""
        text = text.lower()
        return re.findall(r"[a-z]+", text)

    def train(self, texts, labels):
        """Train Naive Bayes from scratch."""
        self.total_samples = len(texts)

        for text, label in zip(texts, labels):
            words = self.tokenize(text)

            self.class_counts[label] += 1

            for word in words:
                self.word_counts[label][word] += 1
                self.vocabulary.add(word)

    def predict(self, text):
        """Predict emotion using log probabilities."""
        words = self.tokenize(text)

        if not words:
            return "Neutral"

        scores = {}

        for label, count in self.class_counts.items():
            score = math.log(
                count / self.total_samples
            )

            total_words = sum(
                self.word_counts[label].values()
            )

            vocab_size = len(self.vocabulary)

            for word in words:
                word_count = self.word_counts[label][word]

                # Laplace smoothing
                probability = (
                    word_count + 1
                ) / (
                    total_words + vocab_size
                )

                score += math.log(probability)

            scores[label] = score

        return max(scores, key=scores.get)


# Small educational training dataset
training_texts = [
    "I love you so much",
    "you are my sweetheart",
    "my darling you are beautiful",
    "I adore you forever",
    "you make my heart happy",
    "I am so excited and joyful",
    "today is a wonderful day",
    "I feel amazing and happy",
    "I feel sad and lonely",
    "I miss you so much",
    "my heart is broken",
    "I feel hurt and upset",
    "the package arrived today",
    "this is an ordinary day",
    "I received your message",
    "the meeting is tomorrow",
]

training_labels = [
    "Romantic",
    "Romantic",
    "Romantic",
    "Romantic",
    "Happy",
    "Happy",
    "Happy",
    "Happy",
    "Sad",
    "Sad",
    "Sad",
    "Sad",
    "Neutral",
    "Neutral",
    "Neutral",
    "Neutral",
]


# Train the model
model = LoveEmotionModel()
model.train(training_texts, training_labels)


# Test the model
if __name__ == "__main__":
    while True:
        message = input(
            "\nEnter a message (or type exit): "
        )

        if message.lower().strip() == "exit":
            break

        prediction = model.predict(message)

        print("Predicted emotion:", prediction)
