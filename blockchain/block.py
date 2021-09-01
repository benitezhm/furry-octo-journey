from time import time

class Block:
    def __init__(self, index, previous_hash, list_of_transactions, proof_of_work, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = list_of_transactions
        self.proof = proof_of_work
        self.timestamp = time