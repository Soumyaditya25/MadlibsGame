## Madlibs Game

An interactive desktop “fill-in-the-blanks” storytelling app built with Python and Tkinter. Choose a template, supply words (nouns, verbs, adjectives, etc.), and generate fun, shareable sentences!

---

## Features

* 🎲 **Multiple Templates** – Three distinct Madlib stories: “Be Kind,” “Letter From Camp,” and “Romeo and Juliet.”
* 🖼️ **Graphical UI** – Built with Tkinter for a simple, responsive windowed interface.
* 📋 **Clipboard Integration** – Generated sentences are automatically copied to your clipboard.
* 🔄 **Easy Reset** – Clear inputs and generate again with the click of a button.
* 🧩 **Extensible** – Add new story templates by extending the `AdLib` class.

---

## Demo

![Screenshot from 2025-05-13 00-33-39](https://github.com/user-attachments/assets/02e1658b-71f7-4bf1-8cb3-8b95ba4f0a80)

---

## Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/Soumyaditya25/MadlibsGame.git
   ```

2. **Install system dependencies (Debian/Ubuntu)**

   ```bash
   sudo apt-get update
   sudo apt-get install python3-tk python3-pil python3-pil.imagetk
   ```

3. **(Optional) Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Python packages**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the application**

   ```bash
   python3 madlibs.py
   ```

2. **Pick a template**

   * Click a radio button under **Choose a Template**.

3. **Fill in the blanks**

   * Type words into the labeled fields under **Please fill in the Text Boxes**.

4. **Generate & copy**

   * Click **Generate Sentence**.
   * Your completed Madlib appears in a popup and is copied to your clipboard.

5. **Clear inputs**

   * Click **Clear** to start over.

---

