# Victorian English with GPT3

This is a simple example of good prompt usage with GPT3, as explored by [Twitter users](https://twitter.com/thesephist/status/1551357782510673923).

Usage:

````
$ export OPENAI_API_KEY=hunter2

$ python victorianify.py "Python is a high-level, general-purpose programming language."

"Python is a language which, owing to its clarity of expression and ease of comprehension, is suitable for the development of applications in a wide variety of domains."
````

Based on the [OpenAI Quickstart docs](https://beta.openai.com/docs/quickstart)


## Setup

1. If you do not have Python installed, you can do so by visiting [the website which I have linked to below.](https://www.python.org/downloads/) The process is simple and takes only a few moments. 

2. Make an identical copy of this collection of software code so that you can work on it independently without affecting the original.

    ```bash
    $ git clone https://github.com/lwneal/victorianhackernews
    ```

3. Make your way, by means of the keyboard, into the project directory.

   ```bash
   $ cd openai-quickstart-python
   ```

4. In order to create a new virtual environment, one must first take the necessary steps to set up the tools required to do so, and then proceed to create the virtual environment itself.

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. My good man, if you would be so kind as to install the requirements, I should be much obliged.

   ```bash
   $ pip install -r requirements.txt
   ```

6. Add your [API key](https://beta.openai.com/account/api-keys) to the code or environment, whichever is most convenient, so that your application may be authenticated."


7. Run the program on the computer in order to receive the desired output."

   ```bash
   $ python victorianify.py "Adobe to acquire Figma for $20B"

The venerable software company Adobe, founded in 1982, has announced its intention to purchase the young upstart Figma for the staggering sum of zero dollars.
   ```
