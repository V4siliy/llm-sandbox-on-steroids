# Prompts

## Settings

### Temperature

Control randomness.

> Temperature is like a chaos knob for AI.

Low temperature: AI plays it safe, sticks to the most likely words. It's like your buddy who always orders the same course.

High temperature: AI gets wild, considers crazier options. It's like your friend who tries random cocktails every time.

When to use:
- Low temp: For serious stuff like answering facts or giving instructions. You want the AI to be boring but correct.
- High temp: For creative things like writing poems or coming up with wild ideas. Let the AI go nuts!

### Top P

Top P (or nucleus sampling) is like a smart bartender for words. It picks the most likely words until their combined probability hits a set limit (P). This keeps AI text diverse and natural.
If you are looking for exact and factual answers keep this low. If you are looking for more diverse responses, increase to a higher value.

> The general recommendation is to alter temperature or Top P but not both.

### Max Length

You can manage the number of tokens the model generates by adjusting the max length. Specifying a max length helps you prevent long or irrelevant responses and control costs.

### Stop Sequences

A string that stops the model from generating tokens.

### Frequency Penalty
Imagine you're at a party, and every time you say a word, you have to pay a buck. The more you use a word, the more it costs. That's what frequency penalty does to the AI. It makes the AI less likely to repeat words it's already used a lot. The higher this penalty, the more the AI tries to use different words.

### Presence Penalty
At the same party, you gotta pay a flat fee every time you use a word you've said before. Doesn't matter if you've said it twice or ten times, you pay the same. That's presence penalty. It stops the AI from repeating the same thing over and over. If you want the AI to get creative and mix things up, crank this up. If you need it to stay on topic, keep it low.

> Tip: Mess with either frequency penalty or presence penalty, but not both at the same time. That's how you keep your AI responses smooth

There are some prompts that I'm using on a daily basis.

## Examples

### Bre (Russian)

> Давай зажжём 🔥 Что там у тебя на уме?

- [bre.md](bre.md)
- [bre.py](bre.py)

### Summariser

> Hello, I'm a summary profi. What can I do for you today?
> 
- [summarizer.md](summarizer.md)
- [summarizer.py](summarizer.py)

### Five experts

> Hello! What's your question?

- [experts.md](experts.md)
- [experts.py](experts.py)

### Grammar checker

> Something that improves sentences

- [grammar.md](grammar.md)
- [grammar.py](grammar.py)