import os


Path = os.path.abspath("YourPath\\WordsCount2")
DictPath = os.path.abspath("YourPath\\dict.txt")
Articles = os.path.abspath("YourPath\\articles.txt")



def actualize_dict():
    
    words_dict = dict()

    files_set = set(os.listdir(Path))
    for file in files_set:
        
        f = open(os.path.join(Path,file),"r",encoding='utf-8')
        for line in f.readlines():
            word, cnt = line.split()
            if word not in words_dict:
                words_dict[word] = 0
            words_dict[word] += int(cnt)
        f.close()


    write_to_dict(words_dict)


def write_to_dict(dict):
    file = open(DictPath,"w",encoding='utf-8')
    sorted_items = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    for word,counter in sorted_items:
        if counter >= 10 and word.isascii():
            print(counter)
            file.write(word + " " + str(counter) + "\n")
            
    file.close()


def files():
    list = os.listdir(Path)
    file = open(Articles,"w",encoding='utf-8')
    for name in list:
        file.write(name.replace(".txt","") +"\n")
    
    file.close()

actualize_dict()
files()
