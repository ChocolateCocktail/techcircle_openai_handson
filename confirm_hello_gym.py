import gym
from agents.random_agent import RandomAgent


def main(episode_count):
    env = gym.make('CartPole-v0')
    agent = RandomAgent(env.action_space.n)
    for i in range(episode_count):
        observation = env.reset()  # initialize the environment
        done = False
        step = 0
        while not done:
            env.render()
            action = agent.act(observation)
            next_observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(step + 1))
            observation = next_observation
            step += 1


if __name__ == "__main__":
    main(episode_count=20)
