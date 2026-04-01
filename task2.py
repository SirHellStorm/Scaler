from env.environment import CorporateMarketEnv
from env.models import Resource, Position
from env.logic import PROFILES

def setup_task2():
    """
    Task 2: Resource Optimization (Medium)
    Objective: Protect your central PR resource from a threatening competitor while optimizing a Team reallocation.
    Initial State: WhiteCorp PR threatened by BlackCorp R&D. WhiteCorp must move a Team to protect.
    """
    env = CorporateMarketEnv()
    env.reset()
    
    # No randomness deterministic state
    env.current_state.resources = []
    
    # WhiteCorp Assets
    env.current_state.resources.append(
        Resource(company="WhiteCorp", profile=PROFILES["PR"], position=Position(row=4, col=4))
    )
    env.current_state.resources.append(
        Resource(company="WhiteCorp", profile=PROFILES["Team"], position=Position(row=4, col=0))
    )
    
    # BlackCorp Threat
    env.current_state.resources.append(
        Resource(company="BlackCorp", profile=PROFILES["R&D"], position=Position(row=6, col=5))
    )
    
    env.current_state.active_turn = "WhiteCorp"
    
    objective = "Reallocate your Team from (4, 0) to defend the central PR asset at (4, 4) from the BlackCorp R&D threat."
    
    return env, objective

if __name__ == "__main__":
    env, obj = setup_task2()
    print("Task 2 Ready:", obj)
