## 常量成员函数

类内部 </br>
```C++
int add() const;
```

或者类外部 </br>

```C++
int opera::add() const{
  bla;
  bla;
}
```

不修改成员变量，若有修改，会报错。

## 返回this

```C++
Sales_data& Sales_data::combine(const Sales_data &rhs)
{
  return \*this;
}
``` 

## 常量引用

```C++
String::size_type find_char(string &s, char);

调用时
find_char("Hello World", 'c');
会报错。

所以，
String::size_type find_char(const string &s, char);
```

## const 初始化顺序

```C++
const int *p = &i;
const int &p = &i;
const int &p = 42;
 
```

## 实参与形参

## Struct and Union

```C++
#include <iostream>
using namespace std;

int main() 
{ 
    union test
    {
        int i;
        struct 
        {
            char first;
            char second;
        }half;
    }number;
    number.i = 0x4241;
    cout<<number.half.first<<" "<<number.half.second<<endl;
    number.half.first = 'a';
    number.half.second = 'b';
    printf("%x\n", number.i);

    return 0; 
}
```

输出结果： </br>
A B </br>
6263

两者之间的区别：
 （1）在同一时刻，结构体的每个成员都有值，但是联合体在同一时刻只有一个成员有值（或理解为结构体的sizeof是所有成员的和，而联合体的sizeof等于其最长的成员的sizeof）；
 （2）当对结构体变量的其中一个成员进行修改时，对其他成员没有影响，但是修改联合体时，则会将原来的成员值覆盖。
例子：关于修改联合体的成员的值.


## 




