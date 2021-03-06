from rich.console import Console
from rich.panel import Panel
from rich.live_render import LiveRender
import sys
import os, shutil
console = Console()

def hata (text):
   console.print(Panel(text, title="🐦Misaki🐦", style="bold white", border_style="bold red"))
   
def bilgi (text):
   console.print(Panel(text, style="white"))
   
def basarili (text):
   console.print(Panel(text, style="white", border_style="green"))
   
def secenek (text):
	console.print(Panel(text, style="bold white", border_style="bold blue"))

def dilsec (text):
    console.print(Panel(text, style="bold magenta", border_style="bold white"))

def lsoru (text):
   console.print(Panel(text, title="🐦", style="bold white", border_style="bold yellow"))  

def onemli (text):
   console.print(Panel(text, style="bold cyan"))

def uyari (text):
   console.print(Panel(text, style="bold cyan", border_style="bold red"))
   
def soru (soru):
   return console.input(Panel(soru, title="🐦", style="bold yellow"))
   
def logo (dil = "None"):
   surum = str(sys.version_info[0]) + "." + str(sys.version_info[1])
   console.print(Panel(f"[bold blue]@MisakiUserBot Installer ✨[/]\n\n[bold cyan]Version: [/][i]1.0[/]\n[bold cyan]Python: [/][i]{surum}[/]\n[bold cyan]Dil: [/][i]{dil}[/]"), justify="center")    




   
def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)

def Sifre(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]

def Sifrele(yazi, key, hexformat=False):
    key, yazi = bytearray(key), bytearray(yazi)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    keystream = Sifre(S)
    return b''.join(b"%02X" % (c ^ next(keystream)) for c in yazi) if hexformat else bytearray(c ^ next(keystream) for c in yazi)