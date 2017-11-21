##
## 頻出名詞の類似語リストを作成する
##

from gensim.models import word2vec
import sys
import common

bocabrary = ['機械', '人間', ]
#bocabrary = ['機械', '知能', 'データ', '人間', '企業', ]
model   = word2vec.Word2Vec.load(common.file_out_path + common.file_model)

# 結果出力ファイル
fw = open(common.file_out_path + common.file_5similar, 'w')

for d in bocabrary:
    common.printFileAndStd(fw, '')
    common.printFileAndStd(fw, '--- 「' + d + '」 に類似 ---')
    results = model.most_similar(positive=d, topn=5)

    for result in results:
    	out = str(result[0]) + '\t' + str(result[1])
    	common.printFileAndStd(fw, out)
    	#print(result[0], '\t', result[1])
    	#fw.write(f[6]  + ' ')

fw.close()