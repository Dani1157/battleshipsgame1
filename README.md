battleships game

 ## Contents

* [User Experience (UX)](#User-Experience-(UX))
    * [Initial Discussion](#Initial-Discussion)
    * [Client Goals](#Client-Goals)

* [Design](#Design)

  * [Wireframes](#Wireframes)
  * [Features](#Features)
  * [Accessibility](#Accessibility)
  * [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages-Used)
  * [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)

* [Deployment & Local Development](#Deployment-&-Local-Development)
  * [Deployment](#Deployment)
  * [Local Development](#Local-Development)
    * [How to Fork](#How-to-Fork)
    * [How to Clone](#How-to-Clone)

* [Testing](#Testing)
    
* [Credits](#Credits)
  * [Code Used](#Code-Used)
  * [Content](#Content)
  * [Media](#Media)
  * [Acknowledgments](#Acknowledgments)
  
  ## User Experience (UX)

### Initial discussion
In project 3 I programmed a game called "Battleship".
The game is a simple  Battleship game. But this time it's a little different The player has a certain amount of bullets To take down the computerships That are randomly placed By the computer.

User stories
#### Client goals

The user should be able to play the game without any knowledge of the game

#### First-time visitor goals
I want to find out how the game works
I want to win against the computer
---

Design
The game was programmed in Python to use the terminal. Since the game is text-based, it has no real design

Features
Game Start, Player has a certain amount of bullets to Tack down the enemy ships. A small instruction of what to do is shown.

![Game Start, Player has to place Certain amount of bullets](assets/testing/images/player-choice.png)

After The computer Places all there ships, there is a description of the game. The game starts automatically.

At first, the player has to choose a column A-3

![Game start: Player has to choose a column A-H to guess where the Computer ships are ](assets/testing/images/ingame.png)


If the player hits a computer ship, it will be pointed out with a hit message.

![In the game, the player hits a computer ship](assets/testing/images/ingame-hit.png)

If the player misses a computer ship it shows the miss message.

![In the game, the player misses a computer ship](assets/testing/images/ingame-miss.png)

If the player wins the game, the game shows the "You win" message as shown in the image below:

![Player wins the game](assets/testing/images/win.png)

If the player loses the game, the game shows the "You loose" message:

![Player looses the game](assets/testing/images/loose.png)


After win, loss , the game ends.

---

#### Game Mechanics

The game lets the player Choose How many bullets they want.
The player can make guesses to target the computer's ships.

The game keeps track of the remaining bullets and ships for both the player and the computer.
The game ends when the player sinks all the opponent's ships or when the bullets run out.

#### User Interface
The game is played in the terminal, providing a simple and text-based user interface.
The player is shown their board with their Number of bullets.
The player can see the computer's board to track their hits and misses.
#### Interaction
The player can interact with the game by inputting coordinates for their guesses.
The game provides clear messages for hits, misses, and game outcomes.

#### Technologies Used

Python: The programming language used to build the game logic.

#### Languages Used

Python: The main language used for programming the game.

#### Frameworks, Libraries & Programs Used

Gitpod: The code editor used for development.
Git & GitHub: Used for version control and project collaboration.
Github - To save and store the files.
Heroku for final deployment.

Deployment & Local Development
#### Deployment

The game is designed to be played locally in a terminal environment.

The third project was developed through Gitpod, using the template provided by Code Institute. Every step was documented and pushed thoroughly via GitHub.

#### Github
Login (or sign up) to Github.
Find the repository for this project, 
Click on the Settings link.
Click on the Pages link in the left-hand side navigation bar.
In the Source section, choose main from the drop-down select branch menu. Select Root from the drop-down select folder menu.
Click Save. Your live Github Pages site is now deployed at the URL shown.cal machine.

#### Heroku

Log in or register a new account on Heroku
Click on 'New' in the dashboard and select 'Create New App'
Select a name for the app and choose your region.
Click on "Create app"
When the app is created click on Setting
To improve compatibility with various Python libraries add Config Var with Key = PORT and the Value = 8000
Add 2 buildpacks: Python and then Nodejs in this specific order
Go back at the top and click on "Deploy" and select "GitHub"
Scroll down and click on 'Connect to GitHub'
Search for your GitHub repository name by typing it
Click on "Connect"
Scroll down and click on "Deploy Branch"
You will see a message "The app was successfully deployed" when the app is built with python and all the depencencies
Click on view and you will see the deployed site

#### Local Development

##### How to Clone

Login (or sign up) to GitHub.
Go to the repository for this project, MrHaJu/Code-Institute-Projekt-3-PYTHON-battleship.
Click on the code button, select whether you would like to clone with HTTPS, SSH, or GitHub CLI, and copy the link shown.
Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## **Testing**

Please view the [testing.md](testing.md) file for more information on the testing undertaken.

- - -

## Credits

#### Code Used

* [W3 schools to find ways to solve problems and improve the code](https://www.w3schools.com/)

#### Content

* The README template was adapted from the Code Institute README template.


#### Media

* No media is used in this text-based game.

### Acknowledgments

* Special thanks to [Vernell](https://github.com/VCGithubCode/) for providing guidance and support during the development of this project.
