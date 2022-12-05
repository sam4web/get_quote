from modules.audio import *
from modules.quote import *


def main():
    quote = get_quote()
    audio_say(quote["text"])


if __name__ == "__main__":
    main()
