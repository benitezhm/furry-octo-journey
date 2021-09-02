from time import time
from util.printable import Printable


class Block(Printable):
    def __init__(self, index, previous_hash, list_of_transactions, proof_of_work, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = list_of_transactions
        self.proof = proof_of_work
        self.timestamp = time() if timestamp is None else timestamp

