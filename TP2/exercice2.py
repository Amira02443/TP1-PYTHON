def tri_select(tab):
    for i in range(len(tab)-1):
        sous_tab = tab[i:]
        mini=min(sous_tab)
        j = sous_tab.index(mini) + i            
        tab[i], tab[j] = tab[j], tab[i]       
    return tab
print(tri_select([5, 2, 9, 1, 7, 3])) 
