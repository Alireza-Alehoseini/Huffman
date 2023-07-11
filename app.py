from flask import Flask, request, jsonify
from huffman import HuffmanCoding

app = Flask(__name__)

@app.route('/compress', methods=['POST'])
def compress():
    text = request.form['text']
    compressor = HuffmanCoding(text)
    compressed_text = compressor.compress()
    return jsonify(compressed_text)

@app.route('/decompress', methods=['POST'])
def decompress():
    text = request.form['text']
    compressor = HuffmanCoding(text)
    decompressed_text = compressor.decompress()
    return jsonify(decompressed_text)

if __name__ == '__main__':
    app.run()
