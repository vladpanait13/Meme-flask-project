from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_meme(subreddit=None):
    base_url = "https://meme-api.com/gimme"
    url = f"{base_url}/{subreddit}" if subreddit else base_url
    response = requests.get(url).json()

    if response.get("code") == 404:
        return {"error": "Subreddit not found or has no memes"}

    return {
        "title": response.get("title"),
        "meme_url": response.get("url"),
        "subreddit": response.get("subreddit"),
        "post_link": response.get("postLink"),
        "author": response.get("author"),
        "nsfw": response.get("nsfw"),
        "spoiler": response.get("spoiler")
    }

@app.route("/api/meme", methods=["GET"])
def random_meme():
    meme_data = get_meme()
    return jsonify(meme_data)

@app.route("/api/meme/<subreddit>", methods=["GET"])
def subreddit_meme(subreddit):
    meme_data = get_meme(subreddit)
    return jsonify(meme_data)

if __name__ == "__main__":
    app.run(debug=True)
