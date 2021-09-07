from functools import reduce
import pickle

from block import Block
from transaction import Transaction
from wallet import Wallet

from util.hash_util import hash_block
from util.verification import Verification

# Initializing our blockchain list
MINING_REWARD = 10


class Blockchain:
    def __init__(self, hosting_node_id):
        # Initializing the blockchain list
        genesis_block = Block(0, '', [], 100, 0)
        self.__chain = [genesis_block]
        self.__open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

    def get_chain(self):
        return self.__chain[:]

    def get_open_transactions(self):
        return self.__open_transactions[:]

    def load_data(self):
        """Initialize blockchain + open transactions data from file."""
        try:
            with open('blockchain.p', mode='rb') as file:
                file_content = pickle.loads(file.read())

                self.__chain = file_content['chain']
                self.__open_transactions = file_content['ot']
        except (IOError, IndexError):
            pass

    def save_data(self):
        try:
            with open('blockchain.p', mode='wb') as file:
                data = {
                    'chain': self.__chain,
                    'ot': self.__open_transactions
                }
                file.write(pickle.dumps(data))
        except IOError:
            print('Save failed! File not found!')

    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof

    def get_balance(self):
        """Calculate and return the balance of a participant."""
        if self.hosting_node == None:
            return None
        participant = self.hosting_node
        tx_sender = [[tx.amount for tx in block.transactions
                      if tx.sender == participant] for block in self.__chain]
        open_tx_sender = [tx.amount
                          for tx in self.__open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        amount_sent = reduce(lambda tx_sum, tx_amount: tx_sum +
                             sum(tx_amount) if len(tx_amount) > 0 else tx_sum, tx_sender, 0)

        tx_recipient = [[tx.amount for tx in block.transactions
                        if tx.recipient == participant] for block in self.__chain]
        amount_received = reduce(lambda tx_sum, tx_amount: tx_sum +
                                 sum(tx_amount) if len(tx_amount) > 0 else tx_sum, tx_recipient, 0)

        return amount_received - amount_sent

    def get_last_blockchain_value(self):
        """ Return the last value of the current blockchain """
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]

    def add_transaction(self, recipient, sender, signature, amount=1.0):
        """ Add a new value as well as the las value of the blockchin to the block

        Arguments:
            :sender: The sender of the coins
            :recipeint: the recipient of the coins
            :amount: The amount of coins sent with the transacion (default = 1.0)
        """
        if self.hosting_node == None:
            return False
        transaction = Transaction(sender, recipient, signature, amount)
        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            return True

        return False

    def mine_block(self):
        if self.hosting_node == None:
            return None
        last_block = self.__chain[-1]
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        reward_transaction = Transaction(
            'MINING', self.hosting_node, '', MINING_REWARD)
        copied_transactions = self.__open_transactions[:]
        for tx in copied_transactions:
            if not Wallet.verify_transaction(tx):
                return None
        copied_transactions.append(reward_transaction)
        block = Block(len(self.__chain), hashed_block,
                      copied_transactions, proof)
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
        return block
