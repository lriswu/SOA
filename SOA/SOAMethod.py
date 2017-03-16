'''
SOA Method
'''
import nltk
import operator
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def readList(S1,S2):
    '''
    read female and male  train list
    :return: list
    '''
    f = open(S1)
    filelist = [f.readline().strip()]
    for line in f:
        filelist.append(line.strip())
    f.close()
    f = open(S2)
    for line in f:
        filelist.append(line.strip())
    f.close()
    return filelist

def Dispaly(dic,path):
    dic_new ={}
    f = open(path,'w')
    sort_dict =sorted(dic.items(),key = operator.itemgetter(1),reverse=True)
    for d,x in sort_dict:
        if x >= 5:
            dic_new[d]= x
            f.write(d+","+str(x)+'\n')
    f.close()
    return dic_new

def BuiltDic(word_dic,filelist,Spath):

    word_list = word_dic.keys()
    file_writer= open(Spath,'w')
    for word in word_list:
        #
        # if word_list.index(word) >2:
        #     break
        word_cout = []
        for file in filelist:
            path = "/home/lris/Desktop/pan_dataset/pan_dataset/docs/" + file + '.txt'
            f = open(path)
            tokens = []

            for line in f.readlines():
                tokens+=nltk.word_tokenize(line)
            text = nltk.Text(tokens)
            word_cout.append(text.count(word))

        s = str(word_cout)
        file_writer.write(word+','+s+'\n')
        print word_list.index(word)
        print word
    #     word_dict[word] = word_cout
    #     print word
    #     print word_dict[word]
    #
    # return word_dict



def builtWord(filelist):
    dict = {}
    for l in filelist:
        # if filelist.index(l)>1:
        #     break

        path = "/home/lris/Desktop/pan_dataset/pan_dataset/docs/"+l+'.txt'
        f = open(path)
        print path
        for line in f.readlines():
            word_list = nltk.word_tokenize(line)
            for word in word_list:
                if word not in dict:
                    dict[word]= 0
                dict[word]+=1

    dict_new =Dispaly(dict,"/home/lris/Desktop/wordFre.json")
    return dict_new

file_list=readList("/home/lris/Desktop/pan_dataset/pan_dataset/gender/female.txt","/home/lris/Desktop/pan_dataset/pan_dataset/gender/male.txt")
dict=builtWord(file_list)
BuiltDic(dict,file_list,"/home/lris/Desktop/term.json")

