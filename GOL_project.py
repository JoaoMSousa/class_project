import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 1
OFF = 0
vals= [ON, OFF]


def randomGrid(numCell):
    # a grid filled with random values porpotion 15% ON 85% OFF
    return np.random.choice(vals,numCell*numCell, p =[0.15 , 0.85]).reshape(numCell,numCell)

def addGlider(i,j,grid):
    """Adds a glider starting at the position (i,j)"""
    glider = np.array([[0,0,1],[1,0,1],[0,1,1]])
    grid[i:i+3, j:j+3] = glider

def addBeacon(i,j,grid):
    """Adds a beacon starting at the position (i,j)"""
    beacon = np.array([[1,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,1]])
    grid[i:i+4, j:j+4] = beacon

def addPulsar(i,j,grid):
    """Adds a pulsar starting at the position (i,j)"""
    pulsar = np.array ( [ [ 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
                        [ 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
                        [ 1,0,0,0,0,1,0,1,0,0,0,0,1],
                        [ 1,0,0,0,0,1,0,1,0,0,0,0,1],
                        [ 0,0,1,1,1,0,0,0,1,1,1,0,0],
                        [ 0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [ 0,0,1,1,1,0,0,0,1,1,1,0,0],
                        [ 1,0,0,0,0,1,0,1,0,0,0,0,1],
                        [ 1,0,0,0,0,1,0,1,0,0,0,0,1],
                        [ 1,0,0,0,0,1,0,1,0,0,0,0,1],
                        [ 0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [ 0,0,1,1,1,0,0,0,1,1,1,0,0]])
    grid[i:i+13, j:j+13] = pulsar

def addCross (i,j,grid):
    cross = np.array([[0,1,0],[1,1,1],[0,1,0]])
    grid[i:i+3, j:j+3]=cross
    #import ipdb; ipdb.set_trace()

def update(framNum, img, grid, numCell):
    metaGrid = grid.copy()
    for line in range (numCell):
        for coll in range (numCell):
            nrofneighbours = int((grid[line, (coll-1)%numCell] + grid[line,(coll+1)%numCell] +
                        grid[(line-1)%numCell, coll] + grid[(line+1)%numCell, coll] +
                        grid[(line-1)%numCell, (coll-1)%numCell] + grid[(line-1)%numCell, (coll+1)%numCell] +
                        grid[(line+1)%numCell, (coll-1)%numCell] + grid[(line+1)%numCell, (coll+1)%numCell]))

                        #Conway's rules
            if grid[line,coll] == ON:
                if (nrofneighbours < 2) or (nrofneighbours > 3):
                    metaGrid[line,coll] = OFF
            else:
                if nrofneighbours==3:
                    metaGrid[line,coll] = ON

    # update data
    img.set_data(metaGrid)
    grid[:] = metaGrid[:]
    return img


def main():
    parser = argparse.ArgumentParser(description="Game of Life SIM.")
    parser.add_argument('--grid-size', dest='size', required = False)
    parser.add_argument('--interval', dest = 'interval', required = False)
    parser.add_argument('--glider', action = 'store_true', required = False)
    parser.add_argument('--beacon', action = 'store_true', required = False)
    parser.add_argument('--pulsar', action = 'store_true', required = False)
    parser.add_argument('--cross', action = 'store_true', required = False)
    args = parser.parse_args()

# set defaul grid size and given number
    numCell = 32
    if  args.size and int(args.size)>=9:
        numCell = int(args.size)


# set animation update interval
    updateInterval = 1
    if args.interval:
        updateInterval = int(args.interval)

# declare grid
    grid = np.array([])
# check for glider, beacon, pulsar flag
## pattern = ['glider', '']
    if args.glider:
        grid = np.zeros(numCell * numCell).reshape(numCell,numCell)
        pixel = np.random.uniform(0,numCell,2)
        addGlider(int(pixel[0]),int(pixel[1]),grid)
    elif args.beacon:
        grid = np.zeros(numCell * numCell).reshape(numCell,numCell)
        pixel = np.random.uniform(0,numCell,2)
        addBeacon(int(pixel[0]),int(pixel[1]),grid)
    elif args.pulsar:
        grid = np.zeros(numCell * numCell).reshape(numCell,numCell)
        pixel = np.random.uniform(0,numCell,2)
        addPulsar(int(pixel[0]),int(pixel[1]),grid)
    elif args.cross:
        grid = np.zeros(numCell * numCell).reshape(numCell,numCell)
        pixel = np.random.uniform(0,numCell,2)
        addCross(int(pixel[0]),int(pixel[1]),grid)
    else:
#populates grid ramdomly 1/0 p=[0.15, 0.85]
        grid = randomGrid(numCell)

#animations init

    figure, ax = plt.subplots()
    image = ax.imshow(grid, interpolation = 'nearest')
    anim = animation.FuncAnimation(figure, update, fargs=(image, grid,numCell, ),frames = 60,
                                    interval = updateInterval, save_count=20)

    plt.show()

## Call to main
if __name__ == '__main__':
    main()
