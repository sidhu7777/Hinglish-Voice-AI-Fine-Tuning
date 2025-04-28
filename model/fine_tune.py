import os
from dotenv import load_dotenv
import openai 
import time


# step 1: loading the openai api keys  from the .env 

load_dotenv()
openai_api_key =os.getenv("OPENAI_API_KEY")


# step 2 : upload the dataset file "dataset.jsonl"
with open("dataset.jsonl","rb") as f:
    upload_response = openai.files.create(
      file=f,
      purpose= "fine-tune"
)

file_id = upload_response.id
print(f"Uploaded file ID: {file_id}")


# step 3 : start fine tuning the model "gpt-3.5-turbo"

fine_tune_job = openai.fine_tuning.jobs.create(
    training_file=file_id,
    model="gpt-3.5-turbo",
    hyperparameters={
      "n_epochs":2
    }
)
print(f"Fine-tune response ID: {fine_tune_job.id}")

# Step 4 checking the job status 
print("\n Checking the job status ---")

while True:
    job_status = openai.fine_tuning.jobs.retrieve(fine_tune_job.id)
    status= job_status.status
    print(f"Current Status :{status}")
    if status in ["succeeded","failed"]:
        print(f"Final Status :{status}")
        if status == "succeeded":
            print(f"Fine-tuned Model : {job_status.fine_tuned_model}")
        break
    time.sleep(10)    