#!/usr/bin/python3

"""Script assigning the secondary structures of a protein."""

# Loading of modules
import re

import hb2_parsing
import helix_assigment
import sheet_assigment


if __name__ == "__main__":
    res_interacting = hb2_parsing.select_res_interacting("data/hbplus/3zy0_new.hb2")
    hbond_dic = hb2_parsing.create_dico_hbonds(res_interacting)
    turn_res = helix_assigment.select_turn_res(hbond_dic)
    helix_dic = helix_assigment.assign_helix(turn_res) 
    for key in helix_dic:
        chain = "".join(helix_dic[key])
        print(f"Chaine {key} : {chain}")