#### 最大公约数

```C++
链接：https://www.nowcoder.com/questionTerminal/bfc691e0100441cdb8ec153f32540be2
来源：牛客网

int GCD(int a, int b)
{
  if(b==0)
    return a;
  else
    return GCD(b, a%b);
}```

#### 判断是否在一条直线

``` C++
bool isLine(Point a, Point b, Point c)
{
  int left = (a.x - b.x) * (b.y - c.y);
  int right = (a.y - b.y) * (b.x - c.x);
  return left == right;
}
```

### 最短树高

注意没有左子树或者右子树的情况；另外，也可考虑广度优先遍历的思路。

```C++
链接：https://www.nowcoder.com/profile/3197530/codeBookDetail?submissionId=9089980
来源：牛客网

class Solution {
public:
    int run(TreeNode *root) {
        if(!root)
            return 0;
        int l = run(root->left);
        int r = run(root->right);
        if(l==0 || r==0)
            return 1+l+r;
        return 1+min(l,r);
    }
};
```

