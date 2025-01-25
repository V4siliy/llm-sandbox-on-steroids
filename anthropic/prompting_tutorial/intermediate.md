# Intermediate

## Chapter 4: Separating Data from Instructions

- 🧠 **What is prompt templating?**  
  Prompt templating is the process of creating a reusable "skeleton" for prompts where fixed instructions are separated from variable data inputs.

- 📋 **Why use prompt templates?**  
  - **Efficiency:** If you need to perform repetitive tasks with changing data, templating avoids rewriting the entire prompt each time. 
  - **User-friendly:** Third-party users can provide simple input (like variables) without needing to interact with or understand the full prompt structure.
  - **Flexibility:** Enables clean, scalable workflows for building dynamic prompts.

- 🏗️ **How does it work?**
  1. **Create the skeleton prompt:** Write the fixed instructions, adding placeholders for variable inputs using a defined format (e.g., `{{variable}}`). 
  2. **Substitute user inputs:** Replace placeholders with specific data programmatically or manually before sending the prompt.

- ✍️ **Example Prompt Template:**
  ```
  Write a story about {{animal}} in {{location}} describing its sound and surroundings.
  ```
  - If substituted with `{{animal}} = 'dog'` and `{{location}} = 'park'`, the final prompt becomes:  
    *"Write a story about a dog in a park describing its sound and surroundings."*

- 🔄 **How to substitute inputs?**
  - **In spreadsheets:** You can replace placeholders (e.g., `{{data}}`) using formulas in Excel, Google Sheets, or other tools.
  - **In code:** Use double curly brackets (e.g., `{{variable}}`) as placeholders and build scripts to insert the variable values dynamically.

- 💡 **Best Practices for Substitution:**
  - **Clarity:** Write variable names that are descriptive yet concise (e.g., `{{user_query}}` or `{{topic_name}}`).
  - **Structure:** Keep instructions clear and concise to maintain focus on the dynamic data.
  - **Validation:** Test your template with multiple substitution examples to ensure consistency.

- 🛠️ **Advanced Techniques with XML Wrapping:**  
  Wrapping inputs in **XML tags** makes templates cleaner and avoids unexpected artifacts in Claude's output. For example:
  
```xml
<animal>dog</animal>
<location>park</location>
```

- 🌟 **Why is this powerful?**
  - **Customizability:** You can use the same functional "template" across multiple scenarios with minimal effort, just by swapping variables.
  - **Consistency:** Ensures instructional clarity regardless of variable inputs while keeping Claude focused on core tasks.

- 🤔 **How many variables can you use?**  
  There’s no hard limit—your template can include as many variables as needed, allowing you to build highly detailed and dynamic prompting systems.

- ⚙️ **Real-World Use Cases:**
  - Creating dynamic survey invitations that change based on user input.
  - Automating reports by substituting key data points per recipient.
  - Coding workflows where inputs dynamically populate templates for repeated AI tasks (e.g., summarization or generation tasks).

### Exercises

- [exercise_4_1_haiku_topic.py](exercise_4_1_haiku_topic.py)
> Write a prompt with a haiku about the topic								
- [exercise_4_2_dog_question_with_typos.py](exercise_4_2_dog_question_with_typos.py)
> Fix the prompt by adding XML tags
- [exercise_4_3_dog_question_part_2.py](exercise_4_3_dog_question_part_2.py)
> Fix the prompt WITHOUT adding XML tags. Instead, remove only one or two words from the prompt.
