from flask import Flask, request, jsonify
from huffman_coding import HuffmanCoding

app = Flask(__name__)

@app.route("/compress", methods=["POST"])
def compress():
    input_text = request.form.get("input_text")
    input_filename = "input.txt"
    compressed_filename = "output.compressed"

    with open(input_filename, "w") as file:
        file.write(input_text)

    compressor = HuffmanCoding(input_filename, compressed_filename, "")
    compressor.compress()

    with open(compressed_filename, "r") as file:
        compressed_text = file.read()

    return jsonify({"compressed_text": compressed_text})

@app.route("/decompress", methods=["POST"])
def decompress():
    compressed_text = request.form.get("compressed_text")
    decompressed_filename = "output.txt"

    with open(decompressed_filename, "w") as file:
        file.write(compressed_text)

    compressor = HuffmanCoding("", "", decompressed_filename)
    compressor.decompress()

    with open(decompressed_filename, "r") as file:
        decompressed_text = file.read()

    return jsonify({"decompressed_text": decompressed_text})


if __name__ == "__main__":
    app.run()
