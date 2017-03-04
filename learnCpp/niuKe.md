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

### 树的前序、中序、后续遍历

recursive solution is trivial, could you do it iteratively?

后序使用一个栈保存节点。

```C++
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> ret;
        if (!root) return ret;
         
        stack<TreeNode*> st;
        st.push(root);
        TreeNode* cur;
        while(!st.empty()){
            cur = st.top();
            if(!cur->left && !cur->right){
                ret.push_back(cur->val);
                st.pop();
            }else{
                if(cur->right){
                    st.push(cur->right);
                    cur->right = NULL;
                }
                if(cur->left){
                    st.push(cur->left);
                    cur->left = NULL;
                }
            }
        }
        return ret;
    }
};
```

先序遍历与后序极度相似。只是直接将根节点弹出即可。
中序遍历

### Find Kth Numbers

```C++
class Solution {
public:
    int findKth(int A[], int m, int B[], int n, int ast, int bst, int k){
        if (ast >= m) return B[bst + k - 1];
        if (bst >= n) return A[ast + k - 1];
        if (k == 1) return (A[ast] < B[bst] ? A[ast] : B[bst]);
        
        int Ak = (ast + k/2 - 1 >= m) ? INT_MAX : A[ast + k/2 - 1];
        int Bk = (bst + k/2 - 1 >= n) ? INT_MAX : B[bst + k/2 - 1];
        if (Ak < Bk)
            return findKth(A, m, B, n, ast+k/2, bst, k-k/2);
        else
            return findKth(A, m, B, n, ast, bst+k/2, k-k/2);
    }
    
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
    	double median = 0.0;
        if((m+n) & 1)
            median = (double)findKth(A, m, B, n, 0, 0, (m+n+1)/2);
        else
            median = (double)(findKth(A, m, B, n, 0, 0, (m+n)/2) + findKth(A, m, B, n, 0, 0, (m+n)/2+1)) / 2;
        
        return median;
    }
};
```

