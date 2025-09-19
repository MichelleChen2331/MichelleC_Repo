csv_lines = []

file = open("handles-n-quacks.csv")

file_contents = file.read()

file_lines = file_contents.split("\n")

file_lines = file_lines[0:len(file_lines)-1]

dict_list_A_H = {}
dict_list_H_N = {}
dict_list_N_Z = {}

file_sorted = []

count = 0

sublist = []
subdict = {}
for line in file_lines:
	line_contents = line.strip().split(",")
	sublist.append(line_contents[1].lower().strip())
	subdict.update({line_contents[1].lower(): line_contents[2]})
	count+=1

sublist.sort()

count = 0
for name in sublist:
       if (count < len(file_lines)/3):
                dict_list_A_H.update({name:subdict[name]})
       elif (count < 2*len(file_lines)/3):
               dict_list_H_N.update({name:subdict[name]})
       else:
                dict_list_N_Z.update({name:subdict[name]})
       count+=1

print(dict_list_A_H)
print(dict_list_H_N)
print(dict_list_N_Z)
