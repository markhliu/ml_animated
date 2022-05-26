# Machine Learning, Animated
(click on the animations to see actions)


![](https://user-images.githubusercontent.com/50116107/170499945-128bf650-2085-490d-9c85-d699b80669e9.gif)

## Explain Machine Learning through Animated Steps

Words and pictures don't do machine learning justice...

Animations do!

Machine learning has proven to be a poerful tool: it has beaten the world Go champion; it's the brain behind self-driving cars. However, machine learning algorithms, to most people, are like black boxes and hard to understand. 

This free online book is here to help. It summarizes machine learning in three words: initialize, adjust, repeat. 
* Step 1: A machine learning model first assigns values to parameters (initialize);
* Step 2: It then makes predictions and compares them with the actual values; it changes the parameters in such a way so that the predictions will move closer to the actual values (adjust);
* Step 3: It repeats step 2 until the parameters converge (repeat). 

Better yet, the book will use animation to show step by step how machines learn: it shows you the initial values, the change in each step, and the final converged parameters and predictions. 

## Ch1: Create Animation
Learn how to create graphs and plots; convert them into animations; combine multiple animations into one.
<img src="https://gattonweb.uky.edu/faculty/lium/ml/pieplot.gif" />

## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />

## Ch3: Introduction to Neural Networks
See how a neural network learns from ten pairs of values: 𝑋=−40, 𝑌=−40;𝑋=0, 𝑌=32;...;𝑋=100, 𝑌=212. The model first assigns values to w and b in 𝑌=w𝑋+b; it then uses gradient descent to adjust the values of w and b; finally it figures out a linear relation between 𝑋 and 𝑌 that corresponds to the relation between Celsius and Fahrenheit 𝑌=1.8∗𝑋+32. This animation shows the value of w and b in each step:
<img src="https://gattonweb.uky.edu/faculty/lium/ml/nn.gif" />

## Ch4: Activation Functions
We need activation functions such as ReLu to approximate nonlinear relations (as in the left of the animation); or sigmoid to squash values to the range [0, 1] so it can be interprested as a probability (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/relusigmoid.gif" />

## Ch5: Binary Classification
See how a neural network with sigmoid activation learns from image-label pairs. During the course of training, the model weights gradually change and the prediction on a picture of a horse goes closer and closer to 1 (as in the left of the animation) and the prediction on a picture of a deer goes closer and closer to 0 (as in the right of the animation).
<img src="https://gattonweb.uky.edu/faculty/lium/ml/p_horse_deer.gif" />

## Ch6: Convolutional Neural Networks
Learn how convolutional layers extract features from images. See a 3 by 3 filter scans over a 3 by 3 image with zero-padding (as in the left of the animation) and a 2 by 2 filter scans over a 6 by 6 image with stride=2 (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/slide_stride.gif" />

## Ch7: Multi-Class Image Classification
Unerstand how image augmentation and convolutional layers help neural networks learn from image-label pairs. As the training progresses, the 10th value of the prediction on a picture of a truck goes closer and closer to 1 and the rest to 0 (as in the left of the animation) and the 7th value of the prediction on a picture of a frog goes closer and closer to 1 (as in the right of the animation).
<img src="https://gattonweb.uky.edu/faculty/lium/ml/p_truck_frog.gif" />

## Ch8: Apply Deep Learning to the Frozen Lake Game
Desgin deep learning game strategies and apply to the Frozen Lake game in OpenAI Gym. see how the agent uses the trained model to make decisions on what's the best next move. The deep neural network predicts the probability of winning if the agent were to take a certain action. The agent picks the action with the highest probability of winning, step by step.
<img src="https://gattonweb.uky.edu/faculty/lium/ml/frozen_stages.gif" />

## Ch9: Apply Deep Learning to Any Situation
Learn how to creatiely apply deep learning to any situation. The Cart Pole game in OpenAI Gym poses a challenge since there is no clear definition of winning and losing. You'll classify the last ten steps as losing and the rest as winning and successfully train the model. The animation shows how the game is played with (right) and without (left) deep learning strategy.
<img src="https://gattonweb.uky.edu/faculty/lium/ml/compare_cartpole.gif" />

## Ch10: Create Your Own Game Environment
Learn to create your own game environment that mimic the OpenAI Gym. The animation below shows your own Fozen Lake game environment, with graphical game boards.

<img src="https://gattonweb.uky.edu/faculty/lium/ml/frozen_steps.gif" />

## Ch11: Deep Learning Game Strategies: Tic Tac Toe
Create a game environment for Tic Tac Toe with all the features and methods of a typical OpenAI Gym game environment. You'll use the deep learning game strategy to play a full game. At each step, the animation will show the game board on the left, and the probability of winning for each next move on the right. The best move is highlighted.

<img src="https://gattonweb.uky.edu/faculty/lium/ml/ttt_DL_steps.gif" />

## Ch12: Deep Learning Game Strategies: Connect Four
Create a game environment for Connect Four. Use the deep learning game strategy to play a full game. At each step, the animation will show the game board on the left, and the probability of winning for each next move on the right. The best move is highlighted.

<img src="https://gattonweb.uky.edu/faculty/lium/ml/conn_DL_steps.gif" />


## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />
## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />


## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />
## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />


## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />
## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />


## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />
## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />


## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />
## Ch2: Gradient Descent -- Where Magic Happens
Gradient descent guides the model on how to adjust parameters so they converge. The learning rate controls how fast to adust: too fast, the parameters never converge (as in the left of the animation; too small, it takes too long to train the model (as in the right of the animation)
<img src="https://gattonweb.uky.edu/faculty/lium/ml/largetosmall.gif" />


