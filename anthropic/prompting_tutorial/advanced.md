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