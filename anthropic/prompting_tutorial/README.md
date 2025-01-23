# Anthropic's Prompt Engineering Tutorial

- [Anthropic's Prompt Engineering Interactive Tutorial](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?gid=150872633#gid=150872633)
  - There is also an [answer key](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?usp=sharing)
- [The same as Jupyter Notebooks](https://github.com/anthropics/prompt-eng-interactive-tutorial)

> Golden Rule of Clear Prompting: show your prompt to a colleague or friend and have them follow the instructions themselves to see if they can produce the result you want. If they're confused, Claude's confused.

## Beginner
### Chapter 1: Basic Prompt Structure

🧠 What is a prompt?

A prompt is the instruction or query provided to the AI model to elicit a desired response.

🏗️ What is the basic structure of a prompt? 

The structure generally includes three components: a system prompt, a user message, and the assistant’s response.

🤔 Why use a system prompt? 

A well-crafted system prompt enhances performance, ensuring the AI adheres to rules and instructions effectively.

📊 What does an API call typically consist of? 

At a minimum, it should include "max_tokens" (to limit text length), "messages" (structured content), and "model" (to specify which AI to use).

👶 How do you modify the model’s behavior? 

Edit the system prompt to adjust tone or style—for instance, making the assistant respond like a 3-year-old child.

🔢 Why does User/Assistant formatting matter? 

Clear User/Assistant formatting ensures the AI accurately understands and engages with the provided context.

#### Exercises

- [Exercise 1.1](exercise_1_1_counting_to_three.py) - Counting to Three
> Using proper User/Assistant formatting, write a prompt to get Claude to count to three
- [Exercise 1.2](exercise_1_2_system_prompt.py) - System Prompt
> Make Claude respond like it's a three-year-old child

## Chapter 2: Being Clear and Direct

🧠 **Why is clarity important?** 

Claude performs best when instructions are clear, specific, and straightforward. Without explicit guidance, Claude cannot infer context or fill in missing information.  

🏗️ **How should you approach prompts?** 

Think of Claude as a new employee on their first day: it knows nothing beyond what you explicitly explain. The more precise and detailed you are, the better the responses will be.

🪞 **What’s the "Golden Rule" of clear prompting?** 
If a human friend or colleague would struggle to follow your instructions and achieve the desired output, then Claude will likely struggle too. Test your prompts on others to identify gaps or ambiguity.

🎯 **What makes a good prompt?**
  - Use simple, direct language without unnecessary complexity.
  - State the desired outcome explicitly—don’t assume the model will guess what you want.
  - Provide examples of the format or style you’re looking for when possible.

🤔 **What should you avoid in a prompt?**
  - **Ambiguity:** Avoid vague phrases like "Make it better" without defining "better."
  - **Under-Specification:** Don't leave instructions incomplete—e.g., requesting a summary without specifying the word count, format, or style.
  - **Assumptions:** Don’t expect context or prior knowledge unless explicitly provided.

🌟 **What’s the benefit of clear prompts?** 

They minimize misunderstanding and maximize efficiency. Clear prompts help Claude deliver highly relevant and actionable responses on the first try, saving you time and effort in revising or re-prompting.

🔄 **How can you iterate on unclear prompts?** If a response isn’t what you expected:
  1. Revisit the instructions—were they too abstract or incomplete?
  2. Add clarifications where necessary.
  3. Test again and refine based on the new output.

#### Exercises

- [Exercise 2.1](exercise_2_1_spanish.py) - Spanish
> Adapt the system prompt to make Claude output its answer in Spanish. 
- [Exercise 2.2](exercise_2_2_one_player_only.py) - One Player Only
> Modify the basketball player prompt to responds with ONLY the name of one specific player, with no other words or punctuation.
- [Exercise 2.3](exercise_2_3_write_a_story.py) - Write a Story
> Modify the prompt to response with a story over 800 words

## Extra materials
- Antropic Documentation
  - [System Prompts](https://docs.anthropic.com/en/release-notes/system-prompts)
    - [Youtube](https://www.youtube.com/watch?v=ZQ7gpMVMaKQ)
  - [Use prompt templates and variables](Use prompt templates and variables)
- [Antropic Prompt Library](https://docs.anthropic.com/en/prompt-library/library)