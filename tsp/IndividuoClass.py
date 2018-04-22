# -*- coding: utf-8 -*-
import json
class Individuo(object):
    atual = []
    pbest = []
    distAtual = ''
    distPbest = ''
    gbest = False

    # Instância atual e distância do Individuo.
    def __init__(self, atual, distAtual):
        self.atual = atual
        self.distAtual = distAtual
    
    # Retornando objeto em json.
    def toJson(self):
        jsonRetorno = ''
        jsonRetorno = {
            'atual' : self.atual,
            'pbest' : self.pbest,
            'distAtual' : self.distAtual,
            'distPbest' : self.pbest,
            'gbest' : self.gbest
        }
        return json.dumps(jsonRetorno)