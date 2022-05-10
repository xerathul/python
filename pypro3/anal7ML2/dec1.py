# Decision tree (의사결정나무)
# classification, regression 모두 가능하나 분류 모델로 더 많이 사용 됨
# - Decision Tree는 여러 가지 규칙을 순차적으로 적용하면서 독립 변수 공간을 분할하는 분류 모형이다

import collections
from sklearn import tree

x = [[180,15],[177,42],[156,35],[174,5],[166,33]]
y = ['m','w','w','m','w']

label_names = ['height','hair length']

model = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
model.fit(x,y)
pred = model.predict(x)
print(pred)

mtdata = [[171,8]]
new_pred = model.predict(mtdata)
print(new_pred)

# - - - - 5교시 - - - -
# 시각화
import pydotplus
dot_data = tree.export_graphviz(model, feature_names = label_names, 
                                out_file = None, filled = True, rounded = True) #옵션이 무지하게 많음..!
graph = pydotplus.graph_from_dot_data(dot_data)
colors = ('red', 'orange')
edges = collections.defaultdict(list)
print(edges, type(edges))   # defaultdict(<class 'list'>, {}) <class 'collections.defaultdict'>

for e in graph.get_edge_list():
    edges[e.get_source()].append(int(e.get_destination()))

print(edges)

for e in edges:
    edges[e].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[e][i]))[0] #edges의 e행i열의0번째
        dest.set_fillcolor(colors[i])

#graph.write_png('tree.png')

# 저장한 tree.png 불러오기
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread    #이미지 읽기
img = imread("tree.png")
plt.imshow(img)
plt.show()