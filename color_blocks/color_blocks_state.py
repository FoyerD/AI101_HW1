import numpy as np
from numpy.typing import NDArray

global_goal_state : NDArray[np.int32] = np.array([])

def init_goal_for_search(goal_blocks: str) -> None:
    global global_goal_state
    global_goal_state = np.array(goal_blocks.split(','))


def parse_state_to_ndarray(blocks_str: str) -> NDArray[np.int32]:
    return np.array([])
    

class color_blocks_state:
    def __init__(self, blocks_str: str, g: np.int32=np.int32(0), h: np.int32=np.int32(0)):
        self.state_array : NDArray[np.int32] = parse_state_to_ndarray(blocks_str)
        self.g : np.int32 = g
        self.h : np.int32 = h
        self.f : np.int32 = g + h
        

    @staticmethod
    def is_goal_state(_color_blocks_state):
        return 

    def get_neighbors(self):
        pass

        # you can change the body of the function if you want
        # def __hash__(self):

        # you can change the body of the function if you want
        # def __eq__(self, other):
        # you can change the body of the function if you want

    # for debugging states
    def get_state_str(self):
        pass

    @override
    def __eq__(self, other):
        return self.state_array == other.state_array

    #you can add helper functions
