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
运行以下命令训练你的模型
```
CUDA_VISIBLE_DEVICES=0 python3 train.py \
--train_data data/train --valid_data data/valid \
--select_data MJ-ST --batch_ratio 0.5-0.5 \
--Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn
```

