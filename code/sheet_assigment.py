""" """
def find_sequential_res(hbond_dic):
    sequential_res = {}

    for key in hbond_dic:
        if key not in sequential_res.keys():
                sequential_res[key] = []
        for i in range(len(hbond_dic[key])-2):
            if ((hbond_dic[key][i+1][1] - hbond_dic[key][i][1]) == 1 and
                (hbond_dic[key][i+2][1] - hbond_dic[key][i+1][1]) == 1):
                    sequential_res[key].append([hbond_dic[key][i][1], hbond_dic[key][i+1][1],hbond_dic[key][i+2][1]])
            
            elif ((hbond_dic[key][i+1][3] - hbond_dic[key][i][3]) == 1 
            and (hbond_dic[key][i+2][3] - hbond_dic[key][i+1][3]) == 1):                          
                    sequential_res[key].append([hbond_dic[key][i][3], hbond_dic[key][i+1][3], hbond_dic[key][i+2][3]])
    return sequential_res

# antiparallel bridge 
def assign_antiparallel_bridge(sequeetial_res, hbond_dic):
    res_bond = []
    for key, value in sequential_res.items():
        for i in range(len(value)-1): 
            for j in range(i+1, len(value)):
                if set(value[i]) & set(value[j]):
                    continue
                else: 
                    list_i = value[i]
                    list_j = value[j]
                    cond_1 = 0
                    cond_2 = 0
                
                    for index in range(len(hbond_dic[key])):
                        to_check = hbond_dic[key][index]
                    
                        if list_i[1] == to_check[1] and cond_1 >= 0:
                            if to_check[3] == list_j[1]:
                                cond_1 += 1
                            else:
                                cond_1 = -2
                        if list_j[1] == to_check[1] and cond_1 >= 0:
                            if list_i[1] == to_check[3]:
                                cond_1 += 1
                            else:
                                cond_1 = -2
                        if list_i[0] == to_check[1] and cond_2 >= 0:
                            if list_j[2] == to_check[3]:
                                cond_2 += 1
                            else:
                                cond_2 = -2
                        if list_j[0] == to_check[1] and cond_2 >= 0:
                            if list_i[2] == to_check[3]:
                                cond_2 += 1
                            else:
                                cond_2 = -2
                    
                        if cond_1 == 2 or cond_2 == 2:
                            res_bond.append([list_i, list_j])
                            break
                        elif cond_1 < 0 and cond_2 < 0:
                            break
    return res_bond                         