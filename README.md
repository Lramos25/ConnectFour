# ConnectFour

Many people I respect advise to have at least one game included in a portfolio. Working on a simple game is a great way to continue to practice planning out a project before sitting down to code. Because I want it to be a project that matters to me I have decided to work on the game Connect Four. I have many fond memories of Connect Four from my childhood. Without bragging too much, I was unofficially  the undisputed neighborhood champion for our unsanctioned friends and family group. I know, sounds unbelievable but it is true. In all seriousness, looking back I can say that connect four is what sparked my competitive nature. My friends wanted to keep playing against me because I did not lose much. They hated when I won and I laughed at them for falling into my traps. Even though this is a small group of unskilled sixth graders playing a fairly simple game, I learned a lot about the work it takes to get to the top and how much more work it takes to stay there. What better project can then one that helped me to understand the importance of dedicated work.


I have made tic tac toe applications for some classes so the general idea is not new to me. In this case, I would like to incorporate a GUI and work to make this feel like actually playing the game. There are three main phases to the game: Set up, game play, checking for a connect four and the flow of each game is as follows:

1)	Set up game (blank board and pieces separated to each player)
2)	Player one picks a column to drop piece in
3)	If player one has four in a row then player one wins
4)	If player one did not win, then player two takes their turn
5)	Player two picks a column to drop a piece in
6)	If player two has four in a row then player two wins
a.	Repeat 2-6 until a player wins
7)	Once a player has four pieces in a row, that player is declared the winner and the game is ended

 

Details to consider during development:


**Set up the game:**
	
  The game board is a blue color grid with 7 columns and 6 rows.
	
  Player pieces are red and yellow 
  
**Gameplay:**
	
  The current player selects the column to drop their piece in. The piece will fall down until it it reaches the end of that column. A column end is ether at the bottom row or another piece occupies the next bottom spot. Only one piece may occupy each spot. Once a piece occupies a spot, the creates a block and makes the next higher spot a new end. The below visual demonstrates these two cases.
 
 
 visual here


**Check for winner:**

Checking horizontal, vertical is a straight forward process:
	Checking horizontal: increment column count by one 
	Checking vertical: increment row count by one

Checking diagonal for wins is a bit different:

Checking diagonal up: increment column count by one, increment row count by one
		
   Checking for diagonal wins that go from one point then move up only need to be checked at specific points. It is not possible for this win to happen if the checks are all in the last 3 columns or last three rows. At least one check will have to be within the first four columns and first three rows (visual below). Some instances do not need to be checked – such as a play at 0,0 – but excluding these will add another layer of complexity and provide no functionality.
    
    
 visual here


Checking diagonal down: decrement column count by one, increment column count by one

Checking for diagonal wins that go from one point then move down follow a similar logic but applied differently as it is the opposite of the previous check.  

**Once a winner is found the game should end and winning message should appear without deleting the game state.**

**Problems encountered when testing that required a little bit more than just reviewing the code:**

1) Game window wont close when selecting the close button (red x)
	Issue resolved by adding pygame.quit() before the sys.exit()

2) ame window not closing automatically once a player wins
  Issue resolved by adding pygame.quit() before the sys.exit() –

3) Piece will start as correct color, but as the mouse cursor moves the color changes from red to yellow. Seems to happen at the start and end of each column.
	Issue resolved by updating the board display after the conditional check on mouse movement


**Lessons learned:**

This was not difficult to start with, but I had a very good idea of what needed to happen at each stage. When I started to include the graphics I ran into some minor issues that required me to keep referencing the documentation or searching for answers in other ways. Most of the smaller problems I encountered had to do with the graphics and mechanics of listeners (such as with mouse motion). It was nice to use various methods and even some trial and error to resolve the problems.


**Final thoughts:**

Overall the project is not very difficult and has been done more times than I can count. I am sure there are many out there that look similar and many others that have been done very different – but I am happy with this for now. Possible upgrades would include an AI to play with, menu system to select the number of players and enter in names to use for each, asking to play again at the end of each game instead of quitting the application.
