import json
print=("text")

# date = input ('\n')
numbers = [print]
file_name = 'jsonFile.json'
with open(file_name,'w') as file_obj:
    json.dump(numbers,file_obj)