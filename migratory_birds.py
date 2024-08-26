def migratory_birds(array_id):
    id_list = []
    for item in array_id:
        if item not in id_list:
            id_list.append(item)
            
    sorted_id_list = sorted(id_list)
    appearance, most_appearance = 0, 0
    for id in sorted_id_list:
        appearance = array_id.count(id)
        if appearance > most_appearance:
            id_most_appeared = id
            most_appearance = appearance
    
    return id_most_appeared
