from string import ascii_uppercase
from random import choice # Choice function returns an item from a list at random.

def make_grid(width, height): 
    """
    Creates a grid that will hold all of the tiles
    for a boggle game
    """
    
    return {(row, col): choice(ascii_uppercase) # This function creates a dictionary with row & col.
        for row in range(height) 
        for col in range(width)}
    
def neighbours_of_position(coords):
    """
    Get neighbours of a given position
    """
    
    row = coords[0] # Assign each number to a variable
    col = coords[1]
    
    # Assign each of the neighbours
    # Top-Left to Top-Right
    
    top_left = (row -1, col -1) # This is always the origin / start point in python (top-left).
    top_center = (row -1, col)
    top_right = (row -1, col +1)
    
    # Left to Right
    left = (row, col -1)
    right = (row, col +1)
    
    # Botton-Left to Bottom-Right
    bottom_left = (row +1, col -1)
    bottom_center = (row +1, col)
    bottom_right = (row +1, col +1)
    
    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]
            
def all_grid_neighbours(grid): 
    """
    'Grid' argument gets all of the possible neighbours
    in each position in the grid.
    """
    
    neighbours = {} # Gets all the possible neighbours by calling the 'neighbours' function
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
        
    return neighbours
    
def path_to_word(grid, path):
    """
    Add all of the letters on the path to a string
    """
    
    return ''.join([grid[p] for p in path])
    
def search(grid, dictionary):
    """
    Search through the paths to locate words by matching
    strings to words in a dictionary
    """
    
    neighbours = all_grid_neighbours(grid) # Get the neighbours of every position
    paths = [] # Get paths list to capture all paths
    
    def do_search(path):
        word = path_to_word(grid, path)
        if word in dictionary:
            paths.append(path)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
                
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    
def get_dictionary(dictionary_file):
    """
    Dictionary code that loads the dictionary_file
    """
    
    with open(dictionary_file) as f:
        return [w.strip().upper() for w in f]
        
def main():
    """
    This is the function that will run the whole project
    The code below represents a high level of abstraction
    """
    
    grid = make_grid(3, 3)
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    for word in words:
        print(word)
    print("Found %s words" % len(words))
   
    """
    Code below is required to help avoid running
    code when a file is imported. The 'if' statement
    will only execute when the file is run directly.  
    Units tests can ow be run without the whole
    boggle solver running. 
    """
    
if __name__ == "__main__": # We want to conditionally run the main ()
    main()
    

    


        
    
    
    
    
    
        
        
    
    
    
    