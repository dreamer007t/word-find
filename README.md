# word-find

clone and run using command "python <file-name>".

The program is a single-player word game, where the user enters as many words as they are able to think of using a selection of 9 letters. The user can play the game in “easy mode” or “hard mode”.
The program first selects 9 letters of the alphabet at random. The same letter can appear multiple times, and the selection process uses the frequency of letters in the game of Scrabble when choosing letters, so that the 9 letters chosen are more likely to contain letters that are common in English words, e.g. the letters are much more likely to contain “E”, “I” or “A” than “Z”, “Q” or “X”.
The program displays the 9 letters in a 3x3 grid and prompts the user for input:
Note: The grid is only for presentation – words do not need to be made up of adjoining letters.
When prompted for input, the user has the following options (these should not be case-sensitive):
1. Enter a word, e.g. “TRAY” would be a valid word given the letters pictured above.  The program will check that the word is valid and award points to the user if it is.
2. Enter “S” to randomly re-order the letters.
 This is just to help the user think of more words, by seeing the letters in a new layout.
3. Enter “L” to display a list of the words that they have already entered during this game.
4. Enter “E” to end the game.
The program shows the grid of letters and prompts the user for input until they enter “E” to end the game. This allows them to keep entering words, shuffling the letters and viewing the list of words until they cannot think of any more words to enter, and choose to end the game.
Whenever the user enters a word, the program needs to check that:
1. The word has a minimum length of 3 characters.
2. The word has not already been used in this game.
3. The word is made up of the letters selected in this game.
4. The word is a recognised English word.
 Semester 2, 2019 CSI6208 Assignment 2 Page 3
 If the word is not valid, the program displays a message telling the user which piece of criteria was not met. If the game is being played in “hard mode”, this causes the game to end immediately. If the game is being played in “easy mode”, the program simply returns to the input prompt.
If the word is valid, the user is awarded points using the letter values in the game of Scrabble, where less common letters are awarded more points, e.g.
(3 points) (6 points) (10 points)
Note: The pictures of tiles are only to help you visualise how points are calculated – they do not appear in the game.
The program will use an online service provided by “Wordnik” to check if the word is a valid English word and to calculate the amount of points that it is worth. There will be a post on the Blackboard discussion board detailing this process, since it is not covered in the unit.
Once the user enters “E” to end the game, the program should show their final score.
If their score is at least 50, the program should congratulate the user and record a “log” of the game in a text file named “logs.txt”. Use the “json” module to read and write data from/to the text file in JSON format (see Reading 7.1). Each log of a game should be a dictionary consisting of three keys:
 “letters”:
 “words”:
 “score”:
the list of letters used in the game the list of words entered by the user the final score of the game
The logs should be stored in a list, resulting in the file containing a list of dictionaries. The example below demonstrates a list of two logs (the word list has been truncated to fit onto the page):
[
{
}, {
} ]
"letters": ["A", "A", "B", "D", "F", "I", "L", "O", "R"],
"words": ["AFRAID", "BALD", "BOAR", "BOLD", "DAB", "FAB", "FAIL", "FAR", ...], "score": 102
"letters": ["B", "D", "I", "J", "L", "N", "O", "O", "S"],
"words": ["BIN", "BINS", "BOLD", "BOLDS", "DIN", "DINS", "JOB", "JOIN", ...], "score": 76
JSON
The program should then show their final score, print “Thank you for playing!”, and end.
