from fastapi import FastAPI
from preproc_base_data.summerizer.summ import sshleifer_summarize  # Import the summerize function

from fastapi.middleware.cors import CORSMiddleware

from .summerize import load_model



app = FastAPI()

# Load model on startup
@app.on_event("startup")
async def startup_event():
    load_model()



@app.get("/")
async def root_endpoint():
    # Use the transcribe_audio function from your transcriber module
    return {"message": "Hello World"}


@app.post("/summarize/")
async def summarize_text(item: dict):
    summarized_text = sshleifer_summarize(item['text'])
    return {"summary": summarized_text}














# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
# # configure CORS
# origins = [
#     "http://localhost:3000",  # React's default port
#     "http://127.0.0.1:3000",
#     "*"
#     # Add other origins if necessary
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,  # List of allowed origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all methods
#     allow_headers=["*"],  # Allow all headers
# )
