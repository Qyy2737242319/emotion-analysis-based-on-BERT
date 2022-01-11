import os
import tudouNLP.models.predict as p
#os.chdir('../.././UPCnlp')
#情感分析
texts="今天天气还可以".split(' ')
predictor=p.sentence('./tudouNLP/models/model/sentiment_model')
result=predictor.sentiment(texts)
print(result)
#分词
#texts=["在山东青岛，位于长江西路的中国石油大学教务处，王新哲、操应长、查明正在参观邃智科技有限公司！","德玛西亚带领着他的子民在瓦罗兰大陆，与瑞兹展开了殊死搏斗"]
#predictor=p.tagger('./model')
#result=predictor.cut(texts)
#print(result)
#词性标注
#predictor=p.tagger('./model')
#predictor.cut(texts,'posseg')
#命名实体识别
#predictor=p.tagger('./model')
#predictor.ner(texts)
