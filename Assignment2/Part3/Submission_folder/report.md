# Assignment 2 Part 3 (Solving MDPs using LP)
## Team credentials
- Team number 97 (and therefore step cost = -10)
- Team members:
    1. Vishal Reddy Mandadi
    2. Hrishi Narayanan
## Introduction
### Concept of Solution
    The problem is solved using Dantzig's simplex algorithm. The variable x_{ia} denotes the expected number of times the action 'a' is taken in state 'i'. The R matrix contains the reward recieved where element r_{ia} implies reward recieved on performing action 'a' in state 'i'. We would like to find the x such the product [np.transpose(R)*x] reaches it's maximum possible value. Max product ensures that x_{ia} is highest when r_{ia} is high => implies we encourage the system to take that action which promises us with maximum reward for that step. Since it is not perfectly deterministic, hence we use expected values. We first solve for x_{ia} for all i and a. Finally, we define policy as 
```python
policy(s) = argmax(x(s, a)) where a is the arguement and x is the vector defined above
```
    The maximization of [np.transpose(R)*x] is subject to the condition the constraints A.x=alpha and x>=0. We will talk about these in detail in the upcoming sections.
## Procedure of making A matrix
### Concept of A matrix
    The A matrix is used to enforce the following constraint (through the equation A.x=0)
```
Expected number of times an agent enters a state = Expected number of times an agent leaves a state (for all non-absorbing state)
Expected number of times an agent enters a state not equal to Expected number of times an agent leaves a state (for absorbing states)
```
    The constraint models the fact that agent takes some action in all non-absorbing states and these actions help them to reach other states. However, in absorbing states, the agent takes NONE action to leave and never to come back, therefore expected number of times an agent leaves this state is not equal to Expected number of times an agent enters a state.

### Construction procedure (in steps)
We followed the following set of steps for constructing the A matrix (algorithmically):
1. Take a particular state action pair (s, a)
2. For that particular state action pair, first put A(s)(s, a) = 1 (meaning, the agent comes out of that state with 100% probability when that action is performed initially (could go back later again and this is explained by step 4))
3. Then, if set O denotes the set of all outcomes (destination states) from (s, a), then for each 'd' belonging to the set O, update A(O)(O, a) as:
    ```python
        A[O][O, a] += -1*(probability of reaching state O on executing 'a' when in state 's')
    ```
4. Remember that for some (s, a) pairs, it is possible to reach state s with some probability p. That case is automatically taken care of by step 3
5. Repeat steps 1, 2, 3 for all possible valid state-action pairs
## Policy construction and Results analysis
### Procedure to find the policy
As said before, x_{ia} denotes the expected number of times an agent takes action 'a' when in state 'i'. The concept and modelling of MDP in LP form is already explained in section 1 (under concept of Solution) so we are not repeating it here. We get desired values of x on solving the following equations 
```
max(R.transpose * x)
such that A.x=alpha and x>=0
```
Now, the policy is calculated using the equation:
```python
policy(s) = argmax(x(s, a)); where a is the arguement
```
Essentially, when in a particular state, it is always rational to choose the action that maximizes the net reward attainable. Higher value of x_{ia} denotes higher the expected reward for taking action 'a' when in state 'i' (This is how we designed the model), hence, it is programmed to choose the actions which ensure highest expected rewards in a particular state.
### Results and analysis
#### Results:
- The agent takes "NONE" when health of MM is zero as NONE is the only action allowed
- The agent prefers "RIGHT" (with more probability) or "STAY" or "SHOOT when in W state when MM is dormant. However, when MM is active, the agent is scared to hell and always chooses to shoot or stay (with shoot being more probable only if has 2 arrows, otherwise, it stays). It is reasonable, because, the agent tries to loose as many less arrows as possible when in state W as the accuracy is very low but however if the MM is ready, it would rather shoot or stay than move right. In fact shoot is more observed because this action will not change the position to E under any circumstance even probabilistically. Following are the results:
```
[['W', 0, 2, 'D', 0], 'NONE']
[['W', 0, 2, 'D', 25], 'SHOOT']
[['W', 0, 2, 'D', 50], 'RIGHT']
[['W', 0, 2, 'D', 75], 'SHOOT']
[['W', 0, 2, 'D', 100], 'RIGHT']
```
```
[['W', 2, 1, 'R', 0], 'NONE']
[['W', 2, 1, 'R', 25], 'STAY']
[['W', 2, 1, 'R', 50], 'SHOOT']
[['W', 2, 1, 'R', 75], 'SHOOT']
[['W', 2, 1, 'R', 100], 'SHOOT']
```
- When the agent is in centre state, if MM is in dormant state, IJ prefers to shoot, however if MM is ready, IJ prefers to go up to craft more arrows even when it has 3 arrows left as escaping is it's primary priority. However, if no of arrows are 3, it chooses to go left or down depending on the availability of material as arrows are already in abundance. If arrows are less than 3, then it always chooses to go up
```
[['C', 2, 3, 'R', 0], 'NONE']
[['C', 2, 3, 'R', 25], 'LEFT']
[['C', 2, 3, 'R', 50], 'LEFT']
[['C', 2, 3, 'R', 75], 'UP']
[['C', 2, 3, 'R', 100], 'UP']
```
- When it's in the east state, with full arrows, it tries to shoot and hit even when MM is in ready state. As long as it has arrows left, it always tries to shoot (but when its health is 100, it tries to hit because the remaining health can be drained out by the remaining arrows). When there are no arrows left, it chooses to hit even when MM is ready, since the agent has more probability of hitting the MM.
```
[['E', 2, 0, 'R', 0], 'NONE']
[['E', 2, 0, 'R', 25], 'HIT']
[['E', 2, 0, 'R', 50], 'HIT']
[['E', 2, 0, 'R', 75], 'HIT']
[['E', 2, 0, 'R', 100], 'HIT']
```
```
[['E', 2, 1, 'R', 0], 'NONE']
[['E', 2, 1, 'R', 25], 'SHOOT']
[['E', 2, 1, 'R', 50], 'SHOOT']
[['E', 2, 1, 'R', 75], 'SHOOT']
[['E', 2, 1, 'R', 100], 'HIT']
```

- The behaviour of the agent in south state is similar to that of it when it is in north state. When the MM is in ready state, the agent always chooses to GATHER as that way it can stay put in S state with 100% probability thus avoiding the wrath of MM.
```
[['S', 2, 1, 'R', 0], 'NONE']
[['S', 2, 1, 'R', 25], 'GATHER']
[['S', 2, 1, 'R', 50], 'GATHER']
[['S', 2, 1, 'R', 75], 'GATHER']
[['S', 2, 1, 'R', 100], 'GATHER']
```
- However, when MM is in state 'D', it chooses to stay there itself. This could be because the agent will now have two possibilities, it could either get hurt when it is teleported to E and subsequently the MM chooses to attack, but the probability is very low. There is also a possibility where the agent may got to E safely and then even cause damage to MM. Conclusion is that, our agent has taken around 0.15*0.2*0.5 = 0.05 chance of being punished and atleast 0.15*0.5 = 0.075 chance of damaging the MM and about 0.85 chance of staying safe. So statistically, the action "STAY" in such case is a good gamble. 
```
[['S', 2, 1, 'D', 0], 'NONE']
[['S', 2, 1, 'D', 25], 'STAY']
[['S', 2, 1, 'D', 50], 'UP']
[['S', 2, 1, 'D', 75], 'STAY']
[['S', 2, 1, 'D', 100], 'STAY']
```
- However you can observe below that when it comes to the case where MM is already ready, chance of being punished are fairly high and hence the agent rather chooses to gather as gather keeps the agent 100% safe
```
[['S', 1, 0, 'R', 0], 'NONE']
[['S', 1, 0, 'R', 25], 'GATHER']
[['S', 1, 0, 'R', 50], 'GATHER']
[['S', 1, 0, 'R', 75], 'GATHER']
[['S', 1, 0, 'R', 100], 'STAY']
```
##### Conclusion from the result
- With a step cost of -10, our agent is still chooses to averse the risk as the penalty on being hit by MM is still 4 times that of step cost. This behavior is observed when agent takes actions craft and gather when in N or S states especially when MM is ready. However, when MM is dormant, the agent goes statistical and chooses to play with minimal risk and the amount of risk depends on the step cost. Lower the step cost, lower the risk it is willing to take, but if step cost is itself high, then it is ready to take the action (as waiting is now more costly than attacking the MM in ready state, statistically speaking)
## Can there be multiple policies? Why? What changes can you make in your code to generate another policy?
Yes, there can be multiple policies. Policy depends on:
1. Rewards. Agent always tends to gain as much high reward as possible (which again depends on our design and in these cases, we tend to design them to get max rewards), therefore, their actions, decision rules are such that the total expected reward is maximum. Rewards are involved in following vectors/variables:
    - R matrix
    - step cost
Therefore, by making changes to R matrix or changing the step cost can change the policy. However simple scaling may not work as the agent always looks for relative rewards (because pure numbers make no sense in linear world, it is relative grading that matters)
2. Start states and start state distribution. The agent depends on them because there are some states which are generally visited with very low probability by the agent. Since agent already knows that it may visit it less number of times, it will be ready to take some risky decisions. Now, if you make it a start state, the agent's expected number of visits will increase, due to which it will first reduce the risk while in the state, it will also try to lower the net visits by changing the policy in the adjacent states to balance the risk and max reward. The following variables/vectors determine the start states and their distribution:
    - start_state variable
    - alpha vector
Therefore, by changing them, you will be able to generate new policies.
3. You can change the A matrix by changing the probability distribution of destination states for any or all states. This will obviously give different policies as destination distribution is the one that decides the attainable rewards. Therefore you can tweak some probability distributions to get different policies. However it is not advised to put random values in A matrix as you are more likely to end up with an unbounded or invalid solutions. Change them by carefully tweaking the destination state distributions. 

Thank you.