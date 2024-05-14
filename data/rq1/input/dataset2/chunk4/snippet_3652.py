#Source: https://stackoverflow.com/questions/61969056/i-want-to-solve-this-error-attributeerror-module-tokenization-has-no-attribut
import tokenization
import codecs
import numpy as np

vocab_path = "./model_ch/vocab.txt"
max_seq_length = 128   

file0 = "./task/message.tsv"
f0 = codecs.open(file0, "r", "utf-8")
lines = f0.readlines()
f0.close()

len_file = len(lines)
count = np.zeros([len_file])
count0 = np.zeros([len_file])
my_tokenizer = tokenization.FullTokenizer(vocab_file=vocab_path)

#file1 = "./task_data_ch/%s_count.tsv" % filename
file1 = "./task/message_count.tsv"
f1 = codecs.open(file1, "w", "utf-8")
f1.write("%s\t%s\t%s\r\n" % ("label","count","count_truncated"))

for i in range(1,len_file):
  a = lines[i]
  a = a.split("\t")
  text = a[1]
  token = my_tokenizer.tokenize(text)
  print(token)
  count[i] = len(token) + 2   # for [CLS] and [SEP]
  if count[i] > max_seq_length:
    count0[i] = max_seq_length
  else:
    count0[i] = count[i]
  f1.write("%s\t%s\t%s\n" % (i-1,int(count[i]),int(count0[i])))

sum0 = int(np.sum(count0))
sum1 = int(np.sum(count))
print(sum0, sum1)
print(int(len_file-1))
f1.write("Total: %s, %s" % (sum1,sum0))
f1.close()