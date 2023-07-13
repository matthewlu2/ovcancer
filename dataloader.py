import os

dir_path = r'C:\Users\pamal\Desktop\data\website_feature_by_gene' 

res = []


for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        path = path[:-4]
        res.append(path)

with open('data/textfiles/long_list.txt','w') as tfile:
	tfile.write('\n'.join(res))