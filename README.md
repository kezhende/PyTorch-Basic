# PyTorch-Basic

PyTorch社区活跃人物陈云编写的《深度学习框架PyTorch入门与实践》的学习代码记录。本书项目的官方主页地址：


https://github.com/chenyuntc/pytorch-book
 
 
在2018年寒假伊始，在京东和淘宝上发现了我所知道的国内第二本关于PyTorch的教程书（第一本是廖星宇的《深度学习入门之PyTorch》）。
 
 
初步印象，印刷比较好，排版工整，代码教程比较人性化，感觉良好。


1.30 2018 


电脑修过之后，好像连wifi的网速变慢了，下载CIFAR-10的数据集要8个小时，不太对劲（沧桑.jpg）
 
 
顺便记录一下Linux下解压tar.gz文件的命令：


tar -zxvf xxx.tar.gz 


1.31 2018 


 CIFAR-10.jpynb 里按原代码敲的话会有一个bug，原代码是直接用LongTensor作为classes数组的下标，系统要求classes数组下标类型需要是int型的


 讨论群里的作者和一个大佬说原代码没问题，这么说有可能是我PyTorch的版本问题，或者前面敲的代码有问题。


