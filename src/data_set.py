import torch
from torch.utils.data import Dataset


class TargetOnlyNextTokenDataset(Dataset):
    def __init__(self, full_token_lists, tokenizer, context_length):
        self.data = []
        self.tokenizer = tokenizer
        self.context_length = context_length
        self.pad_id = tokenizer.token_to_id["<PAD>"]

        for tokens in full_token_lists:
            encoded = self.tokenizer.encode(tokens)

            sep_index = tokens.index("<SEP>")

            for i in range(sep_index + 1, len(encoded)):
                # train only on target-side tokens
                start = max(0, i - self.context_length)

                context = encoded[start:i]

                # left pad to fixed context length
                if len(context) < self.context_length:
                    context = [self.pad_id] * (self.context_length - len(context)) + context

                target = encoded[i]

                self.data.append((context, target))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        context, target = self.data[idx]

        return (
            torch.tensor(context, dtype=torch.long),
            torch.tensor(target, dtype=torch.long)
        )
