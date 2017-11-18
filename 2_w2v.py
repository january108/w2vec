##
## モデルを作成する
##
from gensim.models import word2vec
import logging
import sys
import common

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.LineSentence(common.file_out_path + common.file_wakati)

model = word2vec.Word2Vec(sentences,
                          sg=1,
                          size=100,
                          min_count=1,
                          window=10,
                          hs=1,
                          negative=0)
model.save(common.file_out_path + common.file_model)

print('model saved : ' + common.file_out_path + common.file_wakati)