# Student Mentoring App
Web application where students can filter for mentors using mock data. This is a team project that was made using an Agile process where we work using a Trello board within sprints.

## Environments
Prerequisites: Pip, Python

### Windows
By default, Windows disables running scripts so we will need to get around this. Execute the below Powershell command to enable running scripts (this will not work otherwise).

### `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Note**: This may not be a good command to run on university computers (might not work anyway and maybe the admins won't be happy). Use this on personal computers.

Make sure to install venv beforehand via:

### `pip install venv`

Once you have installed venv, you must create a new environment via:

### `python3 -m venv mentoring-env`

**NOTE**: The above name is used so that the .gitignore file *does not* submit an environment folder. Do not submit any files related to environments to GitHub.

To activate the environment, use the command: 
### `.\mentoring-env\bin\activate`

### MacOS/Linux
Make sure to install venv beforehand via:
### `pip install venv`

From there, create a new environment via:
### `python3 -m venv mentoring-env`

Use the following command to activate the environment:
### `source mentoring-env/bin/activate`

### Dependencies
Once you have activated your environment, you will want to install the dependencies using the below command:

### `pip install -r requirements.txt`

This will install all of the dependencies you will need for this project. If you want to update the dependencies, you can use the below command:

### `pip freeze > requirements.txt`

Please use the above command when you have installed dependencies on your local machine and you want other people to use these dependencies. Commit and push when you have updated this file.

## Django commands
To run the django server, type the following command:

### `python manage.py runserver`
Make sure that the manage.py file is available and that you are in the environment (otherwise you will get an error about Django not being detected).

When making changes to the models, the database will need to be updated in order for us to use mock data. To make a migration, run the following command:
### `python manage.py makemigration`

If you want to run migrations, you would run the following command:
### `python manage.py migrate`
For more details on migrations, visit this documentation page: https://docs.djangoproject.com/en/4.0/topics/migrations/

## Contributing
NOTE: For brevity sake, I described a process we can use to work with Git effectively but you are more than welcome to suggest changes (please suggest in Teams). Usually, people would have a develop branch but for this project scale I think it would make pull requests too slow.

Only people within the team project must contribute to this (unless this is expanded upon in the future). We can use a GitFlow process to categorise branches into features, refactoring, testing, bugfix etc.

For example, if you are creating a guidelines web page, you may name a branch like this:

### `feature/guidelines-page`

Or if you feel that the guidelines web page needs an overhaul (e.g. guidelines need changing), you can do something like this:

### `refactoring/guidelines-page`

We use "feature" to indicate that a branch is there to implement a feature or "testing" to indicate that we are writing unit tests and vice versa. For this project, we will be doing any sprint work based off a "release" branch (e.g. release/sprint-2) which must be merged into a "main" branch. The reason we have release branches is so that we can keep track of where the product is up to for each release (we can omit this if it proves to be overcomplicated).

### Workflow
Do some work (e.g. create HTML file) --> Make a Git commit --> Push to branch --> Make a pull request to pull branch content into a release branch --> Remove worked-upon branch once pulled --> Make a pull request to merge release branch into "main" (this should represent an MVP)

Note that you should make a pull request once you have finished with that branch (e.g. you have finished creating a guidelines page so you make a pull request for feature/guidelines-page or you finished refactoring validation code for submitting details so you make a pull request for refactoring/submission-form).

## How to use Git
I personally recommend using a desktop client such as GitHub Desktop if you are new to Git (another option is SourceTree) as it will simplify the process and lessen the learning curve. You can also use Git within IDEs like Visual Studio or Git in the command line if you want. Feel free to ask for help if you are stuck on using Git.
