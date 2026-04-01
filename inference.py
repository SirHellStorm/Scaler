import os
import sys
import json

try:
    from openai import OpenAI
except ImportError:
    pass

from tasks.task1 import setup_task1
from tasks.task2 import setup_task2
from tasks.task3 import setup_task3
from grader.grader import grade_task1_market_expansion, grade_task2_resource_optimization, grade_task3_corporate_domination
from env.models import Action, Position

def format_board(env):
    state = env.state()
    board = ""
    for r in state.resources:
        board += f"[{r.company}] {r.profile.role} at ({r.position.row}, {r.position.col})\n"
    return board

def run_task(client, model_name, task_idx, setup_func, grader_func, max_steps):
    try:
        env, objective = setup_func()
        initial_state = env.state()
        steps_taken = 0
        
        for step in range(max_steps):
            board_str = format_board(env)
            prompt = (
                f"Objective: {objective}\n"
                f"Current Board State:\n{board_str}\n"
                f"You are WhiteCorp. Output raw JSON ONLY: {{\"from_row\": 0, \"from_col\": 0, \"to_row\": 0, \"to_col\": 0}}"
            )
            
            try:
                print(f"[STEP]")
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.0
                )
                
                content = response.choices[0].message.content.strip()
                if "```json" in content:
                    content = content.replace("```json", "").replace("```", "").strip()
                elif "```" in content:
                    content = content.replace("```", "").strip()
                    
                data = json.loads(content)
                
                action = Action(
                    company="WhiteCorp",
                    from_pos=Position(row=data.get("from_row", 0), col=data.get("from_col", 0)),
                    to_pos=Position(row=data.get("to_row", 0), col=data.get("to_col", 0))
                )
                
                _, _, done, _ = env.step(action)
                steps_taken += 1
                
                if done:
                    break
                    
            except Exception:
                steps_taken += 1
                break
                
        final_state = env.state()
        score = grader_func(initial_state, final_state, steps_taken)
        print(f"[END] {score:.2f}")
        
    except Exception:
        print(f"[END] 0.00")

def main():
    print("[START]")
    
    api_base_url = os.environ.get("API_BASE_URL", "https://api.openai.com/v1")
    model_name = os.environ.get("MODEL_NAME", "gpt-4o-mini")
    hf_token = os.environ.get("HF_TOKEN")
    
    if not hf_token:
        # Failsafe execution preventing standard out pollution
        print("[END] 0.00")
        print("[END] 0.00")
        print("[END] 0.00")
        return
        
    try:
        client = OpenAI(base_url=api_base_url, api_key=hf_token)
    except NameError:
        print("[END] 0.00")
        print("[END] 0.00")
        print("[END] 0.00")
        return

    tasks_info = [
        (1, setup_task1, grade_task1_market_expansion, 6),
        (2, setup_task2, grade_task2_resource_optimization, 3),
        (3, setup_task3, grade_task3_corporate_domination, 4)
    ]
    
    for task_idx, setup_func, grader_func, max_steps in tasks_info:
        run_task(client, model_name, task_idx, setup_func, grader_func, max_steps)

if __name__ == "__main__":
    main()
