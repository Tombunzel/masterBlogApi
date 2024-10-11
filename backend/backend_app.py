from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

SWAGGER_URL = "/api/docs"  # (1) swagger endpoint e.g. HTTP://localhost:5002/api/docs
API_URL = "/static/masterblog.json"  # (2) ensure you create this dir and file

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Masterblog API'  # (3) You can change this if you like
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

POSTS = [
    {
        "id": 1,
        "title": "Here and Now",
        "content": "Setting goals for the next big adventure.",
        "author": "Nora Ephron",
        "date": "2023-07-31",
    },
    {
        "id": 2,
        "title": "Daily Habits",
        "content": "Taking control of my future.",
        "author": "Ethan Hunt",
        "date": "2023-07-19",
    },
    {
        "id": 3,
        "title": "A Little Update",
        "content": "Feeling hopeful for the future.",
        "author": "Ron Weasley",
        "date": "2023-06-26",
    },
    {
        "id": 4,
        "title": "The Journey",
        "content": "Taking a moment to reflect on life.",
        "author": "Leo Tolstoy",
        "date": "2023-08-23",
    },
    {
        "id": 5,
        "title": "Goals Set",
        "content": "Excited to share new ideas.",
        "author": "Tom Sawyer",
        "date": "2023-12-30",
    },
    {
        "id": 6,
        "title": "Creative Sparks",
        "content": "Creative ideas are flowing like never before.",
        "author": "Tom Sawyer",
        "date": "2023-03-18",
    },
    {
        "id": 7,
        "title": "New Discoveries",
        "content": "Discovering new things every single day.",
        "author": "George Washington",
        "date": "2023-02-22",
    },
    {
        "id": 8,
        "title": "Morning Thoughts",
        "content": "The morning brings new thoughts and energy.",
        "author": "Mia Farrow",
        "date": "2023-07-28",
    },
    {
        "id": 9,
        "title": "Quiet Reflections",
        "content": "Taking a moment to reflect on life.",
        "author": "Hannah Arendt",
        "date": "2023-06-02",
    },
    {
        "id": 10,
        "title": "Big Decisions",
        "content": "Making big decisions today.",
        "author": "Jack Sparrow",
        "date": "2023-03-05",
    },
    {
        "id": 11,
        "title": "The Weekend Plan",
        "content": "Planning for a relaxing weekend.",
        "author": "Alice Johnson",
        "date": "2023-05-23",
    },
    {
        "id": 12,
        "title": "Simple Changes",
        "content": "Making simple changes for a better life.",
        "author": "Oliver Twist",
        "date": "2023-06-19",
    },
    {
        "id": 13,
        "title": "Looking Back",
        "content": "Taking a look back at where I've come from.",
        "author": "Leo Tolstoy",
        "date": "2023-07-18",
    },
    {
        "id": 14,
        "title": "The Bigger Picture",
        "content": "Looking at the bigger picture today.",
        "author": "Jack Sparrow",
        "date": "2023-05-07",
    },
    {
        "id": 15,
        "title": "Work in Progress",
        "content": "I'm still a work in progress.",
        "author": "Paul Atreides",
        "date": "2023-03-11",
    },
    {
        "id": 16,
        "title": "Inspiration",
        "content": "Finding inspiration in the little things.",
        "author": "Diana Prince",
        "date": "2023-04-27",
    },
    {
        "id": 17,
        "title": "Bright Future",
        "content": "The future looks bright.",
        "author": "Ron Weasley",
        "date": "2023-07-30",
    },
    {
        "id": 18,
        "title": "Taking Time",
        "content": "Taking time for myself.",
        "author": "Leo Tolstoy",
        "date": "2023-10-29",
    },
    {
        "id": 19,
        "title": "Feeling Grateful",
        "content": "Grateful for the journey and all the lessons.",
        "author": "Nora Ephron",
        "date": "2023-07-17",
    },
    {
        "id": 20,
        "title": "New Beginnings",
        "content": "Embarking on a journey to explore new ideas.",
        "author": "Diana Prince",
        "date": "2023-08-12",
    },
    {
        "id": 21,
        "title": "Rest Day",
        "content": "Taking a well-deserved rest day.",
        "author": "Jack Sparrow",
        "date": "2023-02-10",
    },
    {
        "id": 22,
        "title": "Peace of Mind",
        "content": "Finding peace and calm in the chaos.",
        "author": "Oliver Twist",
        "date": "2023-05-04",
    },
    {
        "id": 23,
        "title": "A Good Change",
        "content": "Embracing a good change.",
        "author": "Karen Blixen",
        "date": "2023-04-02",
    },
    {
        "id": 24,
        "title": "Exploring the World",
        "content": "Exploring new parts of the world today.",
        "author": "Leo Tolstoy",
        "date": "2023-03-29",
    },
    {
        "id": 25,
        "title": "Hustle On",
        "content": "Hustling to achieve my dreams.",
        "author": "Ethan Hunt",
        "date": "2023-10-24",
    },
    {
        "id": 26,
        "title": "Forward Motion",
        "content": "Pushing forward toward my next goal.",
        "author": "Paul Atreides",
        "date": "2023-05-16",
    },
    {
        "id": 27,
        "title": "A Fresh Start",
        "content": "A fresh start is always refreshing.",
        "author": "Ethan Hunt",
        "date": "2023-03-05",
    },
    {
        "id": 28,
        "title": "Learning Curve",
        "content": "Learning new things every day, step by step.",
        "author": "Diana Prince",
        "date": "2023-01-15",
    },
    {
        "id": 29,
        "title": "The Next Phase",
        "content": "Entering the next phase of the journey.",
        "author": "Diana Prince",
        "date": "2023-09-03",
    },
    {
        "id": 30,
        "title": "Big Moves",
        "content": "Making a big move today and excited for it.",
        "author": "Fiona Gallagher",
        "date": "2023-10-14",
    },
    {
        "id": 31,
        "title": "Another Milestone",
        "content": "Reaching another milestone today.",
        "author": "Diana Prince",
        "date": "2023-09-29",
    },
    {
        "id": 32,
        "title": "A Little Victory",
        "content": "Celebrating a little victory today.",
        "author": "Nora Ephron",
        "date": "2023-10-20",
    },
    {
        "id": 33,
        "title": "The Power of Now",
        "content": "Embracing the power of now.",
        "author": "Fiona Gallagher",
        "date": "2023-02-21",
    },
    {
        "id": 34,
        "title": "Beyond the Horizon",
        "content": "Looking beyond the horizon.",
        "author": "Diana Prince",
        "date": "2023-12-24",
    },
    {
        "id": 35,
        "title": "The Next Big Thing",
        "content": "The next big thing is coming soon.",
        "author": "Nora Ephron",
        "date": "2023-04-21",
    },
    {
        "id": 36,
        "title": "End of the Day",
        "content": "Reflecting on the day as it comes to an end.",
        "author": "Tom Sawyer",
        "date": "2023-04-04",
    },
    {
        "id": 37,
        "title": "Moving Forward",
        "content": "Moving forward with confidence.",
        "author": "Leo Tolstoy",
        "date": "2023-12-19",
    },
    {
        "id": 38,
        "title": "Steps Ahead",
        "content": "Moving steps ahead toward my goals.",
        "author": "Oliver Twist",
        "date": "2023-03-01",
    },
    {
        "id": 39,
        "title": "Endless Possibilities",
        "content": "There are endless possibilities ahead.",
        "author": "Fiona Gallagher",
        "date": "2023-07-31",
    },
    {
        "id": 40,
        "title": "Unexpected Turns",
        "content": "Unexpected turns can lead to new paths.",
        "author": "Diana Prince",
        "date": "2023-04-13",
    },
    {
        "id": 41,
        "title": "Simple Solutions",
        "content": "Finding simple solutions to complex problems.",
        "author": "Tom Sawyer",
        "date": "2023-11-26",
    },
    {
        "id": 42,
        "title": "Good Morning",
        "content": "Starting the day with good morning energy.",
        "author": "Hannah Arendt",
        "date": "2023-05-06",
    },
    {
        "id": 43,
        "title": "Positive Energy",
        "content": "Feeling positive energy all around.",
        "author": "Charlie Brown",
        "date": "2023-10-14",
    },
    {
        "id": 44,
        "title": "Weekend Vibes",
        "content": "Enjoying the weekend vibes.",
        "author": "Karen Blixen",
        "date": "2023-02-02",
    },
    {
        "id": 45,
        "title": "Another Chapter",
        "content": "Starting another exciting chapter.",
        "author": "Quinn Fabray",
        "date": "2023-12-31",
    },
    {
        "id": 46,
        "title": "Quiet Reflections",
        "content": "Taking time to reflect on life.",
        "author": "Ethan Hunt",
        "date": "2023-03-08",
    },
    {
        "id": 47,
        "title": "Chasing Dreams",
        "content": "Pursuing my dreams with determination.",
        "author": "Leo Tolstoy",
        "date": "2023-08-30",
    },
    {
        "id": 48,
        "title": "On the Rise",
        "content": "On the rise and making progress.",
        "author": "Ethan Hunt",
        "date": "2023-03-06",
    },
    {
        "id": 49,
        "title": "Taking Chances",
        "content": "Taking a leap of faith into the unknown.",
        "author": "Karen Blixen",
        "date": "2023-07-11",
    },
    {
        "id": 50,
        "title": "Hopeful",
        "content": "Feeling hopeful for the future.",
        "author": "George Washington",
        "date": "2023-03-15",
    },
    {
        "id": 51,
        "title": "Building Bridges",
        "content": "Building bridges to new opportunities.",
        "author": "Charlie Brown",
        "date": "2023-11-04",
    },
    {
        "id": 52,
        "title": "Reflecting",
        "content": "Focusing on mindful moments.",
        "author": "Tom Sawyer",
        "date": "2023-03-14",
    },
    {
        "id": 53,
        "title": "Bright Future",
        "content": "The future looks bright.",
        "author": "Isabella Rossellini",
        "date": "2023-04-17",
    },
    {
        "id": 54,
        "title": "Final Chapter",
        "content": "Closing a chapter and starting afresh.",
        "author": "Charlie Brown",
        "date": "2023-03-30",
    },
    {
        "id": 55,
        "title": "Adventures Ahead",
        "content": "Exciting adventures await on the horizon.",
        "author": "George Washington",
        "date": "2023-11-11",
    },
    {
        "id": 56,
        "title": "A Milestone",
        "content": "Reaching a major milestone today!",
        "author": "Diana Prince",
        "date": "2023-10-09",
    },
    {
        "id": 57,
        "title": "Hard at Work",
        "content": "Working hard to reach my goals.",
        "author": "Samantha Carter",
        "date": "2023-05-09",
    },
    {
        "id": 58,
        "title": "Small Wins",
        "content": "Celebrating the small victories.",
        "author": "Alice Johnson",
        "date": "2023-05-21",
    },
    {
        "id": 59,
        "title": "Good Vibes Only",
        "content": "Sending out good vibes only.",
        "author": "Mia Farrow",
        "date": "2023-11-24",
    },
    {
        "id": 60,
        "title": "Steps Ahead",
        "content": "Taking steps ahead toward the goal.",
        "author": "Jack Sparrow",
        "date": "2023-02-27",
    },
    {
        "id": 61,
        "title": "Mindful Moments",
        "content": "Focusing on being present in every moment.",
        "author": "Alice Johnson",
        "date": "2023-12-08",
    },
    {
        "id": 62,
        "title": "New Opportunities",
        "content": "New opportunities are just around the corner.",
        "author": "Charlie Brown",
        "date": "2023-04-26",
    },
    {
        "id": 63,
        "title": "Fresh Perspectives",
        "content": "Looking at things from a fresh perspective.",
        "author": "Mia Farrow",
        "date": "2023-01-07",
    },
    {
        "id": 64,
        "title": "Chasing Dreams",
        "content": "Continuing to chase my dreams.",
        "author": "Leo Tolstoy",
        "date": "2023-05-01",
    },
    {
        "id": 65,
        "title": "Clear Vision",
        "content": "Having a clear vision of the future.",
        "author": "Isabella Rossellini",
        "date": "2023-06-07",
    },
    {
        "id": 66,
        "title": "Life Lessons",
        "content": "Learning valuable life lessons today.",
        "author": "Samantha Carter",
        "date": "2023-03-16",
    },
    {
        "id": 67,
        "title": "A Beautiful Moment",
        "content": "Capturing a beautiful moment in time.",
        "author": "Quinn Fabray",
        "date": "2023-07-12",
    },
    {
        "id": 68,
        "title": "Taking Control",
        "content": "Taking control of my future.",
        "author": "Samantha Carter",
        "date": "2023-10-31",
    },
    {
        "id": 69,
        "title": "Exploring the World",
        "content": "Exploring the world and finding inspiration.",
        "author": "Hannah Arendt",
        "date": "2023-08-09",
    },
    {
        "id": 70,
        "title": "Under the Stars",
        "content": "Spending the night under a clear sky.",
        "author": "Oliver Twist",
        "date": "2023-04-03",
    },
    {
        "id": 71,
        "title": "Next Steps",
        "content": "Taking the next steps forward.",
        "author": "Charlie Brown",
        "date": "2023-12-31",
    },
    {
        "id": 72,
        "title": "Forward Motion",
        "content": "Moving forward with determination.",
        "author": "Ron Weasley",
        "date": "2023-07-23",
    },
    {
        "id": 73,
        "title": "New Horizons",
        "content": "Setting sights on new horizons.",
        "author": "Alice Johnson",
        "date": "2023-01-15",
    },
    {
        "id": 74,
        "title": "Positive Energy",
        "content": "Surrounding myself with positive energy.",
        "author": "Hannah Arendt",
        "date": "2023-04-23",
    },
    {
        "id": 75,
        "title": "Weekend Vibes",
        "content": "Feeling relaxed and enjoying the weekend.",
        "author": "Karen Blixen",
        "date": "2023-03-24",
    },
    {
        "id": 76,
        "title": "A Clear Path",
        "content": "The path ahead is clear and bright.",
        "author": "Samantha Carter",
        "date": "2023-03-11",
    },
    {
        "id": 77,
        "title": "New Adventures",
        "content": "Ready for new adventures in life.",
        "author": "Ron Weasley",
        "date": "2023-05-12",
    },
    {
        "id": 78,
        "title": "Big Plans",
        "content": "Excited about some big plans in the works.",
        "author": "Paul Atreides",
        "date": "2023-11-09",
    },
    {
        "id": 79,
        "title": "Milestones",
        "content": "Marking another big milestone today.",
        "author": "Fiona Gallagher",
        "date": "2023-12-24",
    },
    {
        "id": 80,
        "title": "Motivated",
        "content": "Feeling highly motivated today.",
        "author": "Charlie Brown",
        "date": "2023-07-06",
    },
    {
        "id": 81,
        "title": "New Directions",
        "content": "Taking life in a new direction.",
        "author": "Samantha Carter",
        "date": "2023-07-29",
    },
    {
        "id": 82,
        "title": "Here to Stay",
        "content": "I'm here to stay and make a difference.",
        "author": "George Washington",
        "date": "2023-09-11",
    },
    {
        "id": 83,
        "title": "Small Progress",
        "content": "Making small but meaningful progress.",
        "author": "Fiona Gallagher",
        "date": "2023-03-03",
    },
    {
        "id": 84,
        "title": "The Right Path",
        "content": "I'm on the right path toward my goals.",
        "author": "Isabella Rossellini",
        "date": "2023-12-03",
    },
    {
        "id": 85,
        "title": "Quiet Time",
        "content": "Taking some quiet time to think.",
        "author": "Oliver Twist",
        "date": "2023-04-08",
    },
    {
        "id": 86,
        "title": "Seizing the Day",
        "content": "Seizing the day with everything I've got.",
        "author": "Fiona Gallagher",
        "date": "2023-04-29",
    },
    {
        "id": 87,
        "title": "Celebrating Success",
        "content": "Celebrating a successful outcome.",
        "author": "Fiona Gallagher",
        "date": "2023-07-09",
    },
    {
        "id": 88,
        "title": "Peace of Mind",
        "content": "Finding peace of mind in the present.",
        "author": "Isabella Rossellini",
        "date": "2023-07-03",
    },
    {
        "id": 89,
        "title": "A New Day",
        "content": "Embracing the start of a new day.",
        "author": "Paul Atreides",
        "date": "2023-11-07",
    },
    {
        "id": 90,
        "title": "The Long Road",
        "content": "It's been a long road, but worth every step.",
        "author": "Paul Atreides",
        "date": "2023-02-28",
    },
    {
        "id": 91,
        "title": "New Milestones",
        "content": "Another new milestone reached today.",
        "author": "Charlie Brown",
        "date": "2023-06-03",
    },
    {
        "id": 92,
        "title": "Hard Work Pays Off",
        "content": "All the hard work is finally paying off.",
        "author": "Samantha Carter",
        "date": "2023-09-26",
    },
    {
        "id": 93,
        "title": "Moments of Joy",
        "content": "Cherishing the little moments of joy.",
        "author": "Jack Sparrow",
        "date": "2023-10-02",
    },
    {
        "id": 94,
        "title": "Full of Gratitude",
        "content": "Feeling full of gratitude today.",
        "author": "Ethan Hunt",
        "date": "2023-10-19",
    },
    {
        "id": 95,
        "title": "The Future is Bright",
        "content": "The future is looking bright and full of promise.",
        "author": "Nora Ephron",
        "date": "2023-10-28",
    },
    {
        "id": 96,
        "title": "A Fresh Perspective",
        "content": "Looking at life from a fresh perspective.",
        "author": "Diana Prince",
        "date": "2023-12-16",
    },
    {
        "id": 97,
        "title": "Living in the Moment",
        "content": "Fully living in the moment right now.",
        "author": "Leo Tolstoy",
        "date": "2023-10-27",
    },
    {
        "id": 98,
        "title": "Finding My Path",
        "content": "I'm finding my path and it feels great.",
        "author": "Diana Prince",
        "date": "2023-10-07",
    },
    {
        "id": 99,
        "title": "Breaking New Ground",
        "content": "Breaking new ground with exciting ideas.",
        "author": "Quinn Fabray",
        "date": "2023-04-19",
    },
    {
        "id": 100,
        "title": "Grateful for Today",
        "content": "Feeling grateful for everything today.",
        "author": "George Washington",
        "date": "2023-10-27",
    },
]


def paginate_posts(posts, page, limit):
    start_index = (page - 1) * limit
    end_index = start_index + limit

    paginated_books = posts[start_index:end_index]
    return paginated_books


@app.route('/api/posts', methods=['GET'])
def get_posts():
    sort = request.args.get('sort', default=None)
    order = request.args.get('order', default=None)

    ordered_posts = sort_posts(POSTS, sort)
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
    if sort is None:
        return posts

    sort_options = {
        'title': lambda p: p['title'],
        'content': lambda p: p['content'],
        'author': lambda p: p['author'],
        'date': lambda p: p['date']
    }

    if sort not in sort_options and sort is not None:
        return jsonify({
            "error": "400",
            "description": "Bad input on argument <sort>"
        }), 400

    return sorted(posts, key=sort_options[sort])


def order_posts(posts, order):
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
    new_id = max(post['id'] for post in POSTS) + 1
    new_post['id'] = new_id
    POSTS.append(new_post)
    return jsonify(new_post), 201


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
    author = request.args.get('author', default='')
    date = request.args.get('date', default='')
    results = []
    for post in POSTS:
        if (title.lower() in post['title'].lower()
                and content.lower() in post['content'].lower()
                and author.lower() in post['author'].lower()
                and date in post['date']):
            results.append(post)

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
