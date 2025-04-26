from tokenizers import Tokenizer, models, trainers, pre_tokenizers

# Create a simple WordLevel tokenizer
tokenizer = Tokenizer(models.WordLevel(unk_token="[UNK]"))
trainer = trainers.WordLevelTrainer(special_tokens=["[UNK]"])
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

# Train from a toy dataset
files = ["sample.txt"]
tokenizer.train(files, trainer)

tokenizer.save("wordlevel-tokenizer.json")