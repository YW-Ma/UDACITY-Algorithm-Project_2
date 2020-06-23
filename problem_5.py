import hashlib
import datetime

class Block:
    """
    Block:
        Timestamp
        Data
        Hash (from data)
        previous Hash
    """
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calc_hash()
        self.previous_hash = previous_hash
        self.next = None
    
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()
    
    def __repr__(self):
        """
        returns the object representation
        so we can print it or use [block] to record the content of it.
        """
        return f"\nTimestamp: {self.timestamp},\nData: {self.data},\nHash: {self.hash},\nPrev_hash: {self.previous_hash},\n"


class BlockChain:
    """
    (first Block)                        (new Block)
    [head block] --> [block] --> ... --> [tail block]
    NOTICE: The direction of arrow is different from the one given in the intro of the problem
    """
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        """
        To make it clear, this function has two step:
        1. creat a new block [first block doesn't have previous_hash]
        2. append the block to the chain
        """
        # 1. creat a new block
        if data is None or len(data) == 0:
            return
        else:
            if self.head is None:# first Block
                new_block = Block(datetime.datetime.now(), data, 0)
            else:# not first Block (need to include the previous_hash)
                new_block = Block(datetime.datetime.now(), data, self.tail.hash)

        # 2. append the block to the chain
        if self.head is None:
            self.head = new_block
            self.tail = self.head
        else:
            self.tail.next = new_block
            self.tail = self.tail.next
        return
    
    def toList(self):
        """
        output the block chain as a list
        each block is a sub list
        """
        block_chain = []
        current_block = self.head
        while current_block is not None:
            block_chain.append([current_block])
            current_block = current_block.next
        return block_chain

# Test:
if __name__ == "__main__":
    chain_1 = BlockChain()
    data1 = "1. Lemon"
    data2 = "2. Banana"
    data3 = "3. Lychee"
    
    chain_1.append(data1)
    chain_1.append(data2)
    chain_1.append(data3)

    print(chain_1.toList())
    """
    Timestamp: 2020-06-23 15:36:51.502838,
    Data: 1. Lemon,
    Hash: aa69170f0d8783ab73eca291135c4196bb699587f14f1f2df41f55017325ef99,
    Prev_hash: 0,
    ], [
    Timestamp: 2020-06-23 15:36:51.502838,
    Data: 2. Banana,
    Hash: 6565f13ac799b518daa076abb6492b5bcdc2425c9d294c1fca1cf965508578ca,
    Prev_hash: aa69170f0d8783ab73eca291135c4196bb699587f14f1f2df41f55017325ef99,
    ], [
    Timestamp: 2020-06-23 15:36:51.502838,
    Data: 3. Lychee,
    Hash: 843b315517a43a11ff4aebde38d5da817076dedbef2a1cbe7ef0a2c9ac4a5ea7,
    Prev_hash: 6565f13ac799b518daa076abb6492b5bcdc2425c9d294c1fca1cf965508578ca,
    ]]
    """

    chain_2 = BlockChain()
    data1 = ""
    data2 = ""
    data3 = ""
    
    chain_2.append(data1)
    chain_2.append(data2)
    chain_2.append(data3)

    print(chain_2.toList())
    """
    []
    """

    chain_3 = BlockChain()
    data1 = None
    data2 = None
    data3 = None
    
    chain_3.append(data1)
    chain_3.append(data2)
    chain_3.append(data3)

    print(chain_3.toList())
    """
    []
    """