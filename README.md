[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14913552&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Tower Rescue: 
## CS110 Final Project   Spring, 2024 

## Team Members

Carol Zhang
Ashley Mera

*** 

## Project Description

Tower Rescue. For this project, there will be a girl in a tower that needs to be saved. Your character is supposed to save the girl but there is a evil witch at the top of the tower trying to chase you. This is a 2 player game so either person can win. The witch will win if she gets the prince before he can catch Rapunzel and the prince will win if he gets to Rapunzel without getting caught.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features
1. "Press start"
2. Moving characters
3. Witch with her apple
4. Tower background
5. "You win!"
=======

### Classes
Character class: represents the main characters and the character can move in various directions and perform actions like jumping 
Tower class: represents the tower and checks for collisions with the character to determine if the character has reached the top 
Witch class: the witch can throw apples at the character

- Character Class: Represents the main character of the game, tasked with saving the girl from the tower. The character can move in various directions and perform actions like jumping.
- Tower Class: Represents the tower where the girl is held captive. It checks for collisions with the character to determine if the character has reached the top of the tower.
-Witch Class: Represents the evil witch at the top of the tower. The witch can chase the prince and when they collide the witch will win.
-Apple Class: Represents the apples that is used with the witch.
-class StartMenu: Allows buttons to play 
-class Highscore: Keeps track of time
-class Clouds: extra decorations for visuals
-class Rapunzel: The person who needs to be saved, if touched by prince, game is won.
-class button: Allows retry 


- Controller Class: Manages the game loop, handles events, updates game logic, and controls the flow of the game.


## ATP

TEST CASE 1: Player Movement for the Prince
Test Description: Verify that the player can move left, right and up.
Test Steps:
1. Start the game
2. Press the left arrow key on keyboard
3. Verify the player moves left
4. Press the right key arrow key on keyboard
5. Verify the player moves right
6. Press the Up key arrow key on keyboard
7. Verify the player moves up
Expected Outcome: The player should move left, right or up using keyboard keys.

TEST CASE 2: Player Movement for the Witch
Test Description: Verify that the player can move left, right and up.
Test Steps:
1. Start the game
2. Press "1" on keyboard to move left
3. Verify the player moves left
4. Press "2" on keyboard
5. Verify the player moves right
6. Press "4" on keyboard to move down
7. Verify the player moves down
8. Press "3" on keyboard to move up
9. Verify the player moves up 
Expected Outcome: The player should move left, right or up and down using keyboard numbers.


TEST CASE 3: Collision detected
Test Description: Ensure that collisions between the witch and prince are detected correctly. You are playing the witch (Keys for witch are 1 and 2, to move left and right and 3, 4 are to move up and down check test case 2 for verification)
Test Steps:
1.Start the game.
2. If you are playing the witch, chase the prince until collistion 
3.Verify that the witch with apple hits the prince. It will say "Game Over"
4. If you are playing with prine, move the prince until he arrives to rapunzel
5. Verify that no collision is detected. The prince will win and screen will say "you win!"
Expected Outcome: Collision of characters should determine winning or losing outcome.



TEST CASE 4: Win/Lose Navigation
Test Description: Test the navigation through the game's menu 
Test Steps:
1. Run the Game
2. Check to see if a "play button" appears
3. Click "PLAY"
4. Verify that game begins
5. Play the game 
Expected Outcome: The beginning button should start the game

TEST CASE 5: Game Over/Retry Condition
1. Start the game
2. Play the game
3. If playing prince, get hit by witch
4. Verify that game displays "Game Over"
5. Click "retry"
6. Verify you can play again
7. If playing prince, get to rapunzel
8. Verify that game displays "You win"
9. Click "retry"
10. Verify you can play again

Expected Outcome: The game should display a message when the player loses or winsand you should get the option to play again.