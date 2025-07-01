import argparse
from morse.encoder import encode_to_morse
from morse.decoder import decode_from_morse

def main():
    #choice = input("Do you want to (E)ncode or (D)ecode? ").lower()
    parser = argparse.ArgumentParser(description="Convert text to Morse code or Morse code to text.")

    # Add --encode and --decode as optional arguments
    parser.add_argument('--encode', type=str, help="Text to encode into Morse code")
    parser.add_argument('--decode', type=str, help="Morse code to decode into text")
    parser.add_argument('--encode-from-file', type=str, help="Path to input file to encode")
    parser.add_argument('--decode-from-file', type=str, help="Path to input file to decode")
    parser.add_argument('--output', type=str, help="Path to save the result into a file")

    args = parser.parse_args()
    
    if args.encode:
        result = encode_to_morse(args.encode)

    elif args.decode:
        result = decode_from_morse(args.decode)

    elif args.encode_from_file:
        with open(args.encode_from_file, 'r') as file:
            text = file.read()
            result = encode_to_morse(text)

    elif args.decode_from_file:
        with open(args.decode_from_file, 'r') as file:
            code = file.read()
            result = decode_from_morse(code)

    else:
        print("Please provide --encode, --decode, --encode-from-file, or --decode-from-file. Use -h for help.")
        exit()

    # Output handling
    if args.output:
        with open(args.output, 'w') as file:
            file.write(result)
        print(f"✅ Output saved to {args.output}")
    else:
        print("💬 Result:", result)


if __name__ == "__main__":
    main()