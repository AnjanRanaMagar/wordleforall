### How to Run this application?

Follow the following steps to run the application in your local machine. Please communicate with Anjan if you are making bid changes to the repo before pushing in remote repo.
## I made some edits in this file.

1. Clone the project into your local machine.
```git clone <link_of_repository>```<br>
Are you already working on the repository but your local repo is not upto date to the remote repo, you may need to rebase the local repo so your local repo is upto date to remote repo.
You can rebase by following the steps below:
    * a. Fetch the latest change from the remote repo:
    ```git fetch origin```
    * b. If you are not in main branch go to the main branch : ```git checkout main```
    * c. Merge the changes from remote branch:
    ```git merge origin/main```
    <br>
    If you see a conflict during a merge, let Anjan know or ignore for now. 
2. After 1st step is done and you have a upto date repository from a remote location, make sure your file has a following hirerchy. 
```
ist-300-team-2
    | instance
        db.sqlite
    | UI
    | PartC
    | WordleApp # this is our main project file.
        | static
        | templates
        __init__.py
        .gitignore
        auth.py
        current_user.txt # this is just for our team demo, only test-user is shown
        main.py
        models.py
        soft_requirements.txt #this has list of our software dependencies
    | notes.md
    | Readme.md

```
Note: The position of the file does not matter, however the hirerchy matters.

3. After verifying the data structure, you will need to install the requirements or dependencies for the wordleapp application to run. You will create a virtual environment in this step:

* Create a virtual env: Go to you 'WordleApp' directory (```cd /WordleApp```). When there run the following code:
```python3 -m venv auth```. Auth is our virtual environment name for this project. You can give other name. 

* Activate virtual env 'auth' : ```source auth/bin/activate```. Once the venv 'auth' is activate run following code to install those dependencies or flask packages. <br>
```pip3 install -r soft_requirements.txtx```. If this does not work, try googling on just install using: ```pip install flask flask-sqlalchemy flask-login flask-migrate```

Once the virtual env is activated, make sure you are in ist-team .. folder. In order to go back to previous folder use the command: ```cd ..```.

4. Run the flask app: To runt the flask, we need to specify our app is "WordleApp'. In order to do so use the following command:
```export FLASK_APP=WordleApp```.

    * Run flask: ``` flask run ```.
    Once it's running it's development server go to log in and try (current user login available in current_user.txt).
    Feel free to create a new user through signup.
<br>

Note: If you get some database or server issues, let me know through text or email. 
