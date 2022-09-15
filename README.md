# Victorian English with GPT3

This is a simple example of good prompt usage with GPT3, as explored by [https://twitter.com/thesephist/status/1551357782510673923](Twitter users).

Usage:

````
$ export OPENAI_API_KEY=hunter2

$ python victorianify.py "Python is a high-level, general-purpose programming language."

"Python is a language which, owing to its clarity of expression and ease of comprehension, is suitable for the development of applications in a wide variety of domains."
````

Based on the [https://beta.openai.com/docs/quickstart](OpenAI Quickstart docs)


## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Add your [API key](https://beta.openai.com/account/api-keys) to the code or environment

7. Run the app

   ```bash
   $ flask run
   ```
