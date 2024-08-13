'''
    File: dijkstr_on_grid.py
    Purpose: This project uses the dijsktra_node class that has been imported
                to find the distance from a starting point, through a maze
'''

from dijkstra_node import*

def map_array(file):
    '''
        args: file
        returns: 2D array of the whole maze 

        this function dycrypts a file and converts its information into a 2D
        array that represents a maze where each # is a node
    '''

    f = open(file)
    maze = []
    for i in f:
        row = []
        for ii in i:

            #adds a node in each spot a # is
            if ii == '#':
                row.append(DijkstraNode())
            elif ii == ' ':
                row.append(ii)
        maze.append(row)
    f.close()
    return maze

def print_maze(maze, mode):
    '''
        args: 2D array maze, and mode which is a string
        returns: None 

        This function prints out the maze based on which mode it is in
        if its in fill mode it prints out the finished maze, if in animate
        it prints out on each stage of it searching
    '''

    if mode == 'fill':
        for i in maze:
            for ii in i:
                if ii != ' ':
                    if ii.is_reached():
                        distance = ii.get_dist()

                        #if the distance is a single digit it prints a space before and after
                        if ii.get_dist() < 10:
                            print(' ' + str(distance) + ' ', end = '')

                        #if distance is above 10 it only prints a space after
                        else:
                            print(str(distance) + ' ', end = '')

                    #if it hasn't been reached it prints a #
                    else:
                        print(' # ', end = '')
                else:
                    print('   ', end = '')
            print()
        print()
    else:
        for i in maze:
            for ii in i:
                if ii != ' ':
                    if ii.is_reached():

                        #checks to make sure the node is done
                        if ii.is_done():

                            #if the distance is a single digit it prints a space before and after
                            if ii.get_dist() < 10:
                                print(' ' + str(ii.get_dist()) + ' ', end = '')

                            #if distance is above 10 it only prints a space after
                            else:
                                print(str(ii.get_dist()) + ' ', end = '')

                        #if it isn't done, then it prints a ? after
                        else:

                            #if the distance is a single digit it prints a space before and after
                            if ii.get_dist() < 10:
                                print(' ' + str(ii.get_dist()) + '?', end = '')

                            #if distance is above 10 it only prints a space after
                            else:
                                print(str(ii.get_dist()) + '?', end = '')
                    
                    #if it hasn't been reached it prints a #
                    else:
                        print(' # ', end = '')
                else:
                    print('   ', end = '')
            print()
        print()

def dijkstra_algorithm(maze, x, y, mode):
    '''
        args: 2D array maze, x and y coordinates as ints, and
                mode a string
        returns: None 

        This function is based on dijkstras algorithm and uses it to find
        the distance from the starting point to every accessable node in the
        maze
    '''

    distance = 1

    #initializes the todo list with the starting points value
    todo = [(0, x, y)]
    dist = [0]
    maze[y][x].update_dist(dist[0])
    while todo != []:
        next = todo[0]
        dist.pop(0)
        cur_x , cur_y = next[1], next[2]
        if mode == 'animate':
            print('CURRENT GRID: ')
            print_maze(maze, mode)
            if todo != []:
                print('TODO list: ' + str(todo))
                print()
        
        next = todo.pop(0)
        #updates the current node so it isn't visited again
        if not maze[cur_y][cur_x].is_done():
            maze[cur_y][cur_x].set_done()

        #next directions can only be up, down, left or right
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        #goes through all the neighbors of next
        for i in directions:

            #uses try and except to skip index out of range issues
            try:
                new_x, new_y = cur_x + i[0], cur_y + i[1]

                #only adds new nodes to todo list if they are not previously visited and valid locations
                if new_x >= 0 and new_y >= 0 and maze[new_y][new_x] != ' ' and maze[new_y][new_x].is_done() == False:
                    if not maze[new_y][new_x].is_reached():
                        todo.append((distance,new_x, new_y))
                        dist.append(distance + 1)
                        maze[new_y][new_x].update_dist(distance)
            except:
                pass
        
        #sorts todo list everytime through
        todo.sort()

        #updates distance only if all previous distances have been reached
        if distance not in dist:
            distance += 1
    if mode == 'fill':
        print_maze(maze, mode)
    else:
        print('-------- All reachable spaces filled.  This is the final map --------')
        print_maze(maze, 'fill')

def main():
    '''
        args: None
        returns: None

        This is the main function where the user is prompted for input
        and the dijkstra_algorithm is called
    '''

    file = input('Please give the grid file: \n')
    maze = map_array(file)
    start = input('Where to start? \n')
    coords = start.strip().split()
    operation = input('What type of operation? \n')
    if operation == 'animate':
        print('Searching from (' + str(coords[0]) + ',' + str(coords[1]) + ') outward.')
        print()
        print('STARTING GRID: ')
        print_maze(maze, 'animate')

    dijkstra_algorithm(maze, int(coords[0]), int(coords[1]), operation)

main()
