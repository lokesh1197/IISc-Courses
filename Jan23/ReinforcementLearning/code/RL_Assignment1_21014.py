import numpy as np
import math

class Maze:
    def __init__(self, gridHeight=6, gridWidth=6, terminalReward=10, lockPickProb=0.5):
        self.rewardsLeft = np.array([[-1, 0, 0, 0, 0, 0], 
                                    [-1, -1, 0, 0, 0,-10], 
                                    [-1, 0, 0, -1, -1, -1], 
                                    [0, 0, 0, -10, -1, -1],
                                    [-1, -1, 0, 0, -1, 0],
                                    [-1, 0, -1, 0, 0 ,-1]])

        self.rewardsRight =  np.array([[ 0, 0, 0, 0, 0, -1], 
                            [ -1, 0, 0 , 0, -10, -1],
                            [ 0, 0, -1, -1, -1, -1],
                            [ 0, 0, -10, -1, -1 ,-1],
                            [ -1, 0, 0, -1, 0, -1],
                            [ 0, -1, 0, 0, -1, -1]])

        self.rewardsUp  =  np.array([[ -1, -1, -1, -1, -1, -1], 
                            [ 0, -1, -1, -1, -1, 0],
                            [ 0, 0, -1, 0, 0, 0],
                            [ -1, 0,0, 0,0, 0],
                            [ 0, -10, -1, -1, -1, 0],
                            [ 0,  0, -1, -10, 0, 0]])


        self.rewardsDown =  np.array([[ 0, -1, -1, -1, -1, 0], 
                            [ 0, 0, -1, 0, 0, 0],
                            [ -1, 0, 0, 0, 0, 0],
                            [ 0, -10,-1,-1,-1, 0],
                            [  0,0,-1,-10,0, 0],
                            [ -1, -1, -1, 0, -1, -1]])

        self.gridHeight = gridHeight
        self.gridWidth = gridWidth
        self.lockPickProb = lockPickProb
        self.terminalReward = terminalReward


    def isStateTerminal(self, state):
        if state == (3, 0) :
            return True
        elif state == (5, 3):
            return True
        return False

    def takeAction(self, state, action):
        retVal = []
        if(self.isStateTerminal(state)):
            return [[state,1, self.terminalReward]] 

        if action=='left':
            reward = self.rewardsLeft[state]
            if(reward == -1):
                retVal.append([state,1,-1])
            elif(reward == -10):
                retVal.append([(state[0], state[1]-1),self.lockPickProb,-1])
                retVal.append([state,1-self.lockPickProb,-1])
            else:
                retVal.append([(state[0], state[1]-1),1,-1])

        if action=='right':
            reward = self.rewardsRight[state]
            if(reward == -1):
                retVal.append([state,1,-1])
            elif(reward == -10):
                retVal.append([(state[0], state[1]+1),self.lockPickProb,-1])
                retVal.append([state,1-self.lockPickProb,-1])
            else:
                retVal.append([(state[0], state[1]+1),1,-1])

        if action=='up':
            reward = self.rewardsUp[state]
            if(reward == -1):
                retVal.append([state,1,-1])
            elif(reward == -10):
                retVal.append([(state[0]-1, state[1]),self.lockPickProb,-1])
                retVal.append([state,1-self.lockPickProb,-1])
            else:
                retVal.append([(state[0]-1, state[1]),1,-1])

        if action=='down':
            reward = self.rewardsDown[state]
            if(reward == -1):
                retVal.append([state,1,-1])
            elif(reward == -10):
                retVal.append([(state[0]+1, state[1]),self.lockPickProb,-1])
                retVal.append([state,1-self.lockPickProb,-1])
            else:
                retVal.append([(state[0]+1, state[1]),1,-1])
        for i,[nextState, prob, reward] in enumerate(retVal):
            if(self.isStateTerminal(nextState)):
                retVal[i][2] = self.terminalReward   

        return retVal 

class GridworldSolution:
    def __init__(self, maze,horizonLength):
        self.env = maze
        self.actionSpace = ['left', 'right', 'up',  'down']
        self.horizonLength = horizonLength
        self.DP = np.ones((self.env.gridHeight,self.env.gridWidth,self.horizonLength),dtype = float) * -np.inf
    
    def optimalReward(self, state, k):
        optReward = -np.inf
        
        #### Write your code here
        self.exp_rewards = []
        for _ in range(self.horizonLength + 1):
            self.exp_rewards.append({})

        def exp_reward(curr_state, steps):
            if steps == 0:
                return np.array([0], dtype=np.int32)

            key = str(curr_state)
            if key in self.exp_rewards[steps]:
                return self.exp_rewards[steps][key]

            next_states = list(map(lambda action : self.env.takeAction(curr_state, action), self.actionSpace))
            rewards = list(map(
                lambda x : np.append(x[0][1] * exp_reward(x[0][0], steps - 1) + (x[1][1] * exp_reward(x[1][0], steps - 1) if len(x) > 1 else 0), sum([y[1] * (y[2] + exp_reward(y[0], steps - 1)[-1]) for y in x]))
                , next_states))

            self.exp_rewards[steps][key] = np.array(max(rewards, key=lambda x : x[-1]), dtype=np.int32)
                
            return self.exp_rewards[steps][key]

        optReward = exp_reward(state, self.horizonLength)[-(k+1)]
        ########
        return optReward

if __name__ == "__main__":
    maze = Maze()
    solution = GridworldSolution(maze,horizonLength=5)
    print(" Horizon ", solution.horizonLength)
    optReward = solution.optimalReward((2,0),0)
    print(" Optimal Reward ", optReward)
    assert optReward==28.0, 'wrong answer'
