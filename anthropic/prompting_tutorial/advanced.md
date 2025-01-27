# Advanced

## Chapter 8: Avoiding Hallucinations

- 🧠 **What are hallucinations?**  
  Sometimes Claude will generate text that is inaccurate, untrue, or unjustified. These errors are known as "hallucinations." Hallucinations can range from confidently incorrect facts to imaginary quotes or reasoning that isn’t grounded in the context you’ve provided.

- 🌟 **The good news:**  
  With the right techniques, you can minimize hallucinations and make Claude's responses more grounded and accurate.

### **Techniques to Reduce Hallucinations:**

1. **Give Claude the option to say “I don’t know.”**  
   Sometimes when Claude doesn’t have sufficient information, it tries to answer anyway and ends up hallucinating. You can "give Claude an out" by instructing it:
   - **Example:**  
     *"If you don't know the answer or don’t have enough evidence, respond with 'I don’t know' rather than making an assumption."*
   - This allows Claude to decline questions rather than providing inaccurate guesses.

2. **Ask Claude to find evidence before answering.**  
   For questions based on specific data or documents, prompt Claude to gather evidence and quote directly before forming an answer:
   - **Example Prompt:**  
     ```
     First, extract relevant information or quotes from this document that directly address the question. Then, base your answer on that evidence.
     ```
   - This process ensures that Claude's responses are grounded in verified content rather than fabricated information.

3. **Ask the question at the **bottom** of the text or document.**  
   - Hallucinations in summarization tasks or on long documents occur when Claude generates content before fully understanding the input. By placing the question at the very bottom of your text or document, Claude processes the entire input first.
   - **Best Practice:** Keep the context and instructions together before presenting the question at the end.

4. **Experiment with temperature settings.**  
   Claude can provide more accurate and deterministic answers by adjusting the temperature parameter:  
   - **Low temperature (closer to 0):** Claude produces consistent, factual, and predictable answers. Useful for reducing creativity in factual or technical contexts.  
   - **High temperature (closer to 1):** Responses are more varied and creative but risk hallucinations or less consistent answers. Best for creative tasks.  
   - **Best Practice:** Use temperature 0 for fact-based reasoning or tasks requiring precision.

### **Addressing Hallucinations in Real-World Scenarios**

1. **Q&A on a Document (With Evidence Extraction):**
   - **Prompt Format Example:**  
     ```
     Document: [Place your document here]
     Question: What is the effectiveness of the new policy, based on this document?  
     
     Instructions:
     First, extract any quotes that address the effectiveness of the policy. Then, answer the question based on the quotes.  
     ```
   - By explicitly requiring evidence-backed answers, you'll often prevent Claude from hallucinating unsupported claims.

2. **General Knowledge Questions:**  
   Include explicit instructions allowing Claude to admit uncertainty:
   - **Example Prompt:**  
     ```
     Only answer this question if you are certain of the answer. If you’re unsure or there isn’t sufficient evidence, respond with 'I don’t know.'
     ```

3. **Creative Tasks with Guardrails:**  
   On creative assignments, guide Claude with constraints. Example:
   - **Prompt Example:**  
     ```
     Write a short sci-fi story. Base all scientific details on credible physics principles or note where creativity replaces realism.
     ```

### **Key Takeaways:**

- 🛠️ **Best Practices:**  
  - Provide clear instructions that allow Claude to decline answering if uncertain.  
  - Ask Claude to extract supporting evidence before building an argument or explanation.  
  - Place inputs (e.g., documents or context) above the final question to ensure the model processes all information first.  

- ✔️ **Use Low Temperature for Accuracy:**  
  Lowering response temperature (e.g., setting it to 0) significantly reduces the likelihood of hallucinations for fact-based tasks.

- 🔄 **Iterate and Experiment:**  
  Not all hallucinations are eliminated with a single method. Experimentation with various techniques (e.g., few-shot examples, reasoning chains, formatting) is often necessary to refine Claude's accuracy.

### Exercises

- [exercise_8_1_beyonce_hallucination.py](exercise_8_1_beyonce_hallucination.py)
> Adapt the prompt to fix Claude's hallucination issue by giving Claude an out.
- [exercise_8_2_prospectus_hallucination.py](exercise_8_2_prospectus_hallucination.py)
> Modify the prompt to fix Claude's hallucination issue by asking for citations.


## Chapter 9: Complex Prompts from Scratch - Career Coach Chatbot

- 🧠 **Why use complex prompts?**  
  Complex tasks require precise guidance to align Claude’s behavior, tone, and response formatting. By modularizing prompts into smaller "elements," you can create refined, reusable, and highly effective prompts for a variety of tasks.

### **Recommended Structure for Complex Prompts**

Not all prompts need every element. Start broad, test for success, and simplify by removing unnecessary details later. Below are the 10 recommended **Prompt Elements** to include in your complex prompt.

### **Prompt Elements:**

#### 1. **User Role**  
   - Always begin any Messages API call with a `user` role to provide clarity in conversation.  
   - The function or application framework (e.g., `get_completion()`) typically handles this automatically.

#### 2. **Task Context**  
   - Clearly define Claude’s purpose and role at the very beginning. This helps Claude establish its identity and maintain consistent behavior.  
   - **Example:**  
     ```
     TASK_CONTEXT = "You will be acting as an AI career coach named Joe created by the company AdAstra Careers. Your goal is to give career advice to users visiting the AdAstra website."
     ```

#### 3. **Tone Context**  
   - Specify the tone Claude should use to suit the interaction. While optional, tone plays a critical role in customer-facing or sensitive tasks.  
   - **Example:**  
     ```
     TONE_CONTEXT = "Maintain a friendly and approachable customer service tone."
     ```

#### 4. **Detailed Task Description and Rules**  
   - Outline specific tasks and rules Claude must follow. This section sets boundaries for proper behavior and provides a fallback in ambiguous scenarios.  
   - **Example:**  
     ```
     TASK_DESCRIPTION = """Here are the rules for the interaction:
     - Always stay in character as 'Joe,' the AI career coach.
     - If unsure, respond with: 'Sorry, I didn't understand that. Could you rephrase your question?'
     - Redirect irrelevant inquiries by saying: 'Sorry, I am Joe, and I only provide career advice. Is there a career question I can help you with?'"""
     ```

#### 5. **Examples**  
   - Provide example interactions that Claude can emulate. Examples are incredibly effective in clarifying tone, format, and style. Enclose them in **XML tags** to emphasize structure.  
   - **Example:**  
     ```
     EXAMPLES = """<example>
     <customer> Hi, how were you created and what do you do? </customer>
     <joe> Hello! My name is Joe, and I was created by AdAstra Careers to give career advice. What can I help you with today? </joe>
     </example>
     """
     ```

#### 6. **Input Data to Process**  
   - Include specific data, such as conversational history or user input, in **XML tags**. This helps Claude focus on task-relevant data and ensures accuracy.  
   - **Example:**  
     ```
     INPUT_DATA = f"""<conversation-history>
     {HISTORY}
     </conversation-history>

     <user-question>
     {QUESTION}
     </user-question>
     """
     ```

#### 7. **Immediate Task Description or Request**  
   - Reiterate what Claude needs to do based on the user’s query. Place this “reminder” toward the **end** of your prompt for clarity and precision.  
   - **Example:**  
     ```
     IMMEDIATE_TASK = "How do you respond to the user's question in your role as Joe?"
     ```

#### 8. **Precognition (Think Step by Step)**  
   - For tasks requiring multiple steps, instruct Claude to think methodically before finalizing its answers.  
   - **Example:**  
     ```
     PRECOGNITION = "Before answering, think through the user's question, analyze the context, and ensure your response adheres to the guidelines."
     ```

#### 9. **Output Formatting**  
   - Specify how you want the response formatted (e.g., wrapped in `<XML>` tags, structured as JSON, or plain text). Formatting ensures consistency in outputs, especially for integration into other systems.  
   - **Example:**  
     ```
     OUTPUT_FORMATTING = "Wrap your response in <response></response> tags."
     ```

#### 10. **Prefilling Claude’s Response (if necessary)**  
   - Prefill specific parts of Claude's output to steer its behavior, tone, or phrasing if needed. Often used with API call structures.  
   - **Example:**  
     ```
     PREFILL = "[Joe] "
     ```


### **Use-Case Example: Career Coach Chatbot**

Imagine building a chatbot for **AdAstra Careers**.

- **Example Input:**  
  ```
  HISTORY = "Customer: Can you help me narrow down my career options? Joe: Sure, tell me about your interests."
  QUESTION = "What are some good options for someone interested in technology and problem-solving?"
  ```

- **Example Final Prompt:**  
  ```
  You will be acting as an AI career coach named Joe created by the company AdAstra Careers. Your goal is to give career advice to users visiting the AdAstra website.

  Maintain a friendly and approachable customer service tone.

  Here are the rules for the interaction:
  - Always stay in character as 'Joe,' the AI career coach.
  - If unsure, respond with: 'Sorry, I didn't understand that. Could you rephrase your question?'
  - Redirect irrelevant inquiries by saying: 'Sorry, I am Joe, and I only provide career advice. Is there a career question I can help you with?'

  <example>
  <customer> Hi, how were you created and what do you do? </customer>
  <joe> Hello! My name is Joe, and I was created by AdAstra Careers to give career advice. What can I help you with today? </joe>
  </example>

  <conversation-history>
  Customer: Can you help me narrow down my career options? Joe: Sure, tell me about your interests.
  </conversation-history>

  <user-question>
  What are some good options for someone interested in technology and problem-solving?
  </user-question>

  How do you respond to the user's question in your role as Joe?

  Before answering, think methodically through the user's question, adhere to guidelines, and analyze the context.

  Wrap your response in <response></response> tags.
  ```
  
### exercises

- [exercise_9_1_financial_services_chatbot.py](exercise_9_1_financial_services_chatbot.py)
> Concatenate it all together and see it in action!
- [exercise_9_2_codebot.py](exercise_9_2_codebot.py)
> Write a prompt for a coding assistance and teaching bot that reads code and offers guiding corrections