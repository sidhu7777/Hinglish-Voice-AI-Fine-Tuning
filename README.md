
# Hinglish Voice-AI Fine-Tuning Mini-Project

## Project Overview

In this mini-project, I fine-tuned a Language Model (LLM) to better understand Hinglish (code-switched Hindi + English) conversations.  
The goal was to adapt the base model `gpt-3.5-turbo` to generate fluent, natural replies in Hinglish by creating and using a small custom dataset.

---

## Objectives

- Assemble a small Hinglish conversational dataset.
- Fine-tune a base OpenAI model (`gpt-3.5-turbo`) using the dataset.
- Generate sample outputs using the fine-tuned model.
- Justify model choice, dataset design, and prompt formatting decisions.

---

## Project Structure

```
dataset.jsonl          # 20 examples for fine-tuning
model/
 ├── fine_tune.py      # Script to upload dataset and start fine-tuning
 ├── inference.py      # Script to test the fine-tuned model
.env                    # API Key storage (ignored by Git)
requirements.txt        # Required libraries (openai, python-dotenv)
README.md               # Project explanation
```
````

---

## Setup Instructions

1. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your OpenAI API key:

   ```
   OPENAI_API_KEY=your-openai-key-here
   ```

3. Fine-tune the model:

   ```bash
   python model/fine_tune.py
   ```

4. Test the fine-tuned model:
   ```bash
   python model/inference.py
   ```

---

## Dataset Selection & Size

I created 20 Hinglish prompt-response examples, covering a wide range of conversational topics:

- Basic greetings
- Planning and schedules
- Daily life discussions
- Requests and emotional expressions
- Light humor

The dataset was designed to:

- Keep prompts short and natural (1–2 lines)
- Mimic real-world casual Hinglish speaking style (mix of Hindi and English)
- Cover different domains (food, weather, plans, emotions)

**Why this dataset?**

- A varied dataset helps the model generalize better, even from just 20 examples.
- Short prompts and completions fit well within token limits for small fine-tunes.
- Hinglish code-switching patterns were kept realistic based on how users actually speak.

**Example entry format:**

```json
{
  "messages": [
    { "role": "user", "content": "Kaise ho?" },
    { "role": "assistant", "content": "Main theek hoon, aur tum?" }
  ]
}
```

Each example uses a `messages` list with clear `role: user` and `role: assistant`, matching OpenAI's fine-tuning requirements.

---

## Model and Hyperparameter Choices

**Model Selected:**

- `gpt-3.5-turbo-0125`

**Reason:**

- `gpt-3.5-turbo` is optimized for conversational applications.
- It requires `messages`-based input/output format, matching our project needs.
- It is cheaper and faster compared to older models like `davinci`.

**Fine-tuning Settings:**

- **Epochs:** 2
- **Learning Rate:** Default (auto-tuned by OpenAI)

**Why these settings?**

- Dataset size is small (20 examples). Two epochs are sufficient to learn without overfitting.
- OpenAI auto-tuning of learning rate ensures efficient optimization without manual tuning.

---

## Prompt Formatting and Generation Settings

**Prompt format used during inference:**

- Role-based message list (`role: user`, `content: <prompt>`).
- Used casual Hinglish text to test natural responses.

**Example during inference:**

```python
messages = [
    {"role": "user", "content": "Mujhe ek achha restaurant suggest karo na."}
]
```

**Temperature setting during inference:**

- `temperature = 0.7` (to allow slight creativity in Hinglish replies without making them random).

---

## Sample Outputs

After fine-tuning, I tested 3 new prompts not seen during training.

**Prompt 1:**

> User: Mujhe ek achha restaurant suggest karo na.  
> Assistant: Kyo na The Big Chill Cafe try karein? Unka pasta aur desserts bahut famous hain.

**Prompt 2:**

> User: Kal movie night arrange karte hain?  
> Assistant: Haan, kis genre ki movies dekhni hain?

**Prompt 3:**

> User: Mummy se pooch lo dinner mein kya banana hai.  
> Assistant: Mummy: Aaj dinner mein paneer butter masala, dal tadka, bhindi fry, roti aur rice hai.

---

## Evaluation Plan

If deployed in production, I would evaluate the fine-tuned model by:

- **Human Review:**  
  Regularly sampling outputs and checking fluency, correctness, and Hinglish naturalness.

- **Automated Metrics:**  
  Track completion lengths, language usage ratios, and user feedback scores.

- **Retraining Strategy:**  
  Expand dataset periodically with new examples if accuracy drops or user queries diversify.

---
