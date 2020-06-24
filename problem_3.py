import sys
import heapq

class Node(object):  
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right
    def traverse(self, code = None):
        if code is None:
            code = ""
            
        if isinstance(self.left[2], Node): 
            self.left[2].traverse(code+"0") # left[0] --> freq; left[2] --> child_node
        else:
            Huffman_code[self.left[2][0]] = code+"0" # [freq, id, [symbol]], left[2][0] --> symbol
            
        if isinstance(self.right[2], Node):
            self.right[2].traverse(code+"1") # right[0] --> freq; right[2] --> child_node
        else:
            Huffman_code[self.right[2][0]] = code+"1" # [freq, id, [symbol]], right[2][0] --> symbol
    
def huffman_tree(data):
    if data is None or data is "":
        return data
    # calculating the frequency of each characters
    frequency = {}
    for character in data:
        frequency[character] = frequency.get(character,0) + 1
    # if only contain one character
    if len(frequency) == 1:
        Huffman_code[data[0]] = "0"
        freq = frequency[data[0]]
        left = [freq, id(freq), data[0]]
        return Node(left)
    # generate a min-heap, so as we can pop two least frequent characters in each loop
    heap = []
    for symbol, freq in frequency.items():
        # insert id, in case freq of many characters is similar.
        heap.append([freq, id(symbol), [symbol]])
    heapq.heapify(heap)
    # building huffman tree
    while len(heap) > 1:
        # pop two nodes with least frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # build a new node and push it back to the min-heap
        new_node = Node(left, right)
        heapq.heappush(heap, [left[0]+right[0], id(new_node), new_node])
    # return the tree
    root = heapq.heappop(heap)[2]
    root.traverse()
    return root

def huffman_encoding(data):
    # calculating the frequency of each characters
    if data is None or data is "":
        return data
    encoded = ""
    for character in data:
        encoded = encoded + Huffman_code[character]
    return encoded

def huffman_decoding(data,tree):
    if data is None or data is "":
        return data
    decoded = ""
    current = tree
    for bit in data:
        if bit == "0":
            current = current.left[2]
        if bit == "1":
            current = current.right[2]
        # NOTICE: We should judge whether we reach the leaf node in the end of the loop, not in the beginning
        # otherwise, we will miss the last character
        if not isinstance(current, Node):
            decoded = decoded + current[0]
            current = tree
    return decoded
    
if __name__ == "__main__":
    # Test 1: normal
    print("Test 1")
    Huffman_code = {}
    a_great_sentence = "The bird is the word"
    tree = huffman_tree(a_great_sentence)
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # 69
    # The bird is the word

    encoded_data = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # 36
    # 1011111011000011111011010110100011100100100011101100001010111100101101

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # 69
    # The bird is the word
    
    # Test 2: contain only one characters
    print("Test 2")
    Huffman_code = {}
    a_great_sentence = "AAAAA"
    tree = huffman_tree(a_great_sentence)
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # 54
    # AAAAA

    encoded_data = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # 24
    # 00000

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # 54
    # AAAAA
    
    # Test 3: all characters only appear once
    print("Test 3")
    Huffman_code = {}
    a_great_sentence = "ABCDEF0123456"
    tree = huffman_tree(a_great_sentence)
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # 62
    # ABCDEF0123456

    encoded_data = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # 32
    # 1011101001111101010011010011000000110011101111001

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # 62
    # ABCDEF0123456

    # Test 4: empty string
    print("Test 4")
    Huffman_code = {}
    a_great_sentence = ""
    tree = huffman_tree(a_great_sentence)
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # 49
    # ""

    encoded_data = huffman_encoding(a_great_sentence)
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Empty string cannot use int() with base 2
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # ""

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # 49
    # ""


    # Test 5: None
    print("Test 5")
    Huffman_code = {}
    a_great_sentence = None
    tree = huffman_tree(a_great_sentence)
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # 16
    # None

    encoded_data = huffman_encoding(a_great_sentence)
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # None cannot use int() with base 2
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # None

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # 16
    # None