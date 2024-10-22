import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

# Predefined patterns
patterns = {
    "glider": [
        [" ", "x", " "],
        [" ", " ", "x"],
        ["x", "x", "x"]
    ],
    "block": [
        ["x", "x"],
        ["x", "x"]
    ],
    "blinker": [
        ["x", "x", "x"]
    ]
}

# Convert the list of lists pattern to NumPy array
def list_to_grid(lst, size):
    grid = np.zeros((size, size), dtype=int)
    if lst is not None:
        pattern = np.array([[1 if cell == "x" else 0 for cell in row] for row in lst])
        # Center the pattern in the grid
        start_x = (size - pattern.shape[0]) // 2
        start_y = (size - pattern.shape[1]) // 2
        grid[start_x:start_x + pattern.shape[0], start_y:start_y + pattern.shape[1]] = pattern
    return grid

# Get all neighbors of a cell
def get_neighbors(cell):
    row, col = cell
    neighbors = [(row + i, col + j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]
    return neighbors

# Update grid using a 3x3 cursor around live cells
def update_grid_optimized(live_cells, grid_shape):
    from collections import defaultdict
    neighbor_count = defaultdict(int)
    
    # Count live neighbors for each live cell and its neighbors
    for cell in live_cells:
        for neighbor in get_neighbors(cell):
            if 0 <= neighbor[0] < grid_shape[0] and 0 <= neighbor[1] < grid_shape[1]:
                neighbor_count[neighbor] += 1
    
    new_live_cells = set()
    
    for cell, count in neighbor_count.items():
        if cell in live_cells:
            if count == 2 or count == 3:  # Live cells with 2 or 3 neighbors stay alive
                new_live_cells.add(cell)
        else:
            if count == 3:  # Dead cells with exactly 3 neighbors come to life
                new_live_cells.add(cell)
    
    return new_live_cells

# Convert live cells to grid
def live_cells_to_grid(live_cells, grid_shape):
    grid = np.zeros(grid_shape, dtype=int)
    for cell in live_cells:
        grid[cell] = 1
    return grid

# Function to animate the Game of Life
def animate(frame, img, live_cells, grid_shape):
    new_live_cells = update_grid_optimized(live_cells, grid_shape)
    new_grid = live_cells_to_grid(new_live_cells, grid_shape)
    img.set_data(new_grid)
    live_cells.clear()
    live_cells.update(new_live_cells)
    return img,

# Parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('--size', type=int, default=20, help='Size of the grid (NxN)')
    parser.add_argument('--pattern', type=str, choices=patterns.keys(), default=None, help='Choose a predefined pattern')
    parser.add_argument('--iterations', type=int, default=100, help='Number of iterations')
    parser.add_argument('--speed', type=int, default=200, help='Animation speed in milliseconds')
    return parser.parse_args()

# Main function to run the game
def main():
    args = parse_args()

    # Initialize the grid based on user input
    if args.pattern:
        grid = list_to_grid(patterns[args.pattern], args.size)
    else:
        # If no pattern, initialize a random grid
        grid = np.random.choice([0, 1], args.size * args.size, p=[0.8, 0.2]).reshape(args.size, args.size)
    
    live_cells = {(r, c) for r in range(grid.shape[0]) for c in range(grid.shape[1]) if grid[r, c] == 1}
    grid_shape = grid.shape

    # Set up the plot for the animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='binary', vmin=0, vmax=1)

    # Run the animation
    ani = animation.FuncAnimation(fig, animate, fargs=(img, live_cells, grid_shape), frames=args.iterations, interval=args.speed, save_count=50)
    plt.show()

if __name__ == '__main__':
    main()
