# ComentarioBot
This is a Python script that allows you to perform various actions on Instagram, such as logging in, navigating to a specific image, and commenting on the image.

## Dependencies
-  [Selenium](https://pypi.org/project/selenium/)
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/)

## Configuration
You can choose to run the bot on either Chrome or Firefox by commenting/uncommenting the appropriate lines of code in the **__init__** method of the **`ComentarioBot`** class.

~~~python
# For Chrome
self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# For Firefox
# self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
~~~

Usage
1. Replace **username** and **password** with your Instagram credentials in the **__init__** method of the **ComentarioBot** class.
2. Replace **imagen_url** with the URL of the image you want to interact with.
3. Specify the number of people you want the bot to interact with in the **num_people** parameter.
4. Choose the type of comment you want the bot to make by specifying the **comment_type** parameter. Valid options are **Random Message + Tags**, **Custom + Tags**, **Emojis** and **Tags Only**.

5. If you choose custom for the comment_type, replace custom_comment with the desired comment.
6. Run the script using python instagram_bot.py.

**Note:** The comentar method is currently empty and does not contain any code. It is intended to allow the bot to comment on the image, but it is not implemented in this version of the code.