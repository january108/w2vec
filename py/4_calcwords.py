from gensim.models import word2vec
import sys
import common

model   = word2vec.Word2Vec.load(common.file_out_path + common.file_model)

fi = open(common.file_out_path + common.file_dic, 'r', encoding='utf-8')
dic = fi.read().splitlines()
p_words = ['知能', '学習']

i = 0
for w1 in p_words:
	for w2 in dic:
		i = i + 1
		results = model.most_similar(positive=[w1,w2], topn=5)

		print('--------------------------------')
		print('(' + str(i) + ')「' + w1 + '」＋「' + w2 + '」＝')
		for result in results:
		    print(result[0], '\t', result[1])
