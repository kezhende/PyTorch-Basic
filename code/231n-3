
# 损失函数
# L_i = \sum_{j \neq y_i}\max(0, s_j - s_{y_i} + 1)

def L_i_vectorized(x, y, W):
  scores = W.dot(x)
  margins = np.maximum(0, scores - scores[y] + 1)
  margins[y] = 0
  loss_i = np.sum(margins)
  return loss_i
