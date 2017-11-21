## 定数
# 対象フォルダ
#file_path = '../data/cio/'
file_path = './data/sample/'
file_in_path = file_path + 'in/'
file_out_path = file_path + 'out/'

# 出力ファイル
file_dic = 'dic.txt'
file_wakati = 'wakati.txt'
file_model = 'wakati.model'
file_similar = 'similar.txt'
file_5similar = '5similar.txt'
file_calc = 'calc.txt'

# ランキング何位までの名詞を使用するか
rank = 10

def printFileAndStd(fw, out):
	print(out)
	fw.write(out + '\n')

