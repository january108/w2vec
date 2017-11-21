##
## 頻出名詞の類似語リストを作成する
##

from gensim.models import word2vec
import sys
import common

model   = word2vec.Word2Vec.load(common.file_out_path + common.file_model)
fi = open(common.file_out_path + common.file_dic, 'r', encoding='utf-8')
dic = fi.read().splitlines()

# 結果出力ファイル
fw = open(common.file_out_path + common.file_similar, 'w')

for d in dic:
    common.printFileAndStd(fw, '')
    common.printFileAndStd(fw, '--- 「' + d + '」 に類似 ---')
    results = model.most_similar(positive=d, topn=5)

    for result in results:
    	out = str(result[0]) + '\t' + str(result[1])
    	common.printFileAndStd(fw, out)
    	#print(result[0], '\t', result[1])
    	#fw.write(f[6]  + ' ')

fw.close()