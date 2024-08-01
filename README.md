# Battleship Game

## Contents

* [User Experience (UX)](#user-experience-ux)
    * [Initial Discussion](#initial-discussion)
    * [Client Goals](#client-goals)
* [Design](#design)
    * [Game Mechanics](#game-mechanics)
    * [User Interface](#user-interface)
    * [Interaction](#interaction)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment--local-development)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
        * [How to Fork](#how-to-fork)
        * [How to Clone](#how-to-clone)
* [Testing](#testing)
* [Credits](#credits)
    * [Code Used](#code-used)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgments](#acknowledgments)

## User Experience (UX)

### Initial Discussion
In Project 3, I programmed a game called **"Battleship."**  
This simple Battleship game differs from traditional versions as players have a limited number of bullets to take down computer ships randomly placed by the computer.

**Live Project:** [Play on Heroku](https://battleships-game10-cdec97573350.herokuapp.com/)

### Client Goals
- **User**: Should be able to play the game without prior knowledge of it. 

### First-time Visitor Goals
- **Find out** how the game works.
- **Win** against the computer.

---

## Design
The game is programmed in Python to run in a terminal. As it is text-based, it features no visual design.

## Features
- **Game Start:** Players begin with a certain number of bullets to target the enemy ships. Instructions on what to do are displayed.

    ![Game Start](assets/testing/images/player-choice.png)

- After the computer places its ships, a game description is shown, and the game starts automatically.
  
- Initially, the player selects a column (e.g., A-3) to guess where the computer's ships are positioned.

    ![Game Start Selection](assets/testing/images/ingame.png)

- Upon hitting a ship, a hit message is displayed:

    ![Hit Message](assets/testing/images/ingame-hit.png)

- Missing a ship results in a miss message:

    ![Miss Message](assets/testing/images/ingame-miss.png)

- Winning the game triggers a "You win" message:

    ![You Win](assets/testing/images/win.png)

- Losing the game displays a "You lose" message:

    ![You Lose](assets/testing/images/loose.png)

Upon finishing, the game ends.

---

### Game Mechanics
- Players choose how many bullets they want.
- Players guess to target the computer's ships.
- The game tracks remaining bullets and ships for both players.
- The game concludes when a player sinks all opponent's ships or runs out of bullets.

### User Interface
- The game utilizes a simple, text-based interface in the terminal.
- Players can view their board and track their bullets.
- The computer's board is also visible for tracking hits and misses.

### Interaction
- Players interact with the game by inputting coordinates for their guesses.
- Clear messages are provided for hits, misses, and game outcomes.

## Technologies Used
- **Python:** The programming language employed for game development.

## Languages Used
- **Python:** The primary language used for coding the game.

## Frameworks, Libraries & Programs Used
- **Gitpod:** Code editor utilized for development.
- **Git & GitHub:** Tools for version control and project collaboration.
- **Heroku:** Platform for final deployment.

### List of Potential Improvements
1. **Difficulty Levels:** Implement varied difficulty settings (Easy, Medium, Hard).
2. **Ship Types and Sizes:** Introduce different ship categories with distinct sizes and special attributes.
3. **Game Modes:** Add single-player mode and multiplayer support.
4. **Visual Enhancements:** Create a GUI using libraries like Pygame or Tkinter.
5. **Sound Effects and Music:** Incorporate sound effects for hits and game events.
6. **Power-Ups or Special Abilities:** Introduce power-ups for players.
7. **Game Statistics:** Track and display detailed stats after each game.
8. **Save and Load Game Functionality:** Allow players to resume games later.
9. **Tutorial or Help Menu:** Guide new players through rules and gameplay mechanics.
10. **Leaderboard:** Display high scores and win/loss records.
11. **Mobile or Online Version:** Adapt the game for mobile platforms or create a web version.
12. **Enhanced Input Validation:** Handle unexpected inputs gracefully.
13. **Achievements or Badges:** Unlock achievements through specific challenges.
14. **Hints/Clues Mechanism:** Allow players to receive hints about nearby ships.
15. **Customizable Game Settings:** Let players customize game parameters before starting.
16. **Story Mode:** Incorporate a narrative-driven mode with missions and challenges.

## Deployment & Local Development

### Deployment
The game is designed for local play in a terminal environment. It was developed through Gitpod, with comprehensive documentation pushed to GitHub.

#### GitHub
1. Log in (or sign up) to GitHub.
2. Navigate to the project repository.
3. Click on the **Settings** link.
4. Click on the **Pages** link in the left-hand navigation bar.
5. In the **Source** section, select **main** from the drop-down menu and **Root** from the drop-down folder menu.
6. Click **Save**. Your live GitHub Pages site is now deployed.

#### Heroku
1. Log in or register on Heroku.
2. Click on **New** in the dashboard and select **Create New App**.
3. Choose an app name and region, then click **Create app**.
4. Go to **Settings**, add a Config Var with Key = PORT and Value = 8000.
5. Add buildpacks: Python followed by Node.js.
6. Click on **Deploy**, select **GitHub**, and connect to your repository.
7. Click **Deploy Branch** to build the app.
8. After successful deployment, click on **View** to see the deployed site.

### Local Development

#### How to Clone
1. Log in (or sign up) to GitHub.
2. Go to the repository, **MrHaJu/Code-Institute-Projekt-3-PYTHON-battleship**.
3. Click the **Code** button, and copy the HTTPS, SSH, or GitHub CLI link.
4. Open the terminal in your code editor, navigate to the desired directory.
5. Type `git clone`, paste the copied link, and press Enter.

## Testing
Please see the [testing.md](testing.md) file for comprehensive testing information.

---

## Credits

### Code Used
- [W3 Schools](https://www.w3schools.com/) for solutions and code improvements.

### Content
- This README template was adapted from the Code Institute README template.

### Media
- No media is used in this text-based game.

### Acknowledgments
- Special thanks to [Vernell](https://github.com/VCGithubCode/) for guidance and support during project development.