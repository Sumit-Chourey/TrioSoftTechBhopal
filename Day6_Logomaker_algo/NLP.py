

from transformers import GPT2Tokenizer, GPT2LMHeadModel


tokenizer =GPT2Tokenizer.from_pretrained('gpt2-large')

model= GPT2LMHeadModel.from_pretrained('gpt2-large',pad_token_id=tokenizer.eos_token_id)

tokenizer.eos_token_id  

tokenizer.decode(tokenizer.eos_token_id)

sentence= 'car'
numeric_id=tokenizer.encode(sentence, return_tansors ='pt')

result =model.generate(numeric_id,max_length=100,num_beams=5,no_reat_ngram_size=2, early_stopping=True)

genrated_text=GPT2Tokenizer.decode(result[0],skip_special_tokens=True)

print(genrated_text)
