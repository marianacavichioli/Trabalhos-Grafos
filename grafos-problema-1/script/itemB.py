import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("./src")
from stationary import statDist
from dataset import createFromDataset

# qual a probabilidade de vencer o jogo (o jogador chegar na 36a casa a longo prazo):
w100 = statDist(createFromDataset(), 100)
print("Probabilidade de vencer o jogo em 100 jogadas: "+str(w100[len(w100)-1])) # resposta
print("\n")

# quais os estados mais prováveis de serem acessados?
print("Os 3 estados (vértices) mais prováveis: "+str(w100.argsort()[-3:][::-1]))