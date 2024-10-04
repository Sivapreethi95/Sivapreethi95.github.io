my_dict ={"a":5,"b":12, "c":7,"d":15}
filtered_dict ={}
for key,values in my_dict.items():
    if values <=10:
        filtered_dict[key]=values
print(filtered_dict)