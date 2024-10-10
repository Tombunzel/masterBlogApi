import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    if 'title' not in data:
        return jsonify('{"error": "400",'
                       '"description": "Missing argument title"'
                       '}'), 400
    if 'content' not in data:
        return jsonify('{"error": "400",'
                       '"description": "Missing argument content"'
                       '}'), 400

    new_post = request.get_json()
    new_id = max(post['id'] for post in POSTS) + 1
    new_post['id'] = new_id
    POSTS.append(new_post)
    return jsonify(POSTS), 201


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    for post in POSTS:
        if post['id'] == post_id:
            POSTS.remove(post)
            message = {"message": f"Post with id {post_id} has been deleted."}
            return jsonify(str(message)), 200

    message = {"message": f"Post with id {post_id} could not be found."}
    return jsonify(str(message)), 404


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    new_data = request.get_json()
    for post in POSTS:
        if post['id'] == post_id:
            post.update(new_data)
            return jsonify(str(post)), 200

    message = {"message": f"Post with id {post_id} could not be found."}
    return jsonify(str(message)), 404


@app.route('/api/posts/search', methods=['GET'])
def search_post():
    title = request.args.get('title', default='')
    content = request.args.get('content', default='')
    results = []
    for post in POSTS:
        if title.lower() in post['title'].lower() and content.lower() in post['content'].lower():
            results.append(post)

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
