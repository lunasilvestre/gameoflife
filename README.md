# Conway's Game of Life

This is an implementation of Conway's Game of Life in Python using `numpy` and `matplotlib` for visualization. The game is a zero-player game, where the evolution of the grid is determined by its initial state and a set of simple rules. 

This implementation allows you to:
- Select the size of the grid.
- Choose predefined patterns (like a glider, block, or blinker).
- Set the number of iterations and the speed of the animation.
- Initialize the grid randomly if no pattern is selected.

## Requirements

- Python 3.x
- `numpy` and `matplotlib` libraries

To install the dependencies, you can run:

```
pip install -r requirements.txt
```

## Usage

### Running the Game

You can run the game using the command line with various options:

```
python game_of_life.py --size SIZE --pattern PATTERN --iterations ITERATIONS --speed SPEED
```

- `--size`: Define the size of the grid (NxN), where `SIZE` is an integer (default is 20).
- `--pattern`: Choose a predefined pattern. Available options are `glider`, `block`, and `blinker`.
- `--iterations`: Number of iterations for the game (default is 100).
- `--speed`: Speed of the animation in milliseconds (default is 200).

### Example Commands

#### Running with a predefined pattern (glider) on a 30x30 grid:

```
python game_of_life.py --size 30 --pattern glider --iterations 200 --speed 100
```

#### Running a random grid with 40x40 size:

```
python game_of_life.py --size 40 --iterations 150 --speed 200
```

## Predefined Patterns

- **Glider**: A small pattern that moves diagonally across the grid.
- **Block**: A 2x2 still-life pattern.
- **Blinker**: A simple oscillator pattern.

## Project Structure

- `game_of_life.py`: The main script for running the simulation.
- `README.md`: This file, with instructions on how to run and use the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `requirements.txt`: The list of dependencies for the project (only if using pip).

