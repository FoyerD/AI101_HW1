import numpy as np
from numpy.typing import NDArray

global_goal_state : NDArray[np.int32] = np.array([])

def init_goal_for_search(goal_blocks: str) -> None:
    global global_goal_state
    global_goal_state = np.array(goal_blocks.split(','))


def parse_state_to_ndarray(blocks_str: str) -> NDArray[np.int32]:
    #!TODO complete
    return np.array([])
    

class color_blocks_state:
    def __init__(self, blocks_str: str, g: float=0, h: float=0):
        self.state_array : NDArray[np.int32] = parse_state_to_ndarray(blocks_str)
        self.g : float = g
        self.h : float = h
        self.f : float = g + h
        

    @staticmethod
    def is_goal_state(_color_blocks_state):
        global global_goal_state
        return global_goal_state == _color_blocks_state

    def get_neighbors(self):
        #!TODO complete
        pass

        # you can change the body of the function if you want
        # def __hash__(self):

        # you can change the body of the function if you want
        # def __eq__(self, other):
        # you can change the body of the function if you want

    # for debugging states
    def get_state_str(self):
        #!TODO complete
        pass

    def __hash__(self):
        return self.state_array.__hash__()

    def __eq__(self, other):
        return self.state_array == other.state_array

    #you can add helper functions
