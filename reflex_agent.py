import random

grid=[
    [0,0,0,1],
    [0,1,0,0],
    [0,0,0,1],
    [1,0,0,'G']
]

def is_valid(pos):
    x,y=pos
    return 0<=x<len(grid)and 0<=y<len(grid[0])and grid[x][y]!=1

def reflex_agent(start,goal):
    pos=start
    path=[pos]
    moves=[(-1,0),(1,0),(0,-1),(0,1)]

    while pos!=goal:
        x,y=pos
        best_moves=None
        best_dist=float('inf')
        print(best_dist)
        for dx,dy in moves:
            new_pos=(x+dx,y+dy)
            if is_valid(new_pos):
                dist=abs(new_pos[0]-goal[0])+abs(new_pos[1]-goal[1])
                if dist<best_dist:
                    best_dist=dist
                    best_move=new_pos


        if best_move is None:
         valid=[(x+dx,y+dy)for dx,dy in moves if is_valid(x+dx,y+dy)]
         if not valid:
            print("Agent is stuck")   
            return 
         best_move=random.choice(valid)   
        pos=best_move
        path.append(pos)
    return path

start=(0,0) 
goal=(3,3)
path=reflex_agent(start,goal)                  
print(path)