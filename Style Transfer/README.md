# 用PyTorch实现风格迁移
## 本实验的文件组织：
```Python
checkpoints/
data/
    coco -> /mnt/3/coco/train2014
main.py
PackedVGG.py
style.jpg
transformer_net.py
utils.py
```
### checkpoints/
用来保存模型
### data/
用来保存数据，可以把数据直接保存在coco文件夹下，也可以通过ln - s /mnt/3/coco/train2014 data/coco软链接方式将数据链接到data/文件夹下，还可以通过命令行参数另外指定数据路径
### main.py
主函数，包括训练和测试
### PackedVGG.py
直接使用torchvision仓库中训练好的VGG-16网络。预训练好的VGG-16，为了提取中间层的输出，所以做了一些修改简化<br>
但在风格迁移中，需要获得中间层的输出，因此需要修改网络的前向传播过程，将相应层的输出保存下来。<br>
同时还有很多层不需要，可以删除以节省内存占用
### transformer_net.py
风格迁移网络，输入一张图，输出一张图
### utils.py
工具集合，主要是可视化工具visdom的封装和计算Gram Matrix等
