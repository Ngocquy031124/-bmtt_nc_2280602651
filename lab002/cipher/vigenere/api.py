from cipher.vigenere import VigenereCipher

vigenere_cipher = VigenereCipher ()
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
 data = request.json 
 plain_text = data['plain_text']
 key = data['key']
 encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key )
 return jsonify({'encrypted_message': encrypted_text})
@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
 data = request.json 
 cipher_text = data['plain_text']
 key = data['key']
 decrypted_text = vigenere_cipher.vigenere_decrypt(plain_text, key) 
 return jsonify({'decrypted_message': decrypted_text})
