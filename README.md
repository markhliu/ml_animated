# Machine Learning, Animated

![fourgames_h](https://user-images.githubusercontent.com/50116107/170499945-128bf650-2085-490d-9c85-d699b80669e9.gif)

## Explain Machine Learning through Animated Steps

Words and pictures don't do machine learning justice...

Animations do!

Machine learning has proven to be a poerful tool: it has beaten the world Go champion; it's the brain behind self-driving cars. However, machine learning algorithms, to most people, are like black boxes and hard to understand. 
The goal of this repo is to train the agent so that it learns to dig a tunnel on the side
of the wall to send the ball to the back of the wall to score more efficiently.

In 2013, the DeepMind team achieved this by using a different approach, namely,
the Deep Q Learning method. Policy Gradient is a different method in reinforcement learning.

Here I am using the policy gradients approach, inspired by this post:
http://karpathy.github.io/2016/05/31/rl/
by Stanford computer scientist Andrej Karpathy.

The code I used is largely based on Andrej's code for the Atari Pong below
https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5

Andrej uses the Atari Pong game but I use the Breakout game here. 
With Breakout, things are more complicated in two ways: 
first, in the Pong game, you only need to move the 
paddle up or down, which is a binary choice. Second, in the Pong game,
the reward structure is more nuanced: -1 for missing,
1 for winning, and 0 if nothing happens. 

In contrast, in Breakout, you need four choices: left, right, no movement, 
or firing the ball. Second, the reward is either 0 or 1. There is no reward
of -1 if the paddle misses the ball.

I changed the binary-classification to multiple-classification; 
Then I hardcode in a reward of -1 if the paddle misses the ball by counting 
the numbers of lives left for the agent. 
