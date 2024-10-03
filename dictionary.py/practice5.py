dict1 ={"a":1,"b":2}
dict2 ={"b":3,"c":4}
merged_dict = dict1.copy()
for key,values in dict2.items():
    if key in merged_dict:
        merged_dict[key] = merged_dict[key]+values
    else :
        merged_dict[key] = values
print(merged_dict)