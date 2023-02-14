import os
from collections import Counter
import socket

files_in_dir = os.listdir('/home/data')
total_words=0
words_count=[]
for file in files_in_dir:
    data_path = os.path.join('/home/data', file)
    with open(data_path, 'r') as f:
        data = f.read()
        num_words = len(data.split())
        words_count.append(num_words)
        if data_path == '/home/data/IF.txt':
            counter = Counter(data.replace('�~@~T', ' ').lower().split())
            top_words = counter.most_common(3)
    total_words = total_words + num_words

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

with open(os.path.join('./', 'output', 'result.txt'), 'w') as f:
    f.write('text file locations:\n')
    for file in files_in_dir:
        data_path = os.path.join('/home/data/', file)
        f.write(f'{data_path}\n')
    f.write('\nnumber of words in file:\n')
    for count in words_count:
        f.write(f'{count}\n')
    f.write('\ntotal number of words:\n')
    f.write(f'{total_words}\n')
    f.write('\ntop 3 words in IF.txt:\n')
    for top_word in top_words:
        f.write(f'{top_word}\n')
    f.write('\nip address:\n')
    f.write(f'{ip_address}\n')

with open('/home/output/result.txt', 'r') as f:
    print(f.read())