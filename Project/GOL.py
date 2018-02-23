def GOL():
    """
    Returns a figure screen of size 32 * 32 Cells with a behaviour
    defined by conways Game of Life (GOL)
    
    Can be called in several different ways.
    
    Parameters
    ----------
    
    --grid-size : define a grid size that is bigger than 8 * 8

    --inteval : Sets the update interval in ms
    
    --glider : Adds a glider in a random position (line, coll).
    
    --beacon : Adds a beacon in a random position (line, coll).
    
    --pulsar : Adds a pulsar in a random position (line, coll).
    
    --cross : Adds a cross in a random position (line, coll).
    
    Returns
    -------
    
    A grid of a given size (min 8*8) with cells behaving as set by conways game of life rule set.
    
    Example
    -------
    GOL_project --grid-size 32
    GOL_project --grid-size 50 --interval 50 --cross
    """
    