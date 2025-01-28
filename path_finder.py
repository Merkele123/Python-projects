import curses
from curses import wrapper
import queue
import time

# Maze layout: "#" represents walls, "O" is the starting point, "X" is the end point, and " " represents open paths
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", "#", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", "#", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", "#"],
    ["#", " ", " ", " ", "#", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "X", "#"],
]

# Function to print the maze, coloring path and maze cells
def print_maze(maze, stdscr, path=[]):
    # Initialize color pairs for maze cells and path cells
    BLUE = curses.color_pair(1)  # Blue for regular maze cells
    RED = curses.color_pair(2)   # Red for the path cells

    # Loop through each row and column in the maze
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:  # If the current cell is part of the path, print it in red
                stdscr.addstr(i, j * 2, "X", RED)  # Print path as 'X'
            else:  # Otherwise, print the regular maze cells
                stdscr.addstr(i, j * 2, value, BLUE)  # Print regular cells as they are

# Function to find the starting position ('O') in the maze
def find_start(maze, start):
    for i, row in enumerate(maze):  # Loop through rows of the maze
        for j, value in enumerate(row):  # Loop through each column
            if value == start:  # If we find the starting point 'O', return its coordinates
                return i, j
    return None  # Return None if 'O' is not found (shouldn't happen)

# Function to find the shortest path from 'O' to 'X' using Breadth-First Search (BFS)
def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)  # Find the starting position in the maze

    q = queue.Queue()  # Create a queue for BFS
    q.put((start_pos, [start_pos]))  # Enqueue the start position with an initial path

    visited = set()  # Set to track visited positions

    # Begin BFS loop
    while not q.empty():
        current_pos, path = q.get()  # Get the current position and path from the queue
        row, col = current_pos

        # Clear the screen and print the maze with the current path
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.1)  # Sleep to slow down the process and visualize the pathfinding
        stdscr.refresh()

        # If we reach the end, return the path
        if maze[row][col] == end:
            return path

        # Get the neighboring cells (up, down, left, right) of the current position
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:  # Skip if the neighbor has already been visited
                continue

            r, c = neighbor
            if maze[r][c] == "#":  # Skip if the neighbor is a wall
                continue

            new_path = path + [neighbor]  # Create a new path by adding the neighbor
            q.put((neighbor, new_path))  # Enqueue the new neighbor with the updated path
            visited.add(neighbor)  # Mark the neighbor as visited

    return []  # Return an empty list if no path is found (shouldn't happen)

# Function to get the valid neighbors (up, down, left, right) of a given cell
def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:  # If the current cell has a valid neighbor above
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # If the current cell has a valid neighbor below
        neighbors.append((row + 1, col))
    if col > 0:  # If the current cell has a valid neighbor to the left
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # If the current cell has a valid neighbor to the right
        neighbors.append((row, col + 1))

    return neighbors

# Main function where the game is run
def main(stdscr):
    # Initialize the color pairs for the maze
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # Find the path from 'O' to 'X'
    path = find_path(maze, stdscr)
    
    # Display a message if the path is found or not
    if path:
        stdscr.addstr(10, 0, "Path found!")  # If a path is found, display the message
    else:
        stdscr.addstr(10, 0, "Path not found!")  # If no path is found, display the message

    stdscr.getch()  # Wait for a key press before exiting

# Start the curses application
wrapper(main)
