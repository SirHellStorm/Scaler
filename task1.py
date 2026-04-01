from env.environment import CorporateMarketEnv
from env.models import Resource, Position
from env.logic import PROFILES

def setup_task1():
    """
    Task 1: Market Expansion (Easy)
    Objective: Penetrate an empty market column with your Intern resource to reach the baseline.
    Initial State: A single WhiteCorp Intern with a clear path against BlackCorp's empty flank.
    """
    env = CorporateMarketEnv()
    env.reset()
    
    # No randomness deterministic state
    env.current_state.resources = []
    
    # WhiteCorp Intern trying to expand
    env.current_state.resources.append(
        Resource(company="WhiteCorp", profile=PROFILES["Intern"], position=Position(row=6, col=0))
    )
    
    # BlackCorp defense on the other side
    env.current_state.resources.append(
        Resource(company="BlackCorp", profile=PROFILES["Manager"], position=Position(row=0, col=7))
    )
    
    env.current_state.active_turn = "WhiteCorp"
    
    objective = "Advance your Intern at (6, 0) upwards directly into the competitor baseline to maximize market expansion."
    
    return env, objective

if __name__ == "__main__":
    env, obj = setup_task1()
    print("Task 1 Ready:", obj)
