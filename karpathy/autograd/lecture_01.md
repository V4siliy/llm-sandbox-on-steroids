# Building micrograd

- 🧠 What is Micrograd? It's an autograd engine implementing backpropagation through computational graphs in 100 lines of code. It efficiently calculates the gradient of the loss function with respect to the neural network's weights.

- ➡️ How does the forward pass work? It computes the neural network's output based on input data and a set of weights, using `Value` objects to track scalar values and operation history.

- ⬅️ What is backpropagation? It's a method for calculating the gradient of the loss function with respect to the network's weights, demonstrating the application of the chain rule through manual gradient calculations.

- 🔢 What components make up a neural network? It consists of neurons (input, hidden, and output), each with a weight and bias. The neuron's output passes through an activation function, such as tanh.

- 📚 How is the neural network library implemented? Classes `Neuron`, `Layer`, and `MLP` are defined in ~50 lines of code, implementing multi-layer perceptrons with configurable architecture.

- 🏋️ How is the network trained? It uses a manual implementation of gradient descent, updating parameters by modifying the `.data` attribute. The loss function is calculated as mean squared error.

- 🔄 What's special about the optimization? It's **crucial to zero out gradients** before calling `.backward()` to avoid gradient accumulation. This is a key point in the training process.

- 🎓 What pedagogical approach does Karpathy use? He simplifies complex training methods, emphasizing understanding of neural network fundamentals before moving on to framework optimization.

- 🔍 How does Micrograd compare to PyTorch? Parallels are drawn between `Value` in Micrograd and tensors in PyTorch, demonstrating similarities in backward pass implementation for the tanh function.

- 💡 What are the key takeaways? The lecture emphasizes the importance of understanding basics before using complex frameworks, showing how these concepts scale in modern deep learning tools.

***

Key metaphors and analogies for memorization:

1. "Neural network as a factory": Imagine a neural network as a factory where neurons are workers, weights are tools, and data is raw material. Backpropagation is like an efficiency report passed from the end of the production line to the beginning.

2. "Gradient descent as descending a mountain": Weight optimization is similar to descending a mountain in fog. You take a step in the direction of the steepest slope (gradient), gradually finding your way to the minimum (valley bottom).

3. "Micrograd as a LEGO set": The Micrograd library is like a basic LEGO set from which you can build complex structures (neural networks), understanding how each brick works.

4. "Training a network as tuning an orchestra": The process of training a neural network is akin to tuning an orchestra, where each instrument (neuron) must be precisely adjusted to create harmonious sound (accurate predictions).

5. "Computational graph as a subway map": Picture the computational graph as a subway map, where stations are operations and lines are data and gradient flows. Backpropagation is like a train going in reverse, collecting information at each station.