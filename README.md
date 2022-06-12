# What Is Wrong With Scene Text Recognition Model Comparisons? Dataset and Model Analysis
| [paper](https://arxiv.org/abs/1904.01906) | [training and evaluation data](https://github.com/clovaai/deep-text-recognition-benchmark#download-lmdb-dataset-for-traininig-and-evaluation-from-here) | [failure cases and cleansed label](https://github.com/clovaai/deep-text-recognition-benchmark#download-failure-cases-and-cleansed-label-from-here) | [pretrained model](https://www.dropbox.com/sh/j3xmli4di1zuv3s/AAArdcPgz7UFxIHUuKNOeKv_a?dl=0) | [Baidu ver(passwd:rryk)](https://pan.baidu.com/s/1KSNLv4EY3zFWHpBYlpFCBQ) |

Official PyTorch implementation of our four-stage STR framework, that most existing STR models fit into. <br>
Using this framework allows for the module-wise contributions to performance in terms of accuracy, speed, and memory demand, under one consistent set of training and evaluation datasets. <br>
Such analyses clean up the hindrance on the current comparisons to understand the performance gain of the existing modules. <br><br>
<img src="./figures/trade-off.png" width="1000" title="trade-off">

## Honors
Based on this framework, we recorded the 1st place of [ICDAR2013 focused scene text](https://rrc.cvc.uab.es/?ch=2&com=evaluation&task=3), [ICDAR2019 ArT](https://rrc.cvc.uab.es/files/ICDAR2019-ArT.pdf) and 3rd place of [ICDAR2017 COCO-Text](https://rrc.cvc.uab.es/?ch=5&com=evaluation&task=2), [ICDAR2019 ReCTS (task1)](https://rrc.cvc.uab.es/files/ICDAR2019-ReCTS.pdf). <br>
The difference between our paper and ICDAR challenge is summarized [here](https://github.com/clovaai/deep-text-recognition-benchmark/issues/13).

## Updates
**Aug 3, 2020**: added [guideline to use Baidu warpctc](https://github.com/clovaai/deep-text-recognition-benchmark/pull/209) which reproduces CTC results of our paper. <br>
**Dec 27, 2019**: added [FLOPS](https://github.com/clovaai/deep-text-recognition-benchmark/issues/125) in our paper, and minor updates such as log_dataset.txt and [ICDAR2019-NormalizedED](https://github.com/clovaai/deep-text-recognition-benchmark/blob/86451088248e0490ff8b5f74d33f7d014f6c249a/test.py#L139-L165). <br>
**Oct 22, 2019**: added [confidence score](https://github.com/clovaai/deep-text-recognition-benchmark/issues/82), and arranged the output form of training logs. <br>
**Jul 31, 2019**: The paper is accepted at International Conference on Computer Vision (ICCV), Seoul 2019, as an oral talk. <br>
**Jul 25, 2019**: The code for floating-point 16 calculation, check [@YacobBY's](https://github.com/YacobBY) [pull request](https://github.com/clovaai/deep-text-recognition-benchmark/pull/36) <br>
**Jul 16, 2019**: added [ST_spe.zip](https://drive.google.com/drive/folders/192UfE9agQUMNq6AgU3_E05_FcPZK4hyt) dataset, word images contain special characters in SynthText (ST) dataset, see [this issue](https://github.com/clovaai/deep-text-recognition-benchmark/issues/7#issuecomment-511727025) <br>
**Jun 24, 2019**: added gt.txt of failure cases that contains path and label of each image, see [image_release_190624.zip](https://drive.google.com/open?id=1VAP9l5GL5fgptgKDLio_h3nMe7X9W0Mf) <br>
**May 17, 2019**: uploaded resources in Baidu Netdisk also, added [Run demo](https://github.com/clovaai/deep-text-recognition-benchmark#run-demo-with-pretrained-model). (check [@sharavsambuu's](https://github.com/sharavsambuu) [colab demo also](https://colab.research.google.com/drive/1PHnc_QYyf9b1_KJ1r15wYXaOXkdm1Mrk)) <br>
