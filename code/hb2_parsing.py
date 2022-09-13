    """Script that parses an .hb2 file and retrieves in dictionary form the pairs of residues and their positions involved in H-bonds.
    """
def select_res_interacting(filename):
    """Parse an .hb2 file to retrieve lines containing H-bonds.

    Parameters
    ----------
    filename : str
        File containing all residues involved in H-bonds found 
        by the hbondplus software.

    Returns
    -------
    list[str]
        List containing all the lines of the .hb2 file containing H-bonds 
        between two residues.
    """
    with open(filename, "r") as filin:
        lines = filin.readlines()
        content = lines[8:]
        hbond_content = []

        for line in content: 
            line.strip()
            if line[0] == line[14]:
                hbond_content.append(line.rstrip("\n"))
            else:
                continue
    return hbond_content

# Dico pour accéder à chaque chaine
def create_dico_hbonds(hbond_content):
    """Create a dictionnary containing every residues interacting in H-bond.

    Parameters
    ----------
    hbond_content : list[str]
        List containing all the lines of the .hb2 file containing H-bonds 
        between two residues.
        
    Returns
    -------
    dic{str: list[list[str, int, str, int]]}
        Dictionary arranged by chain containing an amino acid and its position 
        making an H-bond with an amino acid and its position.
    """
    hbond_dic = {}
    for bond in hbond_content:
        clean_bond = bond.split()[0:3]
        # crée un filtre pour récup chaine, position, residus
        # la capture se fait avec les parenthèses
        regex = re.compile("^([A-Za-z]+)([0-9]+)-([A-Za-z]{3})") 
        filtering_left = regex.search(clean_bond[0])
        filtering_right = regex.search(clean_bond[2])

        #.group(0) = à toute la str
        # chaque group récupérer le contenu entre parenthèse
        chain = filtering_left.group(1)
        pos_left = filtering_left.group(2)
        res_left = filtering_left.group(3)
        pos_right = filtering_right.group(2)
        res_right = filtering_right.group(3)

        # si nouvelle chaine on l'ajoute une nouvelle entrée au dico
        if chain not in hbond_dic.keys():
            hbond_dic[chain] = []

        # on ajoute à la chaine notre couple de résidus
        hbond_dic[chain].append([res_left, int(pos_left), res_right, int(pos_right)])
    return hbond_dic