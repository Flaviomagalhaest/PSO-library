# -*- coding: utf-8 -*-
import json
class Individuo(object):
    atual = []
    pbest = []
    distAtual = 0
    distPbest = 0
    gbest = False

    # Instância atual e distância do Individuo.
    def __init__(self, atual=None, distAtual=None, json=None):
        if(json == None):
            self.atual = atual
            self.distAtual = distAtual
            self.pbest = atual
            self.distPbest = distAtual
        else:
            self.atual = json['atual']
            self.pbest = json['pbest']
            self.distAtual = json['distAtual']
            self.distPbest = json['distPbest']
            self.gbest = json['gbest']
    
    # Retornando objeto em json.
    def toJson(self):
        jsonRetorno = ''
        jsonRetorno = {
            'atual' : self.atual,
            'pbest' : self.pbest,
            'distAtual' : self.distAtual,
            'distPbest' : self.distPbest,
            'gbest' : self.gbest
        }
        return json.dumps(jsonRetorno)