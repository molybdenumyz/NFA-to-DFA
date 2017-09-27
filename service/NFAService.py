# -*- coding: utf-8 -*-
from model.Model import FA


def closure(item_set, f=dict, flag=set):
    res = set(item_set)
    for item in item_set:
        if item not in flag:
            flag.add(item)
            if '::e::' in f[item].keys():
                state_set = f[item]['::e::']
                res = res | closure(state_set, f, flag)
    return res


def move(begin_set, bridge, f, flag=set):
    res = set()
    for begin in begin_set:
        if bridge in f[begin].keys():
            state_set = f[begin][bridge]
            res = res | closure(state_set, f, res)
        else:
            continue
    return res


def NFA_to_DFA(nfa=FA):
    dfa = FA(nfa.SIGMA)

    queue = []
    next_temp = closure(nfa.S, nfa.F, set())
    queue.append(next_temp)
    if not next_temp.isdisjoint(nfa.Z):
        dfa.addZ(0)
    dfa.addK(0)
    i = 0
    while i < len(queue):
        for alphabet in nfa.SIGMA:
            next_temp = move(queue[i], alphabet, nfa.F, set())
            if len(next_temp) == 0:
                continue

            # 检查next_temp是否是第一次出现
            exist = False
            if next_temp in queue:
                exist = True
                index = queue.index(next_temp)
            else:
                queue.append(next_temp)
                index = len(queue) - 1
            # 构造F
            if not (dfa.ifIndexInTransiton(i)):
                dfa.createTransition(i)
            dfa.addTransition(i, alphabet, index)
            # 添加K时检查是否为终态
            if not exist:
                dfa.addK(index)
                if not next_temp.isdisjoint(nfa.Z):
                    dfa.addZ(index)
        i = i + 1

    return dfa
