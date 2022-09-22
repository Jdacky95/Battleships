# BATTLESHIPS

## Overview

This Game is Based on the classic game of Battleships but with a slight twist, where you have a limited  number of shots to take at the opposing fleet before you are overrun.

[You can read more about the original game here:](https://en.wikipedia.org/wiki/Battleship_(game))

[Click here to be taken to the final deployment of the project](https://battleships-jd.herokuapp.com/)

## How to play:

You are Given the opportunity to captain a ship in a ferocious battle where you input coordinates on the map to blindly target the opposing ships.

You have 15 shots to sink the 5 Ships of the opposition before they overrun you.

You must select A row coordinate between 0 and 7 and the same again for the Column coordinate, your crew will then fire on your instruction and mark on your map whether you have hit or missed their ships.

If you sink the opposing ships before you have run out of ammunition you are decalred the winner.

If you run out of ammunition you will undoubtedly be overrun and you will be declared the loser.

## Site Aims

1. Make it clear what the game involves without the need for explanation from external sources
2. To Run without error's and allow the player to play as many times as they like.
3. To be an enjoyable game that encompasses an opportunity to recieve and use inputs to recieve a users chosen Username and to increase playability.


## Features

* Inputs and validations
 * Accepts command to start the game from inital screen and will exit game upon command
 * Accepts player input for Captain name they would like to be reffered to as and is used in F strings through out to help personalise the game.
 * Accepts Coordinate inputs used to Mark Hit and misses on the board. Validation checks have been put in place to ensure that the same coordinate is not targeted more than once and that each input the player uses translates to a position on the board, if it does not the user will be asked to input a new entry.

* Random Number Generation
 * Random number generator from rand int used to automatically place opposing ships

* Turns and Ships left
 * I have declared a variable for the number of turns the user has left, this number goes down by one with every turn taken, if it hits zero, the    player loses the game. 
 * I have declared a variable for the number of ships that there are left on the board, this number goes down by one everytime a ship is hit and if the number reaches zero the player will be decalred the winner.

 ## Testing
 
 * The code has passed through PEP8 validator with no errors.
 * I've tested to see if all inputs into coordinates would either work on the board or produce a message to prompt a new input with clarified instruction. this includes inputs that are left blank. 
 * I have tested that my Restart/ new_game function would succesfully produce a new game without errors, I have fixed issue of My previous board being printed in the game as listed in bugs and fixes below.

 ## Bugs and Fixes

 * Python essential logged errors:
TypeError: list indices must be integers or slices, not str
when using user input to print hits on board:

Solved adding int() to input method

* Error:
 Didn't account for zero indexing in choosing coordinates so my ships and guesses would go over the scope of the board at the fringes.
 : Changed input range to between (0,7)

 * Upon deploying my project to Heroku I realised that when restarting the game with my new_game function the Board from the previous game would print and keep all of the previous selected Hits and misses. I had to reformat the code by changing the two boards from a global variable to a local variable in my run_game function.

 ## Deployment

 1. Click new in top right hand corner of Heroku and select create new app.
 2. Make unique App name and select region, then select create app.
 3. Navigate to settings tab and scroll to "Convig Vars"
 4. Click the button labelled "Reveal config vars" and the enter the "key" as port, the "value" as 8000 and click the add button.
 5. Scroll to the buildpacks section of the settings page, click "add buildpack" and select python save changes then do the same with node.js (make sure Python is the first buildpack in the list.)
 6. Select deploy tab at top of the page and select Github as the deployment method and confirm you want to connect to Github.
 7. Search for your repository name and and click the connect button.
 8. Click Deploy Branch in Manuel settings or select "Enable automatic deploys.


 ## Credits

 * I used the rand int random function from the code institute battleships video.

 * I used Stack overflow to help analyse mistakes in the code i was writing.

 *  I took inspiration from [Python Battleship with Object Oriented Programming](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=1406s) to help create my create ship function.

 * Wikipedia for clarifying the history and rules of battleships. 






