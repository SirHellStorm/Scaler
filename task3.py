from env.environment import CorporateMarketEnv
from env.models import Resource, Position
from env.logic import PROFILES

def setup_task3():
    """
    Task 3: Corporate Domination (Hard)
    Objective: Execute a hostile takeover of the competitor's CEO using disruptive R&D movements in an entrenched market.
    Initial State: BlackCorp CEO is heavily defended. WhiteCorp must use R&D and Manager synergy.
    """
    env = CorporateMarketEnv()
    env.reset()
    
    # No randomness deterministic state
    env.current_state.resources = []
    
    # Heavily entrenched BlackCorp CEO
    env.current_state.resources.append(
        Resource(company="BlackCorp", profile=PROFILES["CEO"], position=Position(row=0, col=0))
    )
    env.current_state.resources.append(
        Resource(company="BlackCorp", profile=PROFILES["Team"], position=Position(row=0, col=1))
    )
    env.current_state.resources.append(
        Resource(company="BlackCorp", profile=PROFILES["Team"], position=Position(row=1, col=0))
    )
    
    # WhiteCorp Aggressors
    env.current_state.resources.append(
        Resource(company="WhiteCorp", profile=PROFILES["R&D"], position=Position(row=2, col=2))
    )
    env.current_state.resources.append(
        Resource(company="WhiteCorp", profile=PROFILES["Manager"], position=Position(row=4, col=1))
    )
    
    env.current_state.active_turn = "WhiteCorp"
    
    objective = "Navigate your R&D resource from (2, 2) to breach the BlackCorp defenses and force a Hostile Takeover on their CEO at (0, 0)."
    
    return env, objective

if __name__ == "__main__":
    env, obj = setup_task3()
    print("Task 3 Ready:", obj)
