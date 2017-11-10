# 1. Compute graph
TensorFlow separates definition of computions from their execution
* assemble a graph
  + Step 1: Read in data
  + Step 2: Create placeholders for inputs and labels
    ```tf.placeholder(dtype, shape=None, name=None)```
* use a session to excute operations in the graph

# 2. TensorBoard

# 3. Constant vs Variable
* Constant values are stored in the graph definition
* Sessions allocate memory to store variable values

*Avoid lazy loading*
* Separate the assembling of graph and executing ops
* Use Python attribute to ensure a function is only 
  loaded the first time it's called


