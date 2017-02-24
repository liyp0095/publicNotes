# 排序算法

### 随机数

rand() 函数产生随机数，范围0~RAND_MAX，其中RAND_MAX is defined in stdlib.h

You can printf it to find its value.

If you want a extent of the random value, it is necessary to define a micro like :

```C++
#define random (rand() % x) // random from 0 to x 
```
srand() function provide the seed of rand() to generate random numbers. like :

```C++
#include <time.h>
srand((int)time(0)); // or srand(geypid())
int a = rand();
```


### 数组

It is available to generate a 0.1 million array of intege. But 1 million will lead to an error.

**WHY??**

### 文件操作

ifstream ofsteam and fstream

```C++
// this is out file stream. just like cout.
ofstream file;
file.open("data.txt");
file << data[i] << endl;
file.close();
```

## Sort Algorithm

This is important.

Bubble: 每次冒出个最大的，n-1次冒完。 </br>
Select: 每次选择最小的，放在已排序的数据后面；分为选择数据，放在对应位置两步。 </br>
Insert: 直接插入，保持前i个数据有序，每次把一个数据插入到正确位置，需要哨兵帮助。  </br>
Quick: 


| 交换排序 | 选择排序 | 插入排序 |
| :------------- | :------------- | ----------- |
| 冒泡法 | 直接选择 | 直接插入 |
| 鸡尾酒 地精 快排 | 堆排序 | 希尔排序 |










