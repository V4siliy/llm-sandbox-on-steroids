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


## Chapter 6: Precognition (Thinking Step by Step)

- 🧠 **Why does “thinking step by step” matter?**  
  Like humans, Claude performs better in complex tasks when given space to methodically process the problem. Rushing straight to an answer often leads to mistakes. By explicitly breaking down processes, Claude becomes more accurate and thoughtful.

- 📋 **What is step-by-step reasoning?**  
  Step-by-step reasoning involves spelling out the thinking process before providing an answer. It’s like asking Claude to “show its work.” This transparency not only improves accuracy but also makes the reasoning more understandable.

- 🏗️ **How can you encourage Claude to think step by step?**
  **Literal instructions:** Explicitly describe the steps Claude should take:
  ```
  First, write the best arguments for each side in <positive-argument> and <negative-argument> XML tags. Then, generate your final answer.
  ```
  - This structure allows Claude to process the problem comprehensively before answering.

- 🎭 **Role prompting can help:**  
  Pairing step-by-step reasoning with role prompting often boosts Claude’s ability to think deeply. For example:
  ```
  Imagine you are an unbiased judge reviewing this case. List the pros and cons step by step before making a final ruling.
  ```

- 🔄 **Why does order matter?**  
  Claude is sometimes **sensitive to the order** of presented arguments. For example, switching the order of “positive” and “negative” arguments might lead Claude to favor the second option—likely due to patterns learned during training. Managing order thoughtfully is crucial for nuanced tasks.

- 💡 **Examples of step-by-step tasks:**  
  1. **Debates/Assessments:** Ask Claude to list arguments on both sides before forming a conclusion.  
     Example:  
     ```
     Brainstorm the pros and cons of remote work in XML tags, then generate your overall assessment.
     ```
  2. **Complex Reasoning:** Build intermediate reasoning steps to solve tricky problems.  
     Example:  
     ```
     Start by brainstorming (in <brainstorm> tags) and list all potential actors born in the year 1956. Then, name a famous movie starring one of them.
     ```

- 🧩 **Breaking things down systematically improves accuracy:**  
  Consider a task where Claude needs to recommend a course of action:  
  ```
  First, identify the potential risks of the project in <risks>. Then, describe the advantages in <advantages>. Finally, provide a well-balanced recommendation.
  ```

- 🚧 **What doesn’t work?**  
  - Asking Claude to “think silently” (i.e., think internally but only share the answer) is ineffective. Thought processes need to be explicitly verbalized within the response.
  
- 🌟 **Why is this powerful?**
  - **Improves outcomes:** Breaking tasks into smaller components helps with focus and accuracy.  
  - **Greater transparency:** Verbalizing the reasoning allows humans to follow and verify the process.  
  - **Consideration of multiple perspectives:** Structured thinking explores all aspects of the task.  

- ⚙️ **Best Practices for Step-by-Step Reasoning:**
  1. **Explicit steps:** Clearly outline the process you want Claude to follow.
  2. **Use XML tags or clear formats:** Make the reasoning process easy to distinguish, both for clarity and parsing.
  3. **Check for subtle biases:** Be mindful of the order in which arguments or options are presented.
  4. **Iterate for refinement:** If answers don’t meet expectations, refine the instructions by including exact examples or restructuring.

### Exercises

- [exercise_6_1_classifying_emails.py](exercise_6_1_classifying_emails.py)
> Sort emails into categories.
- [exercise_6_2_email_classification_formatting.py](exercise_6_2_email_classification_formatting.py)
> Refine the output of the above prompt to yield an answer formatted exactly how we want it.


## Chapter 7: Using Examples (Few-Shot Prompting)

- 🧠 **What is few-shot prompting?**  
  Few-shot prompting involves providing Claude with examples within your prompt to help it understand **how you want it to behave**, or **what kind of output you expect.** It’s a highly effective technique for guiding tone, structure, and accuracy.

- 📋 **Why does it work?**  
  Instead of relying solely on abstract descriptions of desired behavior:
  - **Examples clarify expectations** by directly showing what’s right (or wrong).  
  - **Claude learns by demonstration,** aligning its output style and structure based on the examples provided.

- 🔢 **What do terms like “few-shot” mean?**
  - **Zero-shot prompting:** No examples are provided; only instructions.  
  - **One-shot prompting:** A single example is used.  
  - **Few-shot prompting:** Multiple examples are included to pattern-match behavior.  
  - **n-shot prompting:** “n” refers to the number of examples provided.

- 🎯 **What problems does few-shot prompting solve?**
  1. Ensures correctness by modeling the expected output.  
  2. Enforces structure in complex tasks (e.g., a list, table, or summary).  
  3. Gives Claude clear guidelines for tone, style, or format without detailed explanations.

- ✍️ **A few-shot example for tone and format:**  
  Task: Summarize an article in bullet points.  
  Prompt:  
  ```
  Summarize articles concisely as bullet points:
  
  Example 1:  
  Article: "A new AI model is released with improved capabilities."  
  Summary:  
  - A new AI model has been launched.  
  - It features improved performance.
  
  Example 2:  
  Article: "Scientists discover a new exoplanet similar to Earth."  
  Summary:  
  - A new Earth-like exoplanet has been discovered.  
  - It has potential for supporting life.
  
  Now summarize the following article: "The stock market sees dramatic gains in technology sectors."
  ```

- 🌟 **Why use examples instead of descriptions?**
  - It’s easier for Claude to pattern-match outputs when given examples rather than relying on lengthy descriptions of desired formatting or tone.  
  - Examples act as a “shortcut” to align results with expectations, especially if the task is nuanced or unfamiliar.

- 🔄 **Best practices for few-shot prompting:**
  1. **Choose relevant examples:** Use examples that reflect your task closely to avoid confusion.  
  2. **Keep examples similar in tone and format:** Consistency helps Claude generalize better.  
  3. **Limit cognitive overload:** Fewer, high-quality examples are typically better than overloading the prompt with too many.  
  4. **Position examples thoughtfully:** Place examples near the task for clarity and ensure the formatting is clean.

- 🚧 **Considerations for few-shot prompting:**
  - Be mindful of **token usage.** More examples = higher token cost. Keep examples concise yet effective.  
  - Don’t assume Claude will perfectly mimic every example—it may still need refinement through iterations.  

- 🛠️ **Zero-shot vs. Few-shot in practice:**  
  Compare the performance of a **zero-shot** vs. **few-shot** prompt:  
  - **Zero-shot Prompt:**  
    *"Summarize the article concisely as bullet points."*  
    Claude’s Output:  
    - May follow instructions but potentially misses nuances of style or depth.  
  - **Few-shot Prompt with Examples:**  
    By showing 2-3 concise bullet point examples, Claude is far more likely to stick to the format, improving the accuracy and presentation.

### Exercises

- [exercise_7_1_email_formatting_via_examples.py](exercise_7_1_email_formatting_via_examples.py)
> Edit the PROMPT to use "few-shot" examples of emails + proper classification (and formatting) to get correct answer.
