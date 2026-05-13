class AlgebraTokenizer:
    def __init__(self):
        self.special_tokens = ["<PAD>", "<SOS>", "<EOS>", "<SEP>", "<UNK>"]
        self.vocab = []
        self.token_to_id = {}
        self.id_to_token = {}

    def split(self, text):
        text = str(text).strip()
        tokens = []
        i = 0

        while i < len(text):
            ch = text[i]

            # handle arrow "->"
            if ch == "-" and i + 1 < len(text) and text[i + 1] == ">":
                tokens.append("->")
                i += 2
                continue

            # skip spaces
            if ch.isspace():
                i += 1
                continue

            # numbers, including multi-digit numbers
            if ch.isdigit():
                num = ch
                i += 1

                while i < len(text) and text[i].isdigit():
                    num += text[i]
                    i += 1

                tokens.append(num)
                continue

            # variables, like x
            if ch.isalpha():
                tokens.append(ch)
                i += 1
                continue

            # operators and parentheses
            if ch in "+-*/^=()":
                tokens.append(ch)
                i += 1
                continue

            # fallback for rare cases
            tokens.append(ch)
            i += 1

        # add explicit multiplication symbols
        new_tokens = []

        for j in range(len(tokens)):
            new_tokens.append(tokens[j])

            if j < len(tokens) - 1:
                a = tokens[j]
                b = tokens[j + 1]

                if (
                    (a.isdigit() and b.isalpha()) or
                    (a.isalpha() and b.isalpha()) or
                    (a == ")" and (b.isalpha() or b.isdigit())) or
                    ((a.isalpha() or a.isdigit()) and b == "(")
                ):
                    new_tokens.append("*")

        return new_tokens

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
