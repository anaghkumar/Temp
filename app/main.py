import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="Genesis Node 15/Nov/2022 .", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            # 'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):

        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash


blockchain = Blockchain()
t1 = blockchain.new_transaction("Arpit", "Aditya", '5 BTC')
t2 = blockchain.new_transaction("Aditya", "Arpit", '1 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Suman", "Alu", '1 BTC')
t5 = blockchain.new_transaction("Mukesh", "Arjun", '0.5 BTC')
blockchain.new_block(6789)

print("Genesis block: ", blockchain.chain)
