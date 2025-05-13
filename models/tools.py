from random import randint


class Tools:
    def __init__(self, length, options) -> None:
        self.length = length
        self.options = options

    lowers = [chr(i) for i in range(97, 123)]
    uppers = [chr(i) for i in range(65, 91)]
    numbers = [str(i) for i in range(0, 10)]
    hashes = ["#", "$", "%", "&", "@", "´", "~"]
    dots = [".", ":", ",", ";", "'", '"']
    dashes = ["/", "\\", "|", "-", "_"]
    symbols = ["<", ">", "*", "+", "!", "?", "="]
    brackets = ["{", "[", "(", ")", "]", "}"]
    extended = [
        "Ç",
        "ü",
        "é",
        "â",
        "ä",
        "à",
        "å",
        "ç",
        "ê",
        "ë",
        "è",
        "ï",
        "î",
        "ì",
        "Ä",
        "Å",
        "É",
        "§",
        "Æ",
        "ô",
        "ö",
        "ò",
        "û",
        "ù",
        "ÿ",
        "Ö",
        "Ü",
        "¢",
        "£",
        "¥",
        "ƒ",
        "á",
        "í",
        "ó",
        "ú",
        "ñ",
        "Ñ",
    ]

    def get_random(self, arr):
        return str(arr[randint(0, len(arr) - 1)])

    def generated_password(self):
        password = ""
        option = self.lowers
        length = self.length

        while len(password) < length:
            rand_option = self.get_random(self.options)

            match rand_option:
                case "lower":
                    option = self.lowers
                case "upper":
                    option = self.uppers
                case "number":
                    option = self.numbers
                case "hash":
                    option = self.hashes
                case "dots":
                    option = self.dots
                case "dash":
                    option = self.dashes
                case "symbol":
                    option = self.symbols
                case "bracket":
                    option = self.brackets
                case "extended":
                    option = self.extended

            character = self.get_random(option)
            password += character

        return password
