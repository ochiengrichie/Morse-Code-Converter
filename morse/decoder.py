from morse.encoder import MORSE_CODE_DICT

REVERSED_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def decode_from_morse(morse_code):
    return ''.join(REVERSED_MORSE_CODE_DICT.get(symbol, '') for symbol in morse_code.strip().split())