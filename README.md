# RogueSpeared:  *WAV + XOR Encrypted Python 'Polyglot' File Generator*

**Non-malicious, safe to execute, and for educational and/or red-teaming purposes only.**

This repo contains a Python-based tool to generate fully functional polyglot files that are both:
- Valid **WAV audio files**
- Executable **Python scripts** with encrypted payloads
---

##  Features
- Uses **any real WAV file** as base
- XOR-encrypts the payload (with optional custom key)
- Base64-encodes the XOR'd payload for storage
- Self-decrypts and executes the payload on runtime
- Sandbox-aware (checks for minimal process count)
- Subprocess-based execution (payload dropped to tempfile and run)
- Maintains clean WAV playback in media players

---

## Files
- `generate_polyglot_wav.py`: The generator script
- `input.wav`: Your real WAV audio file
- `payload.py`: Python payload to be embedded
- `polyglot.wav`: Output file (both WAV and executable Python)

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
This produces `polyglot.wav`.

---

## Execution
### Play it:
```bash
start polyglot.wav        # Windows
vlc polyglot.wav          # Linux/Mac
```

### Run it:
```bash
python polyglot.wav
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

## ⚠Ethics & Legal
This is a proof-of-concept for educational and red team use **only**.
- Do **not** use this to bypass security or deceive users without consent.
- Mark all payloads clearly as safe/demo in professional use.

---

## Credits
Built with boundless, unrequited love for red teams, portfolio builders, and those who enjoy creative file abuse.

---

Want payload presets, CLI flags, or GitHub Actions support? PRs welcome!
