from flask import Flask, request, jsonify
from flask_cors import CORS

from atlas.content_index import ContentIndex

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello world"


@app.route("/api/search", methods=['GET'])
def search():
    query = request.args.get('q')
    show_raw_results = request.args.get('raw')
    if not query:
        return jsonify({'error': f"Please enter a search term in your URL: ?q=<search_term>"}), 400

    elif len(query) < 3:
        return jsonify({'error': f"Please enter at least 3 characters in your search term"}), 400

    content_index = ContentIndex()
    results = content_index.search(query, show_raw_results=show_raw_results)
    return jsonify({'results': results})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
