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


## Chapter 5: Formatting Output & Speaking for Claude

- 🧠 **What is output formatting?**  
  Output formatting is the practice of instructing Claude to deliver responses in consistent, structured formats, such as XML or JSON, to make them easier to process or integrate into automated workflows.

- 📋 **Why is formatting important?**  
  - **For humans:** Cleanly formatted outputs ensure better readability and structure, especially for complex information.
  - **For machines:** Consistent formats like XML or JSON allow easy parsing, which is crucial if your response needs to feed into another system or program.

- 🏗️ **How can Claude output in XML?**
  Just as you can use XML tags to structure data in prompts, you can ask Claude to wrap its responses in XML tags as well:
  ```
  <response>
      <poem>Roses are red, violets are blue. Here is the output, just for you.</poem>
  </response>
  ```
  - Claude will reliably encapsulate specific data (e.g., poems, summaries, or answers) between XML tags, making post-processing simple.

- 🛠️ **Practical Tip:** Use XML Output with `stop_sequences`  
  When calling Claude via API, add a closing XML tag (e.g., `</response>`) to the `stop_sequences` parameter. This ensures Claude stops generating once the desired content is produced.  
  - **Advantages of this approach:**
    - Saves time by cutting off unnecessary text beyond the desired response.
    - Reduces costs by avoiding extra, unneeded tokens.

- 🌟 **Claude’s versatility with other formats (e.g., JSON):**  
  Claude can output content in JSON format, providing structured and predictable responses. For better control, you can prefill part of the output. For example:
  ```
  {
      "title": "My JSON formatted response", 
      "content": "Example text will go here."
  }
  ```
  By beginning the prompt with an opening bracket `{`, you can guide Claude toward producing properly formatted JSON.

- 🤔 **Why enforce strict formatting?**  
  - **Reliability:** Ensures outputs can be easily processed by scripts or stored in databases.  
  - **Automation:** Formats like JSON allow seamless integration into pipelines for tasks like logging, visualization, reporting, and more.  
  - **Clarity:** Even for end-users, structured output is easier to comprehend and avoids ambiguity.

- 🚧 **Challenges with deterministic outputs:**  
  While Claude is excellent at following formatting instructions, outputs may still require validation for strict adherence, e.g., closing brackets or fully valid JSON. You can include additional checks programmatically.

- ⚙️ **Real-world use cases for formatted output:**
  1. **XML for Human-Readable Data:** Wrapping an article’s title, author name, and content for later parsing:
     ```xml
     <article>
         <title>Formatting Output with Claude</title>
         <author>AI Enthusiast</author>
         <content>This is an example article.</content>
     </article>
     ```
  2. **JSON for APIs or Programs:** Structuring task-focused data:
     ```json
     {
         "summary": "This chapter explains output formatting.",
         "recommendations": ["Use XML or JSON for consistency", "Set stop_sequences to improve efficiency"]
     }
     ```

- 🔄 **Best Practices:**
  1. Be explicit about the format you want (e.g., "output only as JSON, no extra text").
  2. Include examples in the prompt—this greatly helps Claude match the structure closely.
  3. When using the API, use `stop_sequences` strategically to end outputs after the structured portion.

### Exercises

- [exercise_5_1_steph_curry_goat.py](exercise_5_1_steph_curry_goat.py)
> Modify prompt to make a detailed argument that the best basketball player of all time is Stephen Curry.
- [exercise_5_2_two_haikus.py](exercise_5_2_two_haikus.py)
> Modify the haiku prompt to write two haikus about the animal instead of just one. It should be clear where one poem ends and the other begins.
- [exercise_5_3_two_haikus_two_animals.py](exercise_5_3_two_haikus_two_animals.py)
> Modify the haiku prompt to write two haikus about two different animals. 
