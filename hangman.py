import sys
import random

def hangman(word):
    wrong = 0
    stages = ["",
              "__________       ",
              "|                ",
              "|        |       ",
              "|        O       ",
              "|       /|\      ",
              "|       / \      ",
              "|                ",
              "|                ",
              "|                "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!(終る場合は '9' を入力")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "アルファベット1文字を予想してね (1 letter + Enter key) "
        char = input(msg)
        if char == '9':
            print("\nじゃあ、またね!")
            sys.exit()
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け! 正解は {}.".format(word))
    return win
        

ql = ["cat", "apple", "dog", "orange", "computer", "telephone", "number", "run", "program", "sumo",
      "table", "window", "car", "step", "letter", "hacking", "smile", "laugh", "human", "woman", "peace",
      "door", "chair", "library", "dance", "chance", "delete", "copy", "cut", "excel", "word", "robot", "foot",
      "move", "cpu", "memory", "right", "light", "science", "map", "paint", "draw", "neck", "print",
      "weight", "earth", "radio", "snow", "rainbow", "rain", "dool", "ring", "jupiter", "sun", "moon",
      "saturday", "february", "april", "march", "may", "january", "june", "july", "september", "october",
      "november", "december", "wednesday", "august", "friday", "monday", "gold", "pencil", "color", "view",
      "dictionary", "water", "mountain", "cake", "moon", "super", "power", "clock", "hard", "soft", "usb",
      "house", "mouse", "intel", "game", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
      "original", "text", "mathematics", "poor", "success", "true", "false", "basic", "music", "movie",
      "green", "red", "blue", "yellow", "function", "python", "ruby", "small", "large", "circle", "search",
      "english", "japanese", "sony", "nec", "canon", "nec", "ruby", "mail", "write", "read","open","close",
      "key", "break", "next", "line", "circle", "book", "home", "font", "file", "edit", "menu", "help", "end",
      "image", "address", "eleven", "twelve", "data", "star", "space", "cosmos"
      ]

wc = dc = 0
while True:
    qw = ql[random.randint(0, len(ql)-1)]
    #print(qw)
    if hangman(qw):
        wc += 1
    else:
        dc += 1
    print("\n {} 勝 　{} 敗 です\n\n".format(wc, dc))
