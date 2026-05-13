class AlgebraTokenizer:
    def __init__(self):
        self.special_tokens = ["<PAD>", "<SOS>", "<EOS>", "<SEP>", "<UNK>"]
        self.vocab = []
        self.token_to_id = {}
        self.id_to_token = {}

    def build_vocab(self, token_lists):
        self.vocab = self.special_tokens.copy()

        for tokens in token_lists:
            for token in tokens:
                if token not in self.vocab:
                    self.vocab.append(token)

        self.token_to_id = {
            token: i for i, token in enumerate(self.vocab)
        }

        self.id_to_token = {
            i: token for token, i in self.token_to_id.items()
        }

        return self.vocab, self.token_to_id, self.id_to_token

    def encode(self, tokens):
        encoded = []

        for token in tokens:
            if token in self.token_to_id:
                encoded.append(self.token_to_id[token])
            else:
                encoded.append(self.token_to_id["<UNK>"])

        return encoded

    def decode(self, ids):
        tokens = []

        for idx in ids:
            token = self.id_to_token[idx]

            if token == "<EOS>":
                break

            if token in ["<PAD>", "<SOS>"]:
                continue

            tokens.append(token)

        return tokens
