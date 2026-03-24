from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "facebook/nllb-200-distilled-600M"
batch_size = 20

tokenizer = AutoTokenizer.from_pretrained(model_name, src_lang="hin_Deva")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def translate_text(batch):
    inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True)

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids("eng_Latn")
    )

    translation = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)

    print(translation[0]) 