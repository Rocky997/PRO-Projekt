from fight import Fight
from bojovnik import Bojovnik

if __name__=="__main__":
    boj1=Bojovnik("Kárl",15,8,100)
    boj2=Bojovnik("Chábr",12,15,80)
    souboj=Fight(boj1,boj2)
    souboj.process(100) # Random value podle ktere se pocita sance na utok prvniho nebo druheho bojovnika