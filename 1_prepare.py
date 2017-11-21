import MeCab
import sys
import os
import itertools
from collections import Counter
import common

# 指定フォルダ内のコンテンツを読み込む
def readContents():
	# ファイル読み込み
	files = os.listdir(common.file_in_path)
	print(files)

	# ファイルのコンテンツ読み込み
	contents = ''
	for f in files:
	    fi = open(common.file_in_path + f, 'r', encoding='utf-8')
	    contents =  contents + fi.read()
	    fi.close()

	# print(contents)
	return contents;


# 分かち書き
def wakatiAndCollectNouns():
	tagger = MeCab.Tagger('')

	# 分かち書き結果の出力ファイル
	fw = open(common.file_out_path + common.file_wakati, 'w')

	# 形態素解析の実施、抽出
	chunk = tagger.parse(contents).splitlines()[:-1]
	for ch in chunk:
	    (surface, feature) = ch.split('\t')
	    f= feature.split(',')
	    if f[0] == '名詞' and f[1] == '一般' and not surface.isdigit():
	        if  f[6] != '*':
	            nouns.append(surface)
	    fw.write(f[6]  + ' ')

	fw.close()


# 出現頻度が上位の名詞を topNouns に追加する
def collectTopNouns():
	noun_freq = Counter(nouns)

	# 出力頻度が上位の語彙をコレクト
	for noun_unq in noun_freq.most_common():
		#print(noun_unq)
		if len(topNouns) >= common.rank:
		    break
		else:
			print(noun_unq)
			topNouns.append(noun_unq[0])

	# 出力頻度が上位の語彙をファイル出力
	fd = open(common.file_out_path + common.file_dic, 'w')
	for d in topNouns:
		fd.write(d + '\n')
	fd.close()

#	return topNouns


if __name__ == '__main__':

	nouns = []
	topNouns = []

	# 指定フォルダ内のコンテンツを読み込む
	contents = readContents()

	# 分かち書きし、一般名詞を収集する
	wakatiAndCollectNouns()

	# 出現頻度が上位の名詞を dic に追加する
	collectTopNouns()
