N = 4
def print_new_maze( new_maze ): 
	
	for i in new_maze: 
		for j in i: 
			"""print(str(j) + " ", end ="") 
		print("")"""
def valid( maze, x, y ): 
	
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
		return True
	
	return False
def solveMaze( maze ): 
	new_maze = [ [ 0 for j in range(N) ] for i in range(N) ] 
	
	if new_maze_solution(maze, 0, 0, new_maze) == False: 
		print("no path"); 
		return False
	
	print_new_maze(new_maze) 
	return True
	

def new_maze_solution(maze, x, y, new_maze): 

	if x == N - 1 and y == N - 1: 
		new_maze[x][y] = 1
		return True

	if valid(maze, x, y) == True: 
		new_maze[x][y] = 1

		if new_maze_solution(maze, x + 1, y, new_maze) == True: 
			return True

		if new_maze_solution(maze, x, y + 1, new_maze) == True: 
			return True

		new_maze[x][y] = 0
		return False


#input
maze = [] 
mazeFile = open('input.txt', "r")
lines = mazeFile.readlines()
for line in lines:
    line = list(map(int, line.strip().split()))
    row = [c for c in line]
    maze.append(row)
#output
solveMaze(maze)
f = open('sample.txt','w')
f.write(str(maze))

