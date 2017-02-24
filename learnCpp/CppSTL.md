# STL 

## 简介

STL（Standard Template Library，标准模板库)是惠普实验室开发的一系列软件的统称。它是由Alexander Stepanov、Meng Lee和David R Musser在惠普实验室工作时所开发出来的。现在虽说它主要出现在C++中，但在被引入C++之前该技术就已经存在了很长的一段时间。

STL的代码从广义上讲分为三类：algorithm（算法）、container（容器）和iterator（迭代器），几乎所有的代码都采用了模板类和模版函数的方式，这相比于传统的由函数和类组成的库来说提供了更好的代码重用机会。在C++标准中，STL被组织为下面的13个头文件：<algorithm>、<deque>、<functional>、<iterator>、<vector>、<list>、<map>、<memory>、<numeric>、<queue>、<set>、<stack>和<utility>。

## 算法

### algorithm

#### distance 

distance(a, b); 地址a到b的距离，

#### unique

unique(A, A+n); unique去重消去相邻的重复元素，一般配合sort一起使用。也可以作用于string数组。

#### upper_bound lower_bound

在一个有序数组中找寻边界，大于x的第一个的位置，或者第一个x的位置

numeric
functional

## 容器

* vector
* list
* deque
* set
* multiset
* stack
* queue
* priority_queue
* map
* multimap

## 迭代器

utility
iterator


