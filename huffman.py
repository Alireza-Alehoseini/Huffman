class HuffmanNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


class TextFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, "r") as file:
            return file.read()

    def write_file(self, content):
        with open(self.filename, "w") as file:
            file.write(content)


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        min_priority = min(self.queue)
        self.queue.remove(min_priority)
        return min_priority

    def is_empty(self):
        return len(self.queue) == 0


class HuffmanCoding:
    def __init__(self, input_filename, compressed_filename, decompressed_filename):
        self.input_filename = input_filename
        self.compressed_filename = compressed_filename
        self.decompressed_filename = decompressed_filename

        self.input_text = None
        self.frequency_dict = {}

        self.huffman_tree = None
        self.code_dict = {}

    def read_input_text(self):
        text_file_handler = TextFileHandler(self.input_filename)
        self.input_text = text_file_handler.read_file()

    def calculate_character_frequencies(self):
        for character in self.input_text:
            if character in self.frequency_dict:
                self.frequency_dict[character] += 1
            else:
                self.frequency_dict[character] = 1

    def construct_huffman_tree(self):
        priority_queue = PriorityQueue()
        for character, frequency in self.frequency_dict.items():
            node = HuffmanNode(character, frequency)
            priority_queue.enqueue(node)

        while not priority_queue.is_empty():
            if len(priority_queue.queue) == 1:
                self.huffman_tree = priority_queue.dequeue()
                break

            node1 = priority_queue.dequeue()
            node2 = priority_queue.dequeue()

            parent_frequency = node1.frequency + node2.frequency
            parent_node = HuffmanNode(None, parent_frequency)
            parent_node.left = node1
            parent_node.right = node2

            priority_queue.enqueue(parent_node)

    def generate_huffman_codes(self, node, code):
        if node.character is not None:
            self.code_dict[node.character] = code
        else:
            self.generate_huffman_codes(node.left, code + "0")
            self.generate_huffman_codes(node.right, code + "1")

    def generate_compressed_text(self):
        compressed_text = ""
        for character in self.input_text:
            compressed_text += self.code_dict[character]
        return compressed_text

    def generate_decompressed_text(self, compressed_text):
        decompressed_text = ""
        current_node = self.huffman_tree

        for bit in compressed_text:
            if bit == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.character is not None:
                decompressed_text += current_node.character
                current_node = self.huffman_tree

        return decompressed_text

    def save_compressed_file(self, compressed_text):
        text_file_handler = TextFileHandler(self.compressed_filename)
        text_file_handler.write_file(compressed_text)

    def save_decompressed_file(self, decompressed_text):
        text_file_handler = TextFileHandler(self.decompressed_filename)
        text_file_handler.write_file(decompressed_text)

    def compress(self):
        self.read_input_text()
        self.calculate_character_frequencies()
        self.construct_huffman_tree()
        self.generate_huffman_codes(self.huffman_tree, "")
        compressed_text = self.generate_compressed_text()
        self.save_compressed_file(compressed_text)
        return compressed_text

    def decompress(self):
        text_file_handler = TextFileHandler(self.compressed_filename)
        compressed_text = text_file_handler.read_file()
        decompressed_text = self.generate_decompressed_text(compressed_text)
        self.save_decompressed_file(decompressed_text)
        return decompressed_text

    def execute_compression_and_decompression(self):
        compressed_text = self.compress()
        decompressed_text = self.decompress()
        return compressed_text, decompressed_text

def run_program():
    input_filename = "test.txt"
    compressed_filename = "test.compressed"
    decompressed_filename = "decompressed_test.txt"

    compressor = HuffmanCoding(input_filename, compressed_filename, decompressed_filename)
    compressor.execute_compression_and_decompression()

if __name__ == "__main__":
    run_program()
