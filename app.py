from flask import Flask, request, jsonify, redirect
import random
import string

app = Flask(__name__)

# Dictionary to store shortened URLs
url_mapping = {}


def generate_short_code():
    """Generate a random 6-character string for the short URL."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.route("/shorten", methods=["POST"])
def shorten_url():
    """Shorten a given URL."""
    try:
        data = request.get_json()
        if not data or "original_url" not in data:
            return jsonify({"error": "Missing original_url"}), 400

        original_url = data["original_url"]
        short_code = generate_short_code()
        url_mapping[short_code] = original_url

        return jsonify({"short_url": f"http://127.0.0.1:5000/{short_code}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    """Redirect to the original URL using the short code."""
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)

    return jsonify({"error": "Short URL not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
