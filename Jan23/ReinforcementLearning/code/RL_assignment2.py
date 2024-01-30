import numpy as np 
#RL environment
class gridworld:
    def __init__(self, dims, goal_states, error_states):
        # for actions
        self.actions = ["up", "down", "right", "left"]
        self.action_map = {"up": 0, "down":1, "right": 2, "left": 3}
        self.movement = [[-1,0], [1,0], [0,1], [0,-1]]	

        # for states
        self.rows = dims[0]
        self.columns = dims[1]
        self.current_state = None
        self.error_states = error_states 
        self.goal_states = goal_states
        self.empty_states =  [(i, j) for i in range(self.rows) for j in range(self.columns) if (i, j) not in (self.goal_states + self.error_states)]

        # visual representation of gridworld
        self.grid = np.array([["." for i in range(self.columns)] for j in range(self.rows)])
        for g in self.goal_states:
            self.grid[g] = "O"
        for e in self.error_states:
            self.grid[e] = "X"

    #print gridworld
    def print_grid(self):				
        print(self.grid)

    #set current state to start state
    def reset(self, start_state = None):
        if start_state != None:
             self.current_state = start_state
        else:
            self.current_state =  self.empty_states[np.random.choice(len(self.empty_states))]
        return self.current_state

    def step(self, action): 
        action_index = action
        action_taken = self.actions[action]  
        
        new_state, reward  = (-1, -1), 0 
        
        # out of the board , no movement but -reward for taking action
        if (action_taken == "up" and self.current_state[0] == 0) or (action_taken == "down" and self.current_state[0] == self.rows-1) :
            raise Exception("Invalid action taken")
        elif (action_taken == "left" and self.current_state[1] == 0) or (action_taken == "right" and self.current_state[1] == self.columns-1) :
            raise Exception("Invalid action taken")

        # inside the board
        else:
            new_state = (self.current_state[0] + self.movement[action_index][0] , self.current_state[1] + self.movement[action_index][1])
            if new_state in self.empty_states: # no reward in empty states 
                reward = -1
            elif new_state in self.goal_states: # good state
                reward = 10
            elif new_state in self.error_states: # bad state
                reward = -5 

        # current state changes because of taking action 
        self.current_state = new_state  

        #return current state, reward 
        return self.current_state, reward

class Solution:
    def __init__(self, env, gamma=0.9, epsilon=0.1, maxIter=5000, maxTimesteps = 100):
        self.q_table = {}
        self.env = env
        self.gamma, self.epsilon, self.maxIter, self.maxTimesteps = gamma, epsilon, maxIter, maxTimesteps
        ####### You may add extra functions/ variables in this class

    def isValidAction(self, state, action):
        if self.env.actions[action] == "up":
            return 0 < state[0]
        if self.env.actions[action] == "down":
            return self.env.rows - 1 > state[0]
        if self.env.actions[action] == "left":
            return 0 < state[1]
        if self.env.actions[action] == "right":
            return self.env.columns - 1 > state[1]
        return True

    # Define the Q-learning algorithm
    def q_learning(self):
        q_table = np.zeros((self.env.rows, self.env.columns, len(self.env.actions)))
 
        for iter in range(self.maxIter):
            state = self.env.reset()

            ########## Complete this function #######
            # to calculate alpha for each iteration , alpha = 1 / visit_n(s, a)
            visit_n = np.zeros((self.env.rows, self.env.columns, len(self.env.actions)))
            reachedTerminal = False
            terminalAction = -1
            terminalReward = 0

            for _ in range(self.maxTimesteps):
                if reachedTerminal:
                    visit_n[state[0], state[1], terminalAction] += 1
                    alpha = 1 / visit_n[state[0], state[1], terminalAction]
                    q_table[state[0], state[1], terminalAction] *= (1 - alpha)
                    q_table[state[0], state[1], terminalAction] += alpha * terminalReward
                    break
                else: 
                    for action in range(len(self.env.actions)):
                        if self.isValidAction(state, action):
                            visit_n[state[0], state[1], action] += 1
                            alpha = 1 / visit_n[state[0], state[1], action]
                            next_state, reward = self.env.step(action)
                            if next_state in self.env.goal_states:
                                q_table[state[0], state[1], action] += reward
                                reachedTerminal = True
                                terminalAction = action
                                terminalReward = reward
                                break
                            q_table[state[0], state[1], action] *= (1 - alpha)
                            q_table[state[0], state[1], action] += alpha * (reward + self.gamma * np.max(q_table[next_state[0], next_state[1]]))
                            state = next_state

            #############################

        return q_table 


if __name__ == "__main__":
    np.random.seed(100)

    size = 3
    goal_states = [(0, size-1), (1, size-1), (size-1, 0)] 
    error_states = [(o, o) for o in range(size)] 
    grid = gridworld((size, size), goal_states, error_states)

    grid.print_grid()
    solution = Solution(grid)
    q_table = solution.q_learning()

    print("Q-table:")
    print(q_table)


    assert round(q_table[0,0,1], 5)== 75.5 and round(q_table[0,1,2], 5)==100.0, 'wrong answer'
