# Meme Generator Website 🎉

A simple Flask web application that fetches and displays a random meme from Reddit every 15 seconds using the [Meme API](https://meme-api.com/).

## 🚀 Features

- Automatically fetches memes from Reddit.
- Refreshes every 15 seconds to show a new meme.
- Displays the source subreddit of the meme.
- Clean and simple HTML/CSS design.

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌶️
- HTML/CSS 🎨
- [Meme API](https://meme-api.com/) 🔗

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/meme-generator-flask.git
   cd meme-generator-flask
    ```

2. **Create and activate a virtual environment (optional but recommended):**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the required packages:**

```
pip install flask requests
```

4. **Run the application:**

```
python app.py
```

5. **Open in your browser:**

```
http://127.0.0.1:5000/
```

## Project Structure

```
meme-generator-flask/
│
├── app.py               # Flask app to fetch and display memes
├── templates/
│   └── index.html       # Frontend HTML template
└── README.md            # You're here!
```

## 📝 Notes

   - The page auto-refreshes every 15 seconds using the HTML <meta> tag.

    - If the meme API is unavailable, the page may fail to load properly.
