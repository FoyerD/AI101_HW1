from color_blocks_state import color_blocks_state
import numpy as np
# you can add helper functions and params

global_goal_blocks = ''

def init_goal_for_heuristics(goal_blocks: str) -> None:
    global global_goal_blocks
    global_goal_blocks = np.array(list(map(np.int32, goal_blocks.split(","))), dtype=np.int32)

def base_heuristic(_color_blocks_state: color_blocks_state):
    base_sum = 0
    for i in range(len(color_blocks_state.state_array)-1):
        pass
    return base_sum

def advanced_heuristic(_color_blocks_state):
    return 0

