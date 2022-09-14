    """Script qssigning n-turns and helix.
    """

def select_turn_res(hbond_dic):
    """Selection of residues i making an H-bond with a residue i + 3; 4 or 5.

    Parameters
    ----------
    hbond_dic : dic{str: list[list[str, int, str, int]]}
        Dictionary arranged by chain containing an amino acid and its position 
        making an H-bond with an amino acid and its position.

    Returns
    -------
    dic[str :{list[int]}]
        Dictionary containing for each chain, the positions of the 
        residues making an H-bond with a residue i+3, 4 or 5.
    """
    n = [3, 4, 5]
    turn_dic = {}
    for key in hbond_dic:
        if key not in turn_dic.keys():
            turn_dic[key] = []
        for hbond_couple in hbond_dic[key]:
            if (hbond_couple[1] - hbond_couple[3]) in n:
                turn_dic[key].append(hbond_couple[1])
    return turn_dic

# alpha-helix

def assign_helix(turn_dic):
    """Assignment of helices by the "H", of n-turns by the letter "T".

    Parameters
    ----------
    turn_dic : dic{str :list[int]}
        Dictionary containing for each chain, the positions of the 
        residues making an H-bond with a residue i+3, 4 or 5.

    Returns
    -------
    dic{str : list[str]}
        List containing for each string and at each position the letter 
        "T", "H" or a "-" to assign a helix, an n-turn or no structure 
        of this type. 
    """
    assign_helix_dic = {}

    for key in turn_dic:
        count = 0
        if key not in assign_helix_dic.keys():
            assign_helix_dic[key] = []
        for i in range(len(turn_dic[key])-1):
            if (turn_dic[key][i+1] - turn_dic[key][i]) == 1:
                count += 1
                if count == 2:
                    assign_helix_dic[key].append("H"*2)
                elif count > 2:
                    assign_helix_dic[key].append("H")
            elif (turn_dic[key][i+1] - turn_dic[key][i]) > 1:
                count = 0
                assign_helix_dic[key].append("T")
                space = turn_dic[key][i+1] - turn_dic[key][i]
                assign_helix_dic[key].append("-"*space)            
            else:
                count = 0
                assign_helix_dic[key].append("T") 
    return assign_helix_dic

