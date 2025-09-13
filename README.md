# AI_MIDTERM_TP_JARILLA
Pick your use-case (e.g. map navigation, puzzle game, etc) and develop an A* search program

## Overview
This project demonstrates the **A* search algorithm** in Python using a simple **grid-based navigation example**. The A* algorithm finds the **shortest path** from a start point to a goal while avoiding obstacles.

## Features
- Grid-based map representation (`0 = free cell`, `1 = obstacle`)  
- Manhattan distance heuristic for estimating path cost  
- Finds the shortest path from start to goal  
- Handles obstacles and avoids revisiting cells  
- Easy to modify: change grid size, start, and goal  

## Usage
1. Open `astar_demo.py` (or the main script file).  
2. Modify the `grid`, `start`, or `goal` if you want a custom map.  
3. Run the program:
   - In Visual Studio: Press **Ctrl + F5**  
   - Or in terminal:
     ```bash
     python astar_demo.py
     ```  
4. The program prints the **path from start to goal** as a list of coordinates.
5. 
## How It Works
- **Open Set**: A priority queue containing cells to explore, prioritized by total cost (`g + h`)  
- **Heuristic Function**: Estimates the distance from a cell to the goal (Manhattan distance)  
- **Neighbors**: Checks all adjacent cells (up, down, left, right)  
- **Path Tracking**: Stores the path taken to reach each cell  

## Recording
You can watch a demo recording of the program here:  
https://drive.google.com/drive/folders/1p2axbzWlbWJvswXadpnvAdhvQxawM1-G?usp=sharing
