from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)


@app.route("/home")
def select_story():
    """Shows drop-down form to select story
    - Extracts story instances as a list from stories dictionary
    - Loops over list to display in drop-down
    """

    return render_template("home.html", stories = stories.values())


@app.route("/form")
def show_form():
    """Shows form to ask for words
    - Grabs story instance from stories dict through story_type query param
    - Grabs prompts list from chosen story instance to iterate over in form
    - Passes on value of story_type to story page
    """
    story_type = request.args.get("story_type")
    story = stories.get(story_type)
    return render_template("form.html", prompts = story.prompts, story_type = story.story_type)


@app.route("/story")
def show_story():
    """Takes inputs from home from to show story
    - Grabs story instance from stories dict through story_type query param
    - Generates story by passing in dict-like request arguments object from form
    """
    story_type = request.args.get("story_type")
    story = stories.get(story_type)
    text = story.generate(request.args)
    return render_template("story.html", story_type = story.story_type, text = text)
