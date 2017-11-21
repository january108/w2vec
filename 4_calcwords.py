from gensim.models import word2vec
import sys
import common

model   = word2vec.Word2Vec.load(common.file_out_path + common.file_model)

fi = open(common.file_out_path + common.file_dic, 'r', encoding='utf-8')
dic = fi.read().splitlines()
p_words = ['知能', '学習']

# 結果出力ファイル
fw = open(common.file_out_path + common.file_calc, 'w')

i = 0
for w1 in p_words:
	for w2 in dic:
		i = i + 1
		results = model.most_similar(positive=[w2,w1], topn=5)

		common.printFileAndStd(fw, '--------------------------------')
		common.printFileAndStd(fw, '(' + str(i) + ')「' + w2 + '」＋「' + w1 + '」＝')
		for result in results:
			out = str(result[0]) + '\t' + str(result[1])
			common.printFileAndStd(fw, out)

# 全部足してみる
results = model.most_similar(positive=[dic[0],dic[1],dic[2],dic[3],dic[4],dic[5],dic[6],dic[7],dic[8],dic[9],], topn=5)

common.printFileAndStd(fw, '--------------------------------')
common.printFileAndStd(fw, '(all)「' + dic[0]+ '」＋「' + dic[1]+ '」＋「' + dic[2]+ '」＋「' + dic[3]+ '」＋「' + dic[4]+ '」＋「' + dic[5]+ '」＋「' + dic[6]+ '」＋「' + dic[7]+ '」＋「' + dic[8]+ '」＋「' + dic[9]+ '」＝')
for result in results:
	out = str(result[0]) + '\t' + str(result[1])
	common.printFileAndStd(fw, out)


fw.close()