from functools import reduce
import pickle

from block import Block
from transaction import Transaction

from hash_util import hash_block
from verification import Verification

# Initializing our blockchain list
MINING_REWARD = 10


class Blockchain:
    def __init__(self, hosting_node_id):
        # Initializing the blockchain list
        genesis_block = Block(0, '', [], 100, 0)
        self.chain = [genesis_block]
        self.open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

    def load_data(self):
        """Initialize blockchain + open transactions data from file."""
        try:
            with open('blockchain.p', mode='rb') as file:
                file_content = pickle.loads(file.read())

                self.chain = file_content['chain']
                self.open_transactions = file_content['ot']
        except (IOError, IndexError):
            pass

    def save_data(self):
        try:
            with open('blockchain.p', mode='wb') as file:
                data = {
                    'chain': self.chain,
                    'ot': self.open_transactions
                }
                file.write(pickle.dumps(data))
        except IOError:
            print('Save failed! File not found!')

    def proof_of_work(self):
        last_block = self.chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        verifier = Verification()
        while not verifier.valid_proof(self.open_transactions, last_hash, proof):
            proof += 1
        return proof

    def get_balance(self):
        """Calcualte and return the balance of a participant."""
        participant = self.hosting_node
        tx_sender = [[tx.amount for tx in block.transactions
                      if tx.sender == participant] for block in self.chain]
        open_tx_sender = [tx.amount
                          for tx in self.open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        amount_sent = reduce(lambda tx_sum, tx_amount: tx_sum +
                             sum(tx_amount) if len(tx_amount) > 0 else tx_sum, tx_sender, 0)

        tx_recipient = [[tx.amount for tx in block.transactions
                        if tx.recipient == participant] for block in self.chain]
        amount_received = reduce(lambda tx_sum, tx_amount: tx_sum +
                                 sum(tx_amount) if len(tx_amount) > 0 else tx_sum, tx_recipient, 0)

        return amount_received - amount_sent

    def get_last_blockchain_value(self):
        """ Return the last value of the current blockchain """
        if len(self.chain) < 1:
            return None
        return self.chain[-1]

    def add_transaction(self, recipient, sender, amount=1.0):
        """ Add a new value as well as the las value of the blockchin to the block 

        Arguments:
            :sender: The sender of the coins
            :recipeint: the recipient of the coins
            :amount: The amount of coins sent with the transacion (default = 1.0)
        """
        transaction = Transaction(sender, recipient, amount)
        verifier = Verification()
        if verifier.verify_transaction(transaction, self.get_balance):
            self.open_transactions.append(transaction)
            self.save_data()
            return True

        return False

    def mine_block(self):
        last_block = self.chain[-1]
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        reward_transaction = Transaction(
            'MINNING', self.hosting_node, MINING_REWARD)
        copied_transactions = self.open_transactions[:]
        copied_transactions.append(reward_transaction)
        block = Block(len(self.chain), hashed_block,
                      copied_transactions, proof)
        self.chain.append(block)
        self.open_transactions = []
        self.save_data()
        return True
