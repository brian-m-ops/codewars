def decodeMorse(morse_code):
    return ' '.join(''.join(MORSE_CODE[i] for i in word.split(' ')) for word in morse_code.strip().split("   "))


MORSE_CODE = '.... . -.--   .--- ..- -.. .'  # should return "HEY JUDE"
