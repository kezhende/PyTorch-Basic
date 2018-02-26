import torch
import torch.nn as nn
from torchvision.models import vgg16
from collections import namedtuple

class Vgg16(torch.nn.Module):
    def __init__(self):
	super(Vgg16, self).__init__()
	# 通过features直接获得对应的nn.Sequential对象
	features = list(vgg16(pretrained = True).features)[:23]
	self.features = nn.ModuleList(features).eval()

    def forward(self, x):
	# 在前向传播时，当计算完指定层的输出后，就将结果保存在一个list中，然后再使用namedtuple进行名称绑定
	# 这样可以通过output.relu1_2访问第一个元素，更方便直观
	results = []
	# features的第3,8,15,22层分别是: relu1_2, relu2_2, relu3_3, relu4_3
	for ii, model in enumerate(self.features):
	    x = model(x)
	    if ii in {3, 8, 15, 22}:
		results.append(x)
		vgg_outputs = namedtuple("VggOutputs", ['relu1_2', 'relu2_2', 'relu3_3', 'relu4_3'])
	return vgg_outputs(*results)
