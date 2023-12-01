# # Import necessary libraries
# from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
# # Initialize global variables for the model and processor
# model_id = "openai/whisper-large-v3"

# # Function to load the model into memory
# def load_model():
#     global model, processor, pipe

#     # Load the model and processor
#     model = AutoModelForSpeechSeq2Seq.from_pretrained(
#         model_id, torch_dtype= torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
#     ).to(device)
#     processor = AutoProcessor.from_pretrained(model_id)
#     # Load the pipeline
#     pipe = pipeline(
#         "automatic-speech-recognition",
#         model=model,
#         tokenizer=processor.tokenizer,
#         feature_extractor=processor.feature_extractor,
#         max_new_tokens=128,
#         chunk_length_s=30,
#         batch_size=16,
#         return_timestamps=True,
#         torch_dtype=torch_dtype,
#         device=device,
#     )
# # Function to transcribe audio
# async def transcribe_audio(file):
#     audio_data = await file.read()
#     result = pipe(audio_data)
#     return result["text"]
