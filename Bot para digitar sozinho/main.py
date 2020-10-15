import time, keyboard
time.sleep(10); word = open('texto.txt', 'r')
for x in word:
    print(word.readline()); #keyboard.write(word.readline())
    time.sleep(0.35); #keyboard.press('enter')
