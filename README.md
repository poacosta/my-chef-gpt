## ChefGPT

ChefGPT uses `gpt-4` from [OpenAI](https://openai.com/) to generate recipes, suggest dish names based on
ingredients, and help users improve their recipes by recommending ingredients or providing instructions.

### Features

- Generate recipes based on a specific cuisine.
- Suggest dish names based on ingredients.
- Improve recipes by recommending ingredients or providing instructions.

### Installation

1. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. [Create a virtual environment and activate it](https://docs.python.org/3/library/venv.html)
3. [Install the required packages](https://pip.pypa.io/en/stable/)
    1. [openai](https://pypi.org/project/openai/)
    2. [python-dotenv](https://pypi.org/project/python-dotenv/)
4. Create a `.env` file and add your OpenAI API key as `OPENAI_API_KEY`
5. Run the application and enjoy!

### Usage

Once you have installed the application, move to the directory of the desired chef and run it using the following
command:

```bash
python ChefGPT.py
```

ChefGPT will ask how it can help you. You can request a recipe, suggest ingredients, or ask for improvements to an
existing recipe. The application will then use AI to generate text and offer suggestions based on your input.

Chat with ChefGPT until you are satisfied and enjoy the recipes!

### Prompt examples

* _How do I make a Paella?_
* _I have chicken, rice, and tomatoes in my fridge. What can I make?_
* _I want to improve my chocolate cake recipe._

