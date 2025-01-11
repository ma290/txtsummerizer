from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

app = FastAPI()

# Define the input data model
class TextInput(BaseModel):
    text: str

@app.post("/summarize/")
async def summarize_text(input_data: TextInput):
    try:
        # Perform text summarization
        summary = summarizer(input_data.text, max_length=130, min_length=30)
        # Return the summary
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        return {"error": str(e)}
