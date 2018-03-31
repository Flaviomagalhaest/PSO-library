"""PSO"""
# -*- coding: utf-8 -*-
import sys
import urllib
import googlemaps
import json
from . import lib
from .PontoClass import Pontos
from .PSOClass import PSO
from .Config import Config_API, Config_PSO

configAPI = Config_API(
{'key' : 'AIzaSyC5wyAhlPFnEheBiT8i-XjpAajZ7i93eVQ',
 'txtEnderecos' : 'C:\\wamp64\\www\\pso\\py\\enderecos.txt',
 'transporte' : 'driving',
 'limitDia' : 2500,
 'limitRequi' : 100 })

configPSO = Config_PSO(
{'nr_indiv' : 10
})

def pso(enderecos):
    gmaps = googlemaps.Client(configAPI.key)

    # Instanciando pontos
    pontos = Pontos(enderecos, gmaps)

    # Criando matriz distância de cada ponto
    #transporte pode ser: driving, walking, bicycling, transit
    pontos.calcMatrixDist(configAPI.transporte, configAPI.limitDia, configAPI.limitRequi)

    # Instânciando classe PSO
    pso = PSO(configPSO, len(pontos.lista), pontos)

    # Gera Iterações
    return lib.SerializarObjJSON(pso.gera_iteracoes(200))






