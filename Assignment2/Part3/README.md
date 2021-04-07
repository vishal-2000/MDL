# Assignment 2 Part 3
Solve the given MDP problem using Linear programming
## Characters
- Agent: Indiana Jones (IJ)
- Adversary: Mighty Monster (MM)
## States
- State space: {N, S, E, W, C}
- MM is in E block
- 
## Action
- The agent can either move, hit or shoot at a particular moment (all actions are mutually exclusive)
- Move Action space: {up, down, left, right, stay} 
- Centre (C):
    - available move actions: {up, down, left, right, stay} 
    - move success probability = 0.85
    - on failure, the agent will be moved to E state
    - other actions: shoot, hit (he will stay in this case)
    - IJ can shoot an arrow or a blade
        - Arrows
            - p(arrow success) = 0.5
            - arrow damage to MM = 25 
            - Loses one arrow at every shot
        - Blade
            - p(success) = 0.1
            - Damage caused = 50
- North (N):
    - available move actions: {down, stay} 
    - move success probability = 0.85
    - on failure, the agent will be teleported to E state
    - other actions: craft (he will stay in this case)
    - IJ can craft arrows here (if he has 1 material)
        - Upon crafting he will lose his material and 
            - gain 1 arrow with p = 0.5
            - 2 arrows with a p =  0.35
            - 3 arrows with a p = 0.15
- South (S):
    - available move actions: {up, stay} 
    - move success probability = 0.85
    - on failure, the agent will be teleported to E state
    - other actions: gather material
    - gather success p = 0.75
    - Upon successful gathering, 
        - he will gain 1 material if he has no material 
        - No change if he already has 1 material
- East (E):
    - available move actions: {left, stay}
    - move success p = 1.0
    - other actions: shoot arrows, hit with blade
    - Shoot:
        - p(Success) = 0.9
        - Damage = 25
    - Hit:
        - p(Success) = 0.2
        - Damage = 50
- West (W):
    - available move actions: {right, stay}
    - move success p = 1.0
    - other actions: shoot arrows
    - Shoot:
        - p(Success) = 0.25
        - Damage = 25
## Parameters
- Step cost = -10/Y
- arr = [1/2, 1, 2]
- Y = arr[X mod 3] 
- X: team number (97)
- Gamma = (Discount factor) 0.999
- Delta = (Convergence or bellman error) 10^(-3)

## MM notes
- MM has finite health (max = 100) 
- The episode will end once MM has 0 health
- MM can attack IJ
- MM state space: {READY, DORMANT}
- States:
    - Dormant:
        - Moves to READY with p(success) = 0.2 (at each step)
        - Otherwise stays in dormant state
    - Ready:
        - he may attack with p = 0.5
        - he may not attack and stay in this state with p = 0.5
        - IJ will be effected only if he is in E or C state
        - On successful hit:
            - IJ loses all arrows
            - MM will regain 25 health
            - If IJ had planned to take any action at this step, it would be unsuccessful. IJ will get a -ve reward of -40. 
## IJ notes
- Recieves reward (50) once the MM dies (No reward to be considered for part 3)
- Has infinite health
- Has a BOW and BLADE to attack MM
### Constraints
- Can carry at most 3 arrows at any moment
- Can carry at most 2 materials (bow+arrows or bow+blade or arrows+blade) at any moment



