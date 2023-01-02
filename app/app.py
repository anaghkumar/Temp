import hashlib


class NaturalCoinBlock:
    def __init__(self, prev_block_hash, transaction_list):
        self.prev_block_hash = prev_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + prev_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Anna sends 2 NC to Bob"
t2 = "Bob sends 3.1 NC to Mike"
t3 = "Mike sends 5.3 NC to Anna"
t4 = "Daneil sends 2.2 NC to Mike"
t5 = "Mike sends 8 NC to Daneil"
t6 = "Ruke sends 12 NC to Mike"

initial_block = NaturalCoinBlock("Initial String", [t1, t2])
print(initial_block.block_data)
print(initial_block.block_hash)


second_block = NaturalCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)


third_block = NaturalCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)
