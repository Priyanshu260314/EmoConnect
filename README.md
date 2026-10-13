# 💗 EmoConnect
### Understand Emotions. Connect Hearts.

EmoConnect is a beginner-friendly, NLP-based web application developed using Python and Flask. It analyzes text, detects emotions using the implemented detection logic, compares two messages by matching their words, and generates personalized love letters.
The project demonstrates basic Natural Language Processing concepts through an interactive web application.

## ✨ Features

- 💖 **Emotion Analyzer:** Analyzes user text and identifies emotions based on the implemented detection logic.
- 💞 **Compatibility Checker:** Compares two messages, matches their words, identifies common words, and calculates a word similarity percentage.
- 💌 **Love Letter Generator:** Generates romantic messages and personalized love letters.
- 🎨 **Interactive User Interface:** Provides a user-friendly interface with a romantic theme.
- ⚡ **Local Execution:** Runs locally on your computer using Flask.

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python
- **Web Framework:** Flask
- **Text Analysis:** Basic NLP and word similarity techniques
- **Version Control:** Git and GitHub

## 🧠 How It Works

### 1. Emotion Analyzer

The user enters a text message, and the application analyzes the text to identify emotions according to its implemented detection logic.

### 2. Compatibility Checker

The user enters two messages. EmoConnect compares the words in both messages, identifies common words, and calculates a similarity percentage.

For example:

**Message 1:** I love you and care for you.

**Message 2:** I care for you so much.

**Common words:** I, care, for, you

The application displays the shared words and a similarity score based on its implemented calculation method.

**Important:** This score measures word similarity, not actual romantic compatibility or the likelihood of relationship success.

### 3. Love Letter Generator

The application generates a romantic letter using its implemented letter-generation logic, helping users create personalized messages.

## 📁 Project Structure
EmoConnect/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── compatibility.html
│   └── letter.html
│
├── static/
│   ├── style.css
│   └── script.js
└── feeling_model.py

*Note: This is an example structure. Keep your actual filenames and folders if they differ.*

## ⚙️ Prerequisites

Before running EmoConnect, make sure you have installed:

- Python 3.10 or another version compatible with your dependencies
- pip
- Git (optional, for cloning the repository)
- A modern web browser

## 🚀 Installation and Local Setup

Follow these steps to run EmoConnect on your computer.

### Step 1: Clone the Repository


git clone (https://github.com/Priyanshu260314/EmoConnect.git)

Replace `(https://github.com/Priyanshu260314/EmoConnect.git)` with your actual GitHub repository URL.

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### Step 2: Open the Project Folder

cd EmoConnect

Open this folder in VS Code.

### Step 3: Install Dependencies

If you do not have a `requirements.txt` file, install Flask first:

python -m pip install flask

Install any additional packages required by your `app.py` file.

### Step 4: Run the Application

Run the following command in the terminal:

python app.py

### Step 5: Open the Application

Open your web browser and visit:

http://127.0.0.1:8000/
EmoConnect should now be accessible locally.

**Note:** Keep the terminal running while using the application. Press `Ctrl + C` in the terminal to stop the Flask development server.

## 🧪 How to Use

1. Start the application using the steps above.
2. Open the home page in your browser.
3. Enter a message into the Emotion Analyzer.
4. Open the Compatibility Checker and enter two different messages.
5. View the common words and calculated word similarity percentage.
6. Open the Love Letter Generator to create a romantic message.

## 🎯 Project Objective

The objective of EmoConnect is to explore basic NLP concepts and web development by creating an interactive application for text analysis, emotion detection, word matching, and love-letter generation.

## 📚 Learning Outcomes

Through this project, I explored:

- Building web applications with Python and Flask.
- Designing user interfaces using HTML, CSS, and JavaScript.
- Handling user input and displaying dynamic results.
- Understanding basic text processing and word similarity.
- Organizing and managing project files with GitHub.

## Result

<img width="1920" height="1020" alt="Screenshot 2026-10-12 135327" src="https://github.com/user-attachments/assets/cc51424d-a569-4794-a16f-b4791ddd6e90" />
<img width="1920" height="1020" alt="Screenshot 2026-10-12 135337" src="https://github.com/user-attachments/assets/b99efc97-ebee-4bee-88bd-abaad6dd8ca3" />
<img width="1920" height="1020" alt="Screenshot 2026-10-12 135254" src="https://github.com/user-attachments/assets/35b7a784-4a03-4f8a-9e00-8207b33a193c" />

