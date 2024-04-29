[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14913552&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Tower Rescue: Dodge the Witch's Apples
<<<<<<< HEAD
## CS110 Final Project  << Semester, Year >>

## Team Members

Carol Zhang and Ashley Mera
=======
## CS110 Final Project   Spring, 2024 

## Team Members

Carol Zhang
Ashley Mera
>>>>>>> 91c5c063d48bd00b93de46207dc3b77a5dd33519

*** 

## Project Description

<<<<<<< HEAD
There is a girl at the tower that needs to be saved and the player must get up to the tower without being hit by apples by the evil witch. 
=======
For this project, there will be a girl in a tower that needs to be saved. Your character is supposed to save the girl but there is a evil witch at the top of the tower with the girl.Your objective is to save the girl by climbing the tower while apples are being thrown at you by the witch and getting to the top of the tower.
>>>>>>> 91c5c063d48bd00b93de46207dc3b77a5dd33519

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features


1. "Press start to win
2. Prince
3. The witch with her apples
4. Tower moving with clouds
5. "Congrats you saved her"
=======

### Classes
Character class: represents the main characters and the character can move in various directions and perform actions like jumping 
Tower class: represents the tower and checks for collisions with the character to determine if the character has reached the top 
Witch class: the witch can throw apples at the character
Apple class: represents the apples thrown and the apples move downward and can 

- Character Class: Represents the main character of the game, tasked with saving the girl from the tower. The character can move in various directions and perform actions like jumping.
- Tower Class: Represents the tower where the girl is held captive. It checks for collisions with the character to determine if the character has reached the top of the tower.
-Witch Class: Represents the evil witch at the top of the tower. The witch can throw apples at the character.
-Apple Class: Represents the apples thrown by the witch. The apples move downward and can collide with the character.
- Controller Class: Manages the game loop, handles events, updates game logic, and controls the flow of the game.


## ATP
TEST CASE 1: Player Movement 
Test Description: Verify that the player can move left, right and up.
Test Steps:
1. Start the game
2. Press the left key
3. Verify the player moves left
4. Press the right key
5. Verify the player moves right
6. Press the Up key
7. Verify the player moves up

TEST CASE 2: Collision detected
Test Description: Ensure that collisions between the player's bullets and enemy ships are detected correctly.
Test Steps:
1.Start the game.
2.Fire the apple towards the prince
3.Verify that the apple hits the prince
4.Fire a player's apple that misses the prince
Verify that no collision is detected.

TEST CASE 3: Menu Navigation 
Test Description: Test the navigation through the game's menu 
Test Steps: