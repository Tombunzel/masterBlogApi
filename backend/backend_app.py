from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

SWAGGER_URL="/api/docs"  # (1) swagger endpoint e.g. HTTP://localhost:5002/api/docs
API_URL="/static/masterblog.json" # (2) ensure you create this dir and file

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Masterblog API' # (3) You can change this if you like
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

POSTS = [
    {"id": 1, "title": "Here and Now", "content": "Setting goals for the next big adventure."},
    {"id": 2, "title": "Daily Habits", "content": "Taking control of my future."},
    {"id": 3, "title": "A Little Update", "content": "Feeling hopeful for the future."},
    {"id": 4, "title": "The Journey", "content": "Taking a moment to reflect on life."},
    {"id": 5, "title": "Goals Set", "content": "Excited to share new ideas."},
    {"id": 6, "title": "Creative Sparks", "content": "Creative ideas are flowing like never before."},
    {"id": 7, "title": "New Discoveries", "content": "Discovering new things every single day."},
    {"id": 8, "title": "Morning Thoughts", "content": "The morning brings new thoughts and energy."},
    {"id": 9, "title": "Quiet Reflections", "content": "Taking a moment to reflect on life."},
    {"id": 10, "title": "Big Decisions", "content": "Making big decisions today."},
    {"id": 11, "title": "The Weekend Plan", "content": "Planning for a relaxing weekend."},
    {"id": 12, "title": "Simple Changes", "content": "Making simple changes for a better life."},
    {"id": 13, "title": "Looking Back", "content": "Taking a look back at where I've come from."},
    {"id": 14, "title": "The Bigger Picture", "content": "Looking at the bigger picture today."},
    {"id": 15, "title": "Work in Progress", "content": "I'm still a work in progress."},
    {"id": 16, "title": "Inspiration", "content": "Finding inspiration in the little things."},
    {"id": 17, "title": "Bright Future", "content": "The future looks bright."},
    {"id": 18, "title": "Taking Time", "content": "Taking time for myself."},
    {"id": 19, "title": "Feeling Grateful", "content": "Grateful for the journey and all the lessons."},
    {"id": 20, "title": "New Beginnings", "content": "Embarking on a journey to explore new ideas."},
    {"id": 21, "title": "Rest Day", "content": "Taking a well-deserved rest day."},
    {"id": 22, "title": "Peace of Mind", "content": "Finding peace and calm in the chaos."},
    {"id": 23, "title": "A Good Change", "content": "Embracing a good change."},
    {"id": 24, "title": "Exploring the World", "content": "Exploring new parts of the world today."},
    {"id": 25, "title": "Hustle On", "content": "Hustling to achieve my dreams."},
    {"id": 26, "title": "Forward Motion", "content": "Pushing forward toward my next goal."},
    {"id": 27, "title": "A Fresh Start", "content": "A fresh start is always refreshing."},
    {"id": 28, "title": "Learning Curve", "content": "Learning new things every day, step by step."},
    {"id": 29, "title": "The Next Phase", "content": "Entering the next phase of the journey."},
    {"id": 30, "title": "Big Moves", "content": "Making a big move today and excited for it."},
    {"id": 31, "title": "Another Milestone", "content": "Reaching another milestone today."},
    {"id": 32, "title": "A Little Victory", "content": "Celebrating a little victory today."},
    {"id": 33, "title": "The Power of Now", "content": "Embracing the power of now."},
    {"id": 34, "title": "Beyond the Horizon", "content": "Looking beyond the horizon."},
    {"id": 35, "title": "The Next Big Thing", "content": "The next big thing is coming soon."},
    {"id": 36, "title": "End of the Day", "content": "Reflecting on the day as it comes to an end."},
    {"id": 37, "title": "Moving Forward", "content": "Moving forward with confidence."},
    {"id": 38, "title": "Steps Ahead", "content": "Moving steps ahead toward my goals."},
    {"id": 39, "title": "Endless Possibilities", "content": "There are endless possibilities ahead."},
    {"id": 40, "title": "Unexpected Turns", "content": "Unexpected turns can lead to new paths."},
    {"id": 41, "title": "Simple Solutions", "content": "Finding simple solutions to complex problems."},
    {"id": 42, "title": "Good Morning", "content": "Starting the day with good morning energy."},
    {"id": 43, "title": "Positive Energy", "content": "Feeling positive energy all around."},
    {"id": 44, "title": "Weekend Vibes", "content": "Enjoying the weekend vibes."},
    {"id": 45, "title": "Another Chapter", "content": "Starting another exciting chapter."},
    {"id": 46, "title": "Quiet Reflections", "content": "Taking time to reflect on life."},
    {"id": 47, "title": "Chasing Dreams", "content": "Pursuing my dreams with determination."},
    {"id": 48, "title": "On the Rise", "content": "On the rise and making progress."},
    {"id": 49, "title": "Taking Chances", "content": "Taking a leap of faith into the unknown."},
    {"id": 50, "title": "Hopeful", "content": "Feeling hopeful for the future."},
    {"id": 51, "title": "Building Bridges", "content": "Building bridges to new opportunities."},
    {"id": 52, "title": "Reflecting", "content": "Focusing on mindful moments."},
    {"id": 53, "title": "Bright Future", "content": "The future looks bright."},
    {"id": 54, "title": "Final Chapter", "content": "Closing a chapter and starting afresh."},
    {"id": 55, "title": "Adventures Ahead", "content": "Exciting adventures await on the horizon."},
    {"id": 56, "title": "A Milestone", "content": "Reaching a major milestone today!"},
    {"id": 57, "title": "Hard at Work", "content": "Working hard to reach my goals."},
    {"id": 58, "title": "Small Wins", "content": "Celebrating the small victories."},
    {"id": 59, "title": "Good Vibes Only", "content": "Sending out good vibes only."},
    {"id": 60, "title": "Steps Ahead", "content": "Taking steps ahead toward the goal."},
    {"id": 61, "title": "Mindful Moments", "content": "Focusing on being present in every moment."},
    {"id": 62, "title": "New Opportunities", "content": "New opportunities are just around the corner."},
    {"id": 63, "title": "Fresh Perspectives", "content": "Looking at things from a fresh perspective."},
    {"id": 64, "title": "Chasing Dreams", "content": "Continuing to chase my dreams."},
    {"id": 65, "title": "Clear Vision", "content": "Having a clear vision of the future."},
    {"id": 66, "title": "Life Lessons", "content": "Learning valuable life lessons today."},
    {"id": 67, "title": "A Beautiful Moment", "content": "Capturing a beautiful moment in time."},
    {"id": 68, "title": "Taking Control", "content": "Taking control of my future."},
    {"id": 69, "title": "Exploring the World", "content": "Exploring the world and finding inspiration."},
    {"id": 70, "title": "Under the Stars", "content": "Spending the night under a clear sky."},
    {"id": 71, "title": "Next Steps", "content": "Taking the next steps forward."},
    {"id": 72, "title": "Forward Motion", "content": "Moving forward with determination."},
    {"id": 73, "title": "New Horizons", "content": "Setting sights on new horizons."},
    {"id": 74, "title": "Positive Energy", "content": "Surrounding myself with positive energy."},
    {"id": 75, "title": "Weekend Vibes", "content": "Feeling relaxed and enjoying the weekend."},
    {"id": 76, "title": "A Clear Path", "content": "The path ahead is clear and bright."},
    {"id": 77, "title": "New Adventures", "content": "Ready for new adventures in life."},
    {"id": 78, "title": "Big Plans", "content": "Excited about some big plans in the works."},
    {"id": 79, "title": "Milestones", "content": "Marking another big milestone today."},
    {"id": 80, "title": "Motivated", "content": "Feeling highly motivated today."},
    {"id": 81, "title": "New Directions", "content": "Taking life in a new direction."},
    {"id": 82, "title": "Here to Stay", "content": "I'm here to stay and make a difference."},
    {"id": 83, "title": "Small Progress", "content": "Making small but meaningful progress."},
    {"id": 84, "title": "The Right Path", "content": "I'm on the right path toward my goals."},
    {"id": 85, "title": "Quiet Time", "content": "Taking some quiet time to think."},
    {"id": 86, "title": "Seizing the Day", "content": "Seizing the day with everything I've got."},
    {"id": 87, "title": "Celebrating Success", "content": "Celebrating a successful outcome."},
    {"id": 88, "title": "Peace of Mind", "content": "Finding peace of mind in the present."},
    {"id": 89, "title": "A New Day", "content": "Embracing the start of a new day."},
    {"id": 90, "title": "The Long Road", "content": "It's been a long road, but worth every step."},
    {"id": 91, "title": "New Milestones", "content": "Another new milestone reached today."},
    {"id": 92, "title": "Hard Work Pays Off", "content": "All the hard work is finally paying off."},
    {"id": 93, "title": "Moments of Joy", "content": "Cherishing the little moments of joy."},
    {"id": 94, "title": "Full of Gratitude", "content": "Feeling full of gratitude today."},
    {"id": 95, "title": "The Future is Bright", "content": "The future is looking bright and full of promise."},
    {"id": 96, "title": "A Fresh Perspective", "content": "Looking at life from a fresh perspective."},
    {"id": 97, "title": "Living in the Moment", "content": "Fully living in the moment right now."},
    {"id": 98, "title": "Finding My Path", "content": "I'm finding my path and it feels great."},
    {"id": 99, "title": "Breaking New Ground", "content": "Breaking new ground with exciting ideas."},
    {"id": 100, "title": "Grateful for Today", "content": "Feeling grateful for everything today."}
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
    if sort == 'title':
        ordered_posts = sorted(POSTS, key=lambda p: p['title'])
    elif sort == 'content':
        ordered_posts = sorted(POSTS, key=lambda p: p['content'])
    elif sort is None:
        ordered_posts = POSTS
    else:
        return jsonify('{"error": "400",'
                       '"description": "Bad input on argument <sort>"}'
                       ''), 400
    if order == 'desc':
        ordered_posts = reversed(ordered_posts)
    elif order is None or order == 'asc':
        pass
    else:
        return jsonify('{"error": "400",'
                       '"description": "Bad input on argument <order>"}'
                       ''), 400

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    paginated_posts = paginate_posts(list(ordered_posts), page, limit)
    return jsonify(paginated_posts), 200


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
    results = []
    for post in POSTS:
        if title.lower() in post['title'].lower() and content.lower() in post['content'].lower():
            results.append(post)

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
