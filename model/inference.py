import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Step 1 : set the fine tunned model id 

fine_tuned_model = "ft:gpt-3.5-turbo-0125:personal::BRPlm5zt"

# step 3 : listing the 3 new prompts to the test the trained model

test_prompts = [
    "Mujhe ek achha restaurant suggest karo na.",

    "Kal movie night arrange karte hain?",

    "Mummy se pooch lo dinner mein kya banana hai."
] 

# step 4 :Generating the response

for prompt in test_prompts:
    response = openai.chat.completions.create(
        model= fine_tuned_model,
        messages=[
            {"role":"user","content":prompt}

        ],
        temperature=0.7
    )
    reply = response.choices[0].message.content
    print(f"/user :{prompt}")
    print(f"Assistant :{reply}")