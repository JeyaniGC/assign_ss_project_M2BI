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
    _type_
        _description_
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
    """_summary_

    Parameters
    ----------
    turn_dic : _type_
        _description_

    Returns
    -------
    _type_
        _description_
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

