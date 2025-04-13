# RogueSpeared:  WAV + XOR Encrypted Python 'Polyglot' File Generator

**Non-malicious, safe to execute, and for educational and/or red-teaming purposes only.**

This repo contains a Python-based tool to generate fully functional polyglot files that are both:
- Valid **WAV audio files**
- Executable **Python scripts** with encrypted payloads

Perfect for red teaming, security demos, or portfolio proof-of-concepts.

---

## Features
- Uses **any real WAV file** as base
- XOR-encrypts the payload (with optional custom key)
- Base64-encodes the XOR'd payload for storage
- Self-decrypts and executes the payload on runtime (from EOF)
- Sandbox-aware (basic detection using `psutil`)
- Subprocess-based execution (payload dropped to tempfile and run)
- Maintains clean WAV playback in media players (WAV structure untouched at beginning)

---

## Files
- `generate_polyglot_wav.py`: The generator script
- `input.wav`: Your real WAV audio file
- `payload.py`: Python payload to be embedded
- `polyglot_final.wav`: Output file (WAV + executable Python)

---

## Usage
### 1. Prepare your files:
- Supply any `.wav` file as `input.wav`
- Write your Python code in `payload.py`

Example `payload.py`:
```python
print("🎯 This ran from inside a WAV file! You got ROGUE SPEARED!")
```

### 2. Run the generator
```bash
python generate_polyglot_wav.py
```
This produces `polyglot_final.wav`.

---

## Execution
### Play it:
```bash
start polyglot_final.wav        # Windows
vlc polyglot_final.wav          # Linux/Mac
```

### Run it:
```bash
python polyglot_final.wav
```

---

## Advanced
### XOR Key Customization
You can pass your own XOR key:
```python
xor_key = b"\x12\x34\x56\x78\x9A\xBC\xDE\xF0"
```

Or let the script randomize it (default behavior).

---

## Dependencies
This PoC is mostly self-contained, but the sandbox check uses:
```bash
pip install psutil
```

If not installed, the script simply skips sandbox detection.

---

## Ethics & Legal
This is a proof-of-concept for educational and red team use **only**.
- Do **not** use this to bypass security or deceive users without consent.
- Mark all payloads clearly as safe/demo in professional use.


---

## Credits
Built with boundless, unrequited love for red teams, portfolio builders, and those who enjoy creative file abuse.

---
