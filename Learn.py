def FalstCount(a,b,m):
    res = 1
    while b != 0:
        if b&1:
            res = (res*a)%m
        b >>= 1
        a = (a*a)%m
    return res

#快速幂模
def quick_algorithm(a,b,c):
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans

#快速幂
def func(a,b):
    res = 1
    while b!=0:
        if b&1:
            res = res*a
        b >>= 1
        a *=  a
    return res

#快排
def quictSort(ls):
    if not ls:
        return []
    p = ls[0]
    left = quictSort([x for x in ls[1:] if x<p])
    right = quictSort([x for x in ls[1:] if x>p])
    return left + [p] + right

#判断平衡二叉树
def IsBalanced_Solution(self, pRoot):
    
    
    def get_depth(self, p):
        if p is None:
            return 0
        left = self.get_depth(p.left)
        if left == -1:
            return -1
        right = self.get_depth(p.right)
        if right == -1:
            return -1
        if abs(left-right)>1:
            return -1
        return 1 + max(left,right)

    return self.get_depth(pRoot) != -1

#求二叉树的深度
def TreeDepth(self, pRoot):
 
    if pRoot==None:
        return 0
    return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1

'''
非递归
    int TreeDepth(TreeNode* pRoot) {
        if (!pRoot) return 0;
        queue<TreeNode*> que;
        que.push(pRoot);int depth=0;
        while (!que.empty()) {
            int size=que.size();
            depth++;
            for (int i=0;i<size;i++) {      //一次处理一层的数据
                TreeNode *node=que.front();
                que.pop();
                if (node->left) que.push(node->left);
                if (node->right) que.push(node->right);
            }
        }
        return depth;
    }
'''

#求第N个丑数 把只包含质因子2、3和5的数称作丑数（Ugly Number）
def GetUglyNumber_Solution(self, index):
    # write code here
    if index<7:
        return index
     num = []
    n2,n3,n5 = 0,0,0
    num.append(1)
    while len(num)<index:
        n = min(num[n2]*2,num[n3]*3,num[n5]*5)
        num.append(n)
        if n == num[n2]*2:
            n2+=1
        if n == num[n3]*3:
            n3+=1
        if n == num[n5]*5:
            n5+=1
    return num.pop()

#输入两个链表，找出它们的第一个公共结点。
def FindFirstCommonNode(self, pHead1, pHead2):
    # 使用两个链表合为一个链表同时遍历的方法
    p1 = pHead1
    p2 = pHead2
    while p1 != p2:
        p1 = p1.next if p1 else pHead2
        p2 = p2.next if p2 else pHead1
            
    return p1

#合并两个排序链表
'''
public ListNode Merge(ListNode list1,ListNode list2) {
       if(list1 == null){
           return list2;
       }
       if(list2 == null){
           return list1;
       }
       if(list1.val <= list2.val){
           list1.next = Merge(list1.next, list2);
           return list1;
       }else{
           list2.next = Merge(list1, list2.next);
           return list2;
       }       
   }
'''

#判断对称二叉树
def isSymmetrical(self, pRoot):
    # write code here
    if not pRoot:
        return True
    def compare( pLeft, pRight):
        if not pLeft and not pRight:
            return True
        elif pLeft and pRight:
            if pLeft.val == pRight.val:
                return compare(pLeft.left, pRight.right) and compare(pLeft.right, pRight.left)
        else:
            return False
    return compare(pRoot.left, pRoot.right)

#二叉树序列化及反序列化
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = -1
         
    def Serialize(self, root):
        # write code here
        if not root:
            return '#,'
        return str(root.val)+','+self.Serialize(root.left)+self.Serialize(root.right)
         
    def Deserialize(self, s):
        # write code here
        self.flag += 1
        l = s.split(',')
         
        if self.flag >= len(s):
            return None
        root = None
         
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

#查找最长不重复子串
def find_longest_no_repeat_substr(one_str):
   
    res_list=[]
    length=len(one_str)
    for i in range(length):
        tmp=one_str[i]
        for j in range(i+1, length):
            if one_str[j] not in tmp:
                tmp+=one_str[j]
            else:
                break
        res_list.append(tmp)
    res_list.sort(lambda x,y:cmp(len(x),len(y)))
    return res_list[-1]

#已知前序和中序，重建二叉树并返回
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))
        tin_index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:tin_index])
        root.right = self.reConstructBinaryTree(pre, tin[tin_index+1:])
        return root

#最长无重复字符的长度
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
  
        d_map = {}  
        start = maxLength = 0  
        for i in range(len(s)):  
            if s[i] in d_map and start <= d_map[s[i]]:  
                start = d_map[s[i]] + 1  
            else:  
                maxLength = max(maxLength, i - start + 1)  
            d_map[s[i]] = i  
        return maxLength 


if __name__ == '__main__':
    a=func(3, 4)
    print(a)
