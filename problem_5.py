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
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
    
    def calc_hash(self):
        # encode stamp, data, previous_hash, and data all together.
        # [if only encode data, two same data will have same hash value]
        sha = hashlib.sha256()
        content = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(content.encode('utf-8'))
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
        # We keep the reference of tail of the linked list,
        # so as to achieve O(1) append time.
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
    [[
    Timestamp: 2020-06-24 10:57:59.864151,
    Data: 1. Lemon,
    Hash: f82150e0258eaa3356524b5111cb973d6ae57c894b1819ee1df88c8cb5709f70,
    Prev_hash: 0,
    ], [
    Timestamp: 2020-06-24 10:57:59.865148,
    Data: 2. Banana,
    Hash: ffa30c716f8fd3c1d1c8854aa75d2087f441088104d6673275de81a71fdef1bd,
    Prev_hash: f82150e0258eaa3356524b5111cb973d6ae57c894b1819ee1df88c8cb5709f70,
    ], [
    Timestamp: 2020-06-24 10:57:59.865148,
    Data: 3. Lychee,
    Hash: 37a0b20f5bdff36520d850a606c407b136492fd507a92faa71c7410bf8c32fca,
    Prev_hash: ffa30c716f8fd3c1d1c8854aa75d2087f441088104d6673275de81a71fdef1bd,
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