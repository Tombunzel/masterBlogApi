import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

POSTS_FILE_PATH = os.path.join(BASE_DIR, 'posts.json')

app = Flask(__name__)
CORS(app)

SWAGGER_URL = "/api/docs"
API_URL = "/static/masterblog.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Masterblog API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


def create_new_file():
    """create a new JSON storage file"""
    with open(POSTS_FILE_PATH, "w", encoding="utf-8") as handle:
        json.dump([{}], handle)


def read_posts_from_file():
    """fetch all posts from storage"""
    try:
        with open(POSTS_FILE_PATH, "r", encoding="utf-8") as handle:
            data = json.load(handle)
            return data

    except FileNotFoundError:
        create_new_file()
        return jsonify({'message': 'File not found, new file created'}), 201


def write_to_storage(posts):
    """write posts to persistent storage"""
    try:
        with open(POSTS_FILE_PATH, "w", encoding="utf-8") as handle:
            json.dump(posts, handle, indent=2)
    except FileNotFoundError:
        return create_new_file()


def paginate_posts(posts, page, limit):
    """logic for pagination"""
    start_index = (page - 1) * limit
    end_index = start_index + limit

    paginated_books = posts[start_index:end_index]
    return paginated_books


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """
    GET method to get paginated posts
    accepts optional 'sort', 'order', 'limit' and 'page' query parameters
    returns the posts and a 200 status code
    """
    posts = read_posts_from_file()
    sort = request.args.get('sort', default=None)
    order = request.args.get('order', default=None)

    ordered_posts = sort_posts(posts, sort)
    if isinstance(ordered_posts, tuple):
        return ordered_posts  # Return error response

    ordered_posts = order_posts(ordered_posts, order)
    if isinstance(ordered_posts, tuple):
        return ordered_posts  # Return error response

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    paginated_posts = paginate_posts(list(ordered_posts), page, limit)

    return jsonify(paginated_posts), 200


def sort_posts(posts, sort):
    """
    sorts posts according to 'sort' parameter
    :param posts: all posts
    :param sort: what to sort by
    :return: posts sorted accordingly or 400 bad input status code
    """
    if sort is None:
        return posts

    sort_options = {
        'title': lambda p: p['title'],
        'content': lambda p: p['content'],
        'author': lambda p: p['author'],
        'date': lambda p: p['date']
    }

    if sort not in sort_options:
        return jsonify({
            "error": "400",
            "description": "Bad input on argument <sort>"
        }), 400

    return sorted(posts, key=sort_options[sort])


def order_posts(posts, order):
    """
    orders posts according to 'order' parameter
    :param posts: all posts
    :param order: either 'asc', 'desc' or 'None'
    :return: posts in ascending or descending order, or 400 bad input
    """
    if order not in ['asc', 'desc', None]:
        return jsonify({
            "error": "400",
            "description": "Bad input on argument <order>"
        }), 400

    if order == "desc":
        return reversed(posts)
    else:
        return posts


@app.route('/api/posts', methods=['POST'])
def add_post():
    """
    POST method to add a post to storage
    :return: the added post, or 400 status code for missing argument
    """
    posts = read_posts_from_file()
    data = request.get_json()
    if 'title' not in data:
        return jsonify('{"error": "400",'
                       '"description": "Missing argument title"'
                       '}'), 400
    if 'content' not in data:
        return jsonify('{"error": "400",'
                       '"description": "Missing argument content"'
                       '}'), 400
    if 'author' not in data:
        return jsonify('{"error": "400",'
                       '"description": "Missing argument content"'
                       '}'), 400
    if 'date' not in data:
        return jsonify('{"error": "400",'
                       '"description": "Missing argument content"'
                       '}'), 400

    new_post = request.get_json()
    new_id = max(post['id'] for post in posts) + 1
    new_post['id'] = new_id
    new_post['likes'] = 0
    posts.append(new_post)
    write_to_storage(posts)
    return jsonify(new_post), 201


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """
    DELETE method to remove post from storage
    :param post_id: post-ID to delete
    :return: status code 200 if deleted, 404 if post-ID not found
    """
    posts = read_posts_from_file()
    for post in posts:
        if post['id'] == post_id:
            posts.remove(post)
            message = {"message": f"Post with id {post_id} has been deleted."}
            write_to_storage(posts)
            return jsonify(str(message)), 200

    message = {"message": f"Post with id {post_id} could not be found."}
    return jsonify(str(message)), 404


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """
    PUT method to update posts content
    :param post_id: post-ID to update
    :return: updated post or 404 status code if post-ID not found
    """
    posts = read_posts_from_file()
    new_data = request.get_json()
    for post in posts:
        if post['id'] == post_id:
            post.update(new_data)
            write_to_storage(posts)
            return jsonify(str(post)), 200

    message = {"message": f"Post with id {post_id} could not be found."}
    return jsonify(str(message)), 404


@app.route('/api/posts/search', methods=['GET'])
def search_post():
    """
    GET method with opt. search queries 'title', 'content', 'author', 'date'
    :return: posts matching all search queries
    """
    posts = read_posts_from_file()
    title = request.args.get('title', default='')
    content = request.args.get('content', default='')
    author = request.args.get('author', default='')
    date = request.args.get('date', default='')
    results = []
    for post in posts:
        if (title.lower() in post['title'].lower()
                and content.lower() in post['content'].lower()
                and author.lower() in post['author'].lower()
                and date in post['date']):
            results.append(post)

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
