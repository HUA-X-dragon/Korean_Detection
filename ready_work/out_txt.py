import os

pngname = []
name = []
for filename in os.listdir(r"E:\AItest\ML\deep-text-recognition-benchmark-master\data\valid"):
    pngname.append(filename)
    name.append(filename.split('.')[0])

fo=open(r'E:\AItest\ML\deep-text-recognition-benchmark-master\data\gt2.txt', 'w', encoding='utf8')
for item in pngname:
    fo.write('valid/'+str(item)+'\t'+str(item.split('_')[0])+'\n')


# pngname = []
# name = []
# for filename in os.listdir(r"E:\AItest\ML\TextRecognitionDataGenerator-master\trdg\out2"):
#     pngname.append(filename)
#     name.append(filename.split('.')[0])
#
# fo=open(r'E:\AItest\ML\TextRecognitionDataGenerator-master\trdg\out2\1.txt', 'w', encoding='utf8')
# for item in pngname:
#     fo.write(str(item).replace(' ', '')+' '+str(item.split('_')[0].replace(' ', ''))+'\n')