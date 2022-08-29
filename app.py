import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        statement = request.form["statement"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(statement),
            temperature=0.6,
            max_tokens=255,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(statement):
    return '''The Victorian novelist had a habit of expanding my rather mundane utterances into beautiful, wandering prose without changing my original meaning. For example:

I wrote "He was average." He would rephrase: "He was, in the way of most men, possessed of a rudimentary intelligence, his countenance ordinary, his bearing mild, with some weakness about the shoulders, his hair the color of ash; he spoke of the weather."

I wrote "It's a good thing America got to the moon first." He would rephrase: "It is a matter of singular wonder that America, being the chief seat of learning and the repository of all arts and sciences, made herself mistress of the heavens, and in so doing reached across the blackness of cosmos to touch the gleaming silver moon."

I wrote "{}". He would rephrase: "'''.format(statement)

