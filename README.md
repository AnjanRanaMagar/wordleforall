# ist-303-team-2

Team members: Roberta Vitale, Anjan Rana Magar, Chun Chen Lai

Concept for your application: Interactive Word Puzzle Challenge Application that promotes mental stimulations and interactive community among the players

Project stakeholders: Students and Faculty of the Claremont Colleges

Project requirements: User-friendly and clean interface, account registration, login interface and authentication, word puzzle or letters rearranging gameplay mechanics, score leaderboard.

### How to Run this application?

Follow the following steps to run the application in your local machine. 

1. Clone the project into your local machine.
```git clone <link_of_repository>```<br>
If you are already working in the repository but your local repo is not upto date to the remote repo, you may need to rebase the local repo so your local repo is upto date to remote repo.
You can rebase by following the steps below:
    * a. Fetch the latest change from the remote repo:
    ```git fetch origin```
    * b. If you are not in main branch go to the main branch : ```git checkout main```
    * c. Merge the changes from remote branch:
    ```git merge origin/main```
    <br>
    If you see a conflict during a merge, contact me (Anjan) for help.

2. After 1st step is done and you have a upto date repository from a remote location, make sure your file has a following hirerchy (order does not matter). 
```
ist-300-team-2
    | instance
        db.sqlite
    | migrations
    | UI
    | PartC
    | PartD
    | WordleApp # this is our main project file.
        | static
            | images
            app.js
            style.css
            ...
        | templates
            | base.html
            | index.html
            ....
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


**Part A** **(Meeting on 1/27)**
**Users stories:**

**User Registration and Authentication**
*As a new user, I want to register for an account using my email and password.
Estimated Completion Time: 1 week
*As a registered user, I want to log in securely using my credentials.
Estimated Completion Time: 1 week

**Profile Management**
*As a user, I want to create and update my profile with personal information.
Estimated Completion Time: 1 week

**Daily Puzzles and Leaderboard**
*As a user, I want to view the daily puzzle challenge to participate in.
Estimated Completion Time: 1 week days

*As a user, I want to see my current ranking on the leaderboard.
Estimated Completion Time: 3 days

**Gameplay Features**
*As a user, I want to play the interactive game where I guess words based on clues.
Estimated Completion Time: 1 week

*As a user, I want to earn points for correct guesses and progress through levels.
Estimated Completion Time: 4 days

**Settings and Preferences**
*As a user, I want to customize my game settings (e.g., difficulty level, sound).
Estimated Completion Time: 2 days

**Security and Privacy**
*As a user, I want assurance that my personal information and gameplay data are secure.
Estimated Completion Time: 3 days

**Responsive Design**
*I want a user-friendly interface that allows me to access the game seamlessly from my smartphone.
Estimated Completion Time: 5 days

**PART B** **(Meeting on 2/6, 2/13)**

**Tasks:**
**User Registration and Authentication**
1.Provide a login page with ability to create an account with user's email and password and authenticate them.
2.Able to make users to log in securely using users' credentials.

**Profile Management**
3.Provide a home page for users to see their profile and prepare for the game.
4.Allow users to view and update their own profile with personal information.

**Daily Puzzles and Leaderboard**
5.Provide the graphic user interface.
6.View the daily puzzle challenge to participate in.
7.Provide the rules of the game of how it supposed to be played.
8.Make players able to see current ranking on the leaderboard.

**Gameplay Features**
9.Allow users to play the interactive game where users guess the words based on clues.
10.Allow players to earn points for correct guesses and progress through levels.

**Settings and Preferences**
11.Allow users to customize their game settings (e.g., difficulties)

**Security and Privacy**
12.Make sure that users' personal information and gameplay data are secure.

**Responsive Design**
13.Provide a user-friendly interface that allows users to access the game seamlessly from their devices.

**Features will be in Milestone 1.0 of our project**
1.Working login page with ability to create account or sign in. (2 days)
2.Functional authentication mechanism.                          (2 days, along with Feature 1.)
3.Working home page with ability to view and edit users' account. (2 days)
4.Functional prompt button to start game.                       (1 day)
5.A preview version of the game.                                (4 days)

**Tasks allocation**
1.Front end: Roberta, Haifa
2.Back end: Anjan, Chun Chen Lai

**Burndown Chart**
![Team Project Burndown](https://github.com/MikeLaiGitHub/ist-303-team-2/assets/123436580/64be8eab-d054-4155-84a3-a186971d9fe8)

**Evidence of periodic meetings**
Meeting on February 6th: we decomposed the user stories shown in Part A into tasks, discussed the features of the application, and built the iterations for Milestone 1.0. We also assigned tasks to each group member.

Meeting on February 13th: we created a burn down chart that will allow us to track our work until completion of Milestone 1.0. We started to develop the application's code based on the chosen iterations.

Provide evidence in your github repository that you are meeting for periodic stand up meetings - your team should ideally meet at least twice a week.
Ensure that your development and testing environment is set up. Be sure to have some working functional (however rudimentary) and test code in your repository.

**PART C** **(Milestone1.0)**

Please refer to the folder named PartC for the Milestone1.0. The milestone includes details on Agile Methods used, Burndown charts, SiteMaps, etc.


**PART D** **(Milestone2.0)**

Please refer to the folder named PartD for the Milestone2.0.The milestone includes details on Agile Methods used, Burndown charts, SiteMaps, etc.

**Three Most Important learning outcomes** **(Milestone2.0)**

- Iterative development and continuous feedback to meet user expectations successfully

- Prioritization and adaptability, especially considering strict time constraints

- Cross-functional collaboration among team members with diverse skill sets
