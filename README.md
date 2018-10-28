# task3
Finding of the shortest way in the labyrinth
## How to use the program:
* if you don't have "colorama" library, please install it:
  * `pip intstall colorama`
* enter the structure of labyrinth in the file "maze.txt". Note that free area should be marked as **'.'** and the obstacles with **'#'**. By default, this file contains the labyrinth example given in the task;
* run main.py. By doing this, the maze will be read from file and checked for permeability. If this ckeck returns True, the length of the shortest way will be counted, this way will be marked with stars and the labirynth with shortest way will be printed. If the check returns False, message about it will be printed.
______________________________________________

## Description of files:
* sources.py : contains fuctions for checking permeability, finding the shortest path with the adaptation of A* method and beautiful output of the maze :) ;
* maze.txt : contains the original labyrinth;
* main.py : executable file.
