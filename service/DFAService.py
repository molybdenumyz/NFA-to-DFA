# -*- coding: utf-8 -*-
from model.Model import FA


def not_slice(state_for_test, state_now, sigma, f, p):
    for alphabet in sigma:
        for state_set in p:
            # 没有指向终态
            if f[state_for_test][alphabet] in state_set:
                if f[state_now][alphabet] in state_set:
                    break
                else:
                    return False
    return True


def simplify(dfa=FA):
    simple_dfa = FA(dfa.SIGMA)
    simple_dfa.setF(dfa.F)
    simple_dfa.setK(dfa.K)
    simple_dfa.setS(dfa.S)
    simple_dfa.setZ(dfa.Z)
    p = [dfa.K ^ dfa.Z, dfa.Z]
    update = True
    while update:
        for state_set in p:
            update = False
            if len(state_set) == 1:
                continue
            state_for_test = state_set.pop()
            # 只是为了拿出其中的一个元素,放回去是为了防止弹出后转移到该状态的搜索不到
            state_set.add(state_for_test)
            new_temp_set = {state_for_test, }
            for state in state_set:
                # 判断该集合是否需要分割，相同的放在一个集合里
                if not_slice(state_for_test, state, simple_dfa.SIGMA, simple_dfa.F, p):
                    new_temp_set.add(state)
            p.append(new_temp_set)
            # 在s中删除同时在s和new中的项目，如{1,2,3,4} 和 {1，3} 消去 {1，3}
            state_set.difference_update(new_temp_set)
            if (len(state_set) == 0):
                p.remove(set())
            else:
                update = True
                break

    for state_set in p:
        if len(state_set) == 1:
            continue
        else:

            state_for_test = state_set.pop()

            for state in simple_dfa.K:
                for item in simple_dfa.F[state].keys():
                    if simple_dfa.F[state][item] in state_set:
                        simple_dfa.F[state][item] = state_for_test

            for state in state_set:
                for item in simple_dfa.F[state]:
                    simple_dfa.F[state_for_test][item] = simple_dfa.F[state][item]
                # 删除多余节点
                simple_dfa.F.pop(state)
                simple_dfa.K.remove(state)
                simple_dfa.Z.discard(state)
                if state == 0:
                    simple_dfa.S = state_for_test

    return simple_dfa
