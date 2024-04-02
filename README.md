# Finding Collisions in a Weak Hash Function

## Objective
Your task is to find at least one pair of distinct inputs that produce the same output (hash value) when processed through a given weak hash function written in Python.

## Tools and Setup
- **Programming Environment**: Ensure you have access to a Python environment where you can run Python scripts. Tools like IDLE, PyCharm, or Jupyter Notebook are suitable.
- **Provided Hash Function**: [This repository](https://github.com/UCN-LANY-PSI/weak-hash) contains a Python script that implements a weak hash function. Familiarize yourself with how the function works and what its output looks like.

## Task Steps

1. **Review the Provided Hash Function**: Start by understanding the Python script provided by your instructor. Identify the input it expects and how it processes that input to produce a hash.

2. **Plan Your Approach**: Consider how you might find two different inputs that produce the same hash output. Think about whether a brute-force approach or a more analytical strategy would be more effective.

3. **Generate Inputs**: Write a Python script to generate inputs for the hash function. This could involve creating random strings, sequential numbers, or any other data type accepted by the hash function.

4. **Compute Hashes**: Use the provided hash function to compute the hash for each input generated in the previous step. Store the input-hash pairs in a way that makes it easy to identify when two inputs produce the same hash.

5. **Identify Collisions**: Implement a method to detect when two different inputs result in the same hash output. This could involve comparing each new hash to all previously generated hashes or using a data structure like a dictionary to track hash occurrences.

6. **Document Your Findings**: Once you have found at least one pair of inputs that collide, document your inputs and their corresponding hash. Explain your method for finding these collisions and any challenges you faced during the task.

## Deliverables
- **Code**: Submit your Python script(s) used for generating inputs, computing hashes, and identifying collisions.
- **Report**: Provide a brief report detailing the following:
  - The approach you took to find collisions.
  - The pair(s) of colliding inputs you discovered.
  - Any interesting observations or challenges you encountered during the exercise.
  - Your thoughts on the implications of hash collisions in cryptographic applications.

## Tips for Success
- **Experiment with Different Strategies**: Don't hesitate to try both brute-force and analytical methods. Sometimes, understanding the structure of the hash function can lead to shortcuts in finding collisions.
- **Collaborate with Peers**: Discussing strategies with your classmates can provide new insights and approaches to the problem.
- **Consider the Hash Function’s Characteristics**: Pay attention to the characteristics of the hash function that might make it more susceptible to collisions. Understanding its weaknesses will guide your approach.

## Reflection
After completing the task, reflect on how real-world cryptographic hash functions are designed to resist such collision attacks and why ensuring collision resistance is critical for security applications.

This hands-on task will not only deepen your understanding of cryptographic hash functions and their vulnerabilities but also enhance your problem-solving and coding skills in Python.
