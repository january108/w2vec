##
## 頻出名詞の類似語リストを作成する
##

from gensim.models import word2vec
import sys
import common

model   = word2vec.Word2Vec.load(common.file_out_path + common.file_model)
fi = open(common.file_out_path + common.file_dic, 'r', encoding='utf-8')
dic = fi.read().splitlines()

for d in dic:
    print()
    print('--- 「' + d + '」 に類似 ---')
    results = model.most_similar(positive=d, topn=5)

    for result in results:
        print(result[0], '\t', result[1])
