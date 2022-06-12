1 创建您自己的 lmdb 数据集

```
pip3 install fire
python3 create_lmdb_dataset.py --inputPath data/ --gtFile data/gt.txt --outputPath result/
```
数据文件夹的结构如下

```
data
├── gt.txt
└── test
    ├── word_1.png
    ├── word_2.png
    ├── word_3.png
    └── ...
```
这时，gt.txt应该是{imagepath}\t{label}\n
```
test/word_1.png Tiredness
test/word_2.png kills
test/word_3.png A
...
```
2 修改--select_data,--batch_ratio和opt.character
```
    parser.add_argument('--select_data', type=str, default='/', 
                     help='select training data (default is MJ-ST, which means MJ and ST used as training data)') 
    parser.add_argument('--batch_ratio', type=str, default='1', 
                     help='assign ratio for each selected data in the batch') 
```
```
parser.add_argument('--character', type=str, default='0123456789abcdefghijklmnopqrstuvwxyz', help='character label') 
```
