import os, threading, time

def cls():
    os.system("cls" if os.name == "nt" else "clear")

text_list = []

def start_printing(text, delay=5):
    text_list.append("")
    def f(text, delay, n):
        for l in text:
            text_list[n] += l            
            time.sleep(delay)
            cls()
            print("\n".join(text_list))
    thread = threading.Thread(target=f, args=(text, delay, len(text_list)-1))
    thread.start()

start_printing("abcdef")
start_printing('1234')
start_printing('5  6')