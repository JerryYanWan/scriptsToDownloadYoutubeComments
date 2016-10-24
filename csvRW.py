# coding: utf-8
import csv
import sys
import codecs
if __name__ == '__main__':

  data = []
  with open(sys.argv[1], "r") as fr:
    rr = csv.reader(fr)
    for line in rr:
      print line
      data.append(line)

  with open(sys.argv[2], "w") as fw:
    fw.write(codecs.BOM_UTF8)
    wr = csv.writer(fw)
    for line in data:
      wr.writerow(line)
   # for key in all_comments_table.keys():
   #   listInfo = all_comments_table[key]
   #   listInfo.append(str(comments_followers[key]))
   #   wr.writerow([x.encode('utf-8') for x in listInfo])
