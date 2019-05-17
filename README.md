# AI Project
### Bot which can play pacman using genetic algorithm.
# INSTALATION 
````
pip3 install pygame
````
# RUN
`````
python3 main.py 
`````
# RUN REPLAY(saved data)
`````
python3 main.py replay
`````

# CONFIG
 * SIMILATION_COUNT : min 0
 * GENERATION_SIZE : min 0
 * MUTATION_RATE : Beetween 0 and 1
 * RENDER_BEST_POPULATION_COUNT : min 0 max generation size

# ABOUT PACMAN
* GHOSTS MOVES
    * Pinky : Follow 4 tile front of pacman.
    * Clyde : Follow reverse position of pacman 4 tile front.
    * Blinky: Follow current position of pacman.
    * Inky :  Follow reverse current position of pacman.