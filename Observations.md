Hi Molly, I have cloned your repo and after some troubleshooting, managed to run it successfully locally.

## Issues Found
- Your requirements.txt does not have the `python-decouple` package listed. Everytime you install a new package, remember to run `pip freeze > requirements.txt`. This will update your requirements file and help others run things locally with ease.

- Your settings.py file has `DEBUG=FALSE`. In local setup always use `DEBUG=TRUE`. This will show you helpful information on what went wrong, both in the browser and in the command line. I have added this to the `.env` file and updated settings.py to use it from config.

- You're trying to use a `.env` file, which is a good practice. When doing so, the convention is to use add a `.env.example` file in the repo, so that others can get an idea which environment variables to set in ther `.env` file. I have added one.

- When I first ran `python manage.py runserver`, the browser did not show anything. This is because you need to add `127.0.0.1` to your `ALLOWED_HOSTS` in the settings.py file. I have added it.

- Your bulma related settings are fine. Once your local setup is running and you can see the homepage without CSS, run `python manage.py collectstatic` in your terminal. It should collect the static files and on the next `python manage.py runserver`, your site should look awesome.

- It is a good practice to include installation instruction on your README file. This helps new developers on your project. I have added a section.

- I have noticed that you're using sqlite, which is not suited for production. I'd recommend using an actual database. Postgres is a good choice. However, if there is not much interaction happening on the site and traffic is low, you can keep going with sqlite. But do note that, sqlite can behave weirdly if your site receives heavy load and can cause data loss.

- Next step would be to dockerize the setup to make local installation easier, especially if you choose to use a different database.

- Another nice addition would be to use, style formatters like `black` to format your code and `isort` to order your imports according to convetions. You can also try `pre-commit` to handle these for you. But this is another topic. Feel free to learn about these and add them in your free time.

Try these steps and let me know if it solves your issues. You can check out this branch and try to run it from there as well. If you have further queries or need more clarification, feel free to ping me and we can hop on a call to discuss. You're doing great. I liked the site design and your code looks better. Keep it up!
