import threading
import random
import time


# Global variables
INGREDIENTS_NAMES = {'tobacco', 'paper', 'matches'}
ingredients_semaphores = {
    'tobacco_paper': threading.Semaphore(0), 
    'tobacco_matches': threading.Semaphore(0), 
    'paper_matches': threading.Semaphore(0)
    }  # Semaphores for the possible pairs of ingredients that the agent may produce
agent_semaphore = threading.Semaphore(0)  # Semaphore synchronization between agent and smokers


class Agent(threading.Thread):

    def run(self):
        '''
        This method runs the agent thread. It simulates the work of the agent.
        '''
        while True:

            # Choose ingredient pair to make available to smokers
            try:
                random_seed = int(input('\nEnter a number for the random seed: ')) * 100
            except ValueError:
                print("Invalid input, setting random seed to 0")
                random_seed = 0
            random.seed(random_seed)
            ingredient_pair = random.choice(list(ingredients_semaphores.keys()))

            # Make the ingredient pair available to smokers
            ingredients_semaphores[ingredient_pair].release()  # call sem signal on ingredients pair
            print(f"Agent makes {ingredient_pair} available to smokers")

            # Wait for the smoker that has the complementary ingredient to 
            # pick up the ingredients, make cigarette, and finish smoking
            ingredients_semaphores[ingredient_pair].acquire()  # call sem wait on ingredients pair



class Smoker(threading.Thread):

    def __init__(self, name, ingredient):
        '''
        initialize the smoker thread.
        '''
        super().__init__()
        self.name = name

        # set the required ingredient pair
        if ingredient == 'tobacco':
            self.required_ingredient_pair = 'paper_matches'
        elif ingredient == 'paper':
            self.required_ingredient_pair = 'tobacco_matches'
        elif ingredient == 'matches':
            self.required_ingredient_pair = 'tobacco_paper'


    def run(self):
        '''
        This method runs the smoker thread. It simulates the work of each smoker.
        '''
        while True:

            # Wait for complimentary ingredients to be available
            print(f"{self.name} waits for {self.required_ingredient_pair}")
            ingredients_semaphores[self.required_ingredient_pair].acquire()  # sem wait on required ingredient pair semaphore
            
            # Make cigarette and smoke it
            print(f"{self.name} makes a cigarette and smokes it")
            time.sleep(random.uniform(0.5, 1.5))  # simulate smoking for a random duration of time between 0.5 and 1.5 seconds

            # Signal agent that the ingredients pair is used up 
            print(f"{self.name} signals to agent to make next ingredients pair")
            ingredients_semaphores[self.required_ingredient_pair].release()  # sem signal on required ingredient pair semaphore


def main():
    '''
    Main program, simulates the Cigarette Smokers' Problem
    '''

    # Create agent and smokers
    agent = Agent()
    smoker1 = Smoker('Smoker with tobacco', 'tobacco')
    smoker2 = Smoker('Smoker with paper', 'paper')
    smoker3 = Smoker('Smoker with matches', 'matches')
    smokers = {smoker1, smoker2, smoker3}

    # Start agent and smokers threads (simulate their work)
    for smoker in smokers:
        smoker.start()
    agent.start()

    # Wait for threads to finish 
    for smoker in smokers:
        smoker.join()
    agent.join()


# Run the main program
if __name__ == '__main__':
    main()
    print('Done')
    exit(0)