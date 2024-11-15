import os


names_of_files = ['1.txt', '2.txt', '3.txt']
folder_path = os.getcwd()

list_of_files = list((filter (lambda i: i in os.listdir(folder_path), names_of_files)))

files_path = [os.path.join(os.getcwd(), name) for name in names_of_files]

len_path = {}
for path in files_path:
    with open(path, 'r', encoding='utf8') as f:
        l = len(f.readlines())
        len_path.setdefault(path.split('/')[-1], l)

len_path_sorted = dict(sorted(len_path.items(), key=lambda item: item[1]))


file_new_path = os.path.join(os.getcwd(), "result.txt" )

for path, len in len_path_sorted.items():
    with open (file_new_path, 'a', encoding='utf8', newline="") as f:
        f.write(path + '\n')
        f.write(str(len) + '\n')
        with open (os.path.join(os.getcwd(), path), 'r', encoding='utf8', newline="") as file:
            reader = file.readlines()
            for i in reader:
                if i[-1] == '\n':
                    f.write(i)
                else:
                    f.write(i + '\n')


