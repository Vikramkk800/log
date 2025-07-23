from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "t5-small"

print("Downloading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

tokenizer.save_pretrained("t5-small")
model.save_pretrained("t5-small")

print("Model downloaded and saved to ./t5-small")

