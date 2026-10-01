import random

def random_walk_visualizer(steps=25, width=31):
    position = width // 2


    for step_num in range(1, steps + 1):
        track = list("-" * width)
        
        
        print(f"Step {step_num:2d}: {''.join(track)}")
        move = random.choice([-1, 1])
        position += move
        position = max(0, min(width - 1, position))
if __name__ == "__main__":
    random_walk_visualizer(steps=20, width=25)
