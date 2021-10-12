import torch
from transformers import BertTokenizerFast, EncoderDecoderModel
import pandas as pd

device = 'cuda' if torch.cuda.is_available() else 'cpu'
ckpt = 'mrm8488/bert2bert_shared-german-finetuned-summarization'
tokenizer = BertTokenizerFast.from_pretrained(ckpt)
model = EncoderDecoderModel.from_pretrained(ckpt).to(device)


def generate_summary(text):
    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)
    output = model.generate(input_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)


data = pd.read_csv('VideoStatisiken/HandOfBloodStatsSubtitles', index_col=0)

data["summary"] = data["subtitles"].apply(lambda x: generate_summary(x))
data.to_csv('summary_test')
