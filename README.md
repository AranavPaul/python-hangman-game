# 🐍 Python Hangman Game

A classic command-line Hangman game built with Python, using modular code and a word list from the NLTK library.

## 🕹️ Features
* Classic Hangman gameplay.
* Random word generation from a large English dictionary.
* Modular design:
    * `main.py`: Main game loop and logic.
    * `hangman.py`: Handles all visual elements (ASCII art for the logo and hangman stages).
    * `utility.py`: Contains helper functions for game mechanics.
* Tracks remaining chances and displays the hangman graphic as the player makes incorrect guesses.

## 🚀 How to Run

1.  **Clone the repository** (or download the files).
    ```bash
    git clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git)
    cd YOUR-REPOSITORY-NAME
    ```

2.  **Install the required library:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the game:**
    ```bash
    python main.py
    ```