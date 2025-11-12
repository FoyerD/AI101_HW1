import numpy as np
from numpy.typing import NDArray

global_goal_state : NDArray[np.float64] | None = None

def init_goal_for_search(goal_blocks: str) -> None:
    global global_goal_state
    global_goal_state = np.array(goal_blocks.split(','))

class color_blocks_state:
    self.state_array : NDArray[tuple[np.float64, np.float64]] | None = None

    def __init__(self, blocks_str, **kwargs):
        # you can use the init function for several purposes
        pass

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