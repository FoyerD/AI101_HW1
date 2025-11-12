import numpy as np
from numpy.typing import NDArray

global_goal_state : NDArray[np.float32] = np.array([])

def init_goal_for_search(goal_blocks: str) -> None:
    global global_goal_state
    global_goal_state = np.array(goal_blocks.split(','))


def parse_state_to_ndarray(blocks_str: str) -> NDArray[np.float32]:
    return np.array([])
    

class color_blocks_state:
    def __init__(self, blocks_str: str, g: np.float32=np.float32(0), h: np.float32=np.float32(0)):
        self.state_array : NDArray[np.float32] = parse_state_to_ndarray(blocks_str)
        self.g : np.float32 = g
        self.h : np.float32 = h
        self.f : np.float32 = g + h
        

    @staticmethod
    def is_goal_state(_color_blocks_state):
        pass

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



    #you can add helper functions