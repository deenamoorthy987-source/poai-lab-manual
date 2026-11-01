#Ex No: 2 IMPLEMENTATION OF DEPTH FIRST SEARCH ALGORITHM

#Dfs for Graph


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    graph[node] = []

    neighbour = input("Enter Neighbour of Node ").split()

    for neighbor in neighbour:
        graph[node].append(neighbor)


def is_valid(node):
    return node in graph


def dfs(current, visited, path):

    if current == goal:
        path.append(current)
        return True

    visited.add(current)

    neighbours = graph[current]

    for neighbour in neighbours:

        if is_valid(neighbour) and neighbour not in visited:
            if dfs(neighbour, visited, path):
                path.append(current)
                return True

    return False


start = input("Enter start node: ")
goal = input("Enter goal node: ")

visited = set()
path = []

if dfs(start, visited, path):
    path.reverse()

    print("\nDFS Path\n")

    for node in path:
        print(node)

else:
    print("No Path Found")


#DFS MAZE PROGRAM

maize_size=6

start=(0,0)
goal=(0,5)

obstacles={(0,1),(1,1),(4,1),(3,2),(4,2),(3,3),(4,3),(0,4),(3,4),(3,5)}

def is_valid(x,y):
  return (0<=x<maze_size and o<=y<maze_size and (x,y) not in obstacles)

def dfs(current,visited,path):
  if current==goal:
    path.append(current)
    return True

  visited.add(current)

  x,y=current

  directions=[(-1,0),(1,0),(0,-1),(0,1)]

  for dx,dy in directions:
    nx=x+dx
    ny=y+dy

    if is_valid(nx,ny) and (nx,xy) not in visited:
      if dfs((nx,ny), visited,path):
        path.append(current)
        return True
  return False

visited=set()
path=[]

if dfs(start,visited,path):
  path.reverse()

print("\nDFS Path\n")

for step in path:
  print(step)

print("\nMaze Representation\n")

for y in range(maze_size):
  for x in range(maze_size):
    if (x,y) == start:
      print("S",end=" ")

    elif (x,y) == goal:
      print("G", end=" ")

    elif (x,y) == obstacles:
      print("X",end=" ")

    elif (x,y) in path:
      print("*",end=" ")

    else:
      print(".",end=" ")
  print()

else: 
  print("No Path Found")

