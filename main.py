morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def search_for_key(value):
    for x, y in morse_code_dict.items():
        if y == value:
            return x

def main():
    answer = input("Please state your business (encode/decode): ")

    if answer.lower() == "encode":

        text = input("Please type in your text to encode with morse: ")
        encoded_text = ""
        for x in text:
            encoded_text += morse_code_dict[x.upper()] + " "
            

        print(f"Your encoded message is:{encoded_text}")

    elif answer.lower() == "decode":
        
        text = input("Please type in your message to decode by morse: ").split()
        decoded_text = ""
        for x in text:
            decoded_text += search_for_key(x)

        print(f"Your encoded message is:{decoded_text}")


    else:
        main()

main()


# - --- .-.. --. .- //  tolga