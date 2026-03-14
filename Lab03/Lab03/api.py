from flask import Flask, request, jsonify

app = Flask(__name__)

# Caesar Encrypt
def caesar_encrypt(text, key):
    result = ""
    key = int(key)

    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


# Caesar Decrypt
def caesar_decrypt(text, key):
    result = ""
    key = int(key)

    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char

    return result


@app.route("/api/caesar/encrypt", methods=["POST"])
def encrypt():
    data = request.json

    plain_text = data["plain_text"]
    key = data["key"]

    encrypted = caesar_encrypt(plain_text, key)

    return jsonify({
        "encrypted_message": encrypted
    })


@app.route("/api/caesar/decrypt", methods=["POST"])
def decrypt():
    data = request.json

    cipher_text = data["cipher_text"]
    key = data["key"]

    decrypted = caesar_decrypt(cipher_text, key)

    return jsonify({
        "decrypted_message": decrypted
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)