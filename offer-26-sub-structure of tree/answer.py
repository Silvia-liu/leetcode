class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True  # 如果B遍历完了，说明b是a的子结构
            if not A or A.val != B.val: return False  # 如果a遍历完了，即最后一个节点都不符合，或者a的值和b的值不相等，则返回false
            return recur(A.left, B.left) and recur(A.right, B.right)  # 如果A B相等，则接着往下遍历，即返回recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
    # 上面这句相当于主函数
    #  bool(A and B)保证A B都不为空结构。
    # 情况一，b的根节点是a的根节点，recur(A, B)
    # 情况二， b的根节点是a的左子节点，self.isSubStructure(A.left, B)
    # 情况三， b的根节点是a的右子节点，self.isSubStructure(A.right, B)
    # 如果不用情况2 3，b的根节点=a的左子节点，带入recur(A, B),会出错，所以需要self.isSubStructure(A.left, B)和self.isSubStructure(A.right, B)
    
    
    # 1 ‘默写’代码的时候 bool(A and B)出错，后面那个and也错了。要保证AB不是空结构，且B为A的子结构，才可以返回Ture
    # 2 self.isSubStructure的self忘记加了。
    # 3 最后一行的and左右要用（）括起来，不可以直接用表达式
    # 4 倒数第二行的and也错了写成了or，是理解失误  解释如下：
    例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
    # 代码执行如题解的ppt所示，最后一行的return相当于主函数
    #先bool(A and B) 为真，然后执行recur(A, B)，return false，然后执行右边的self.isSubStructure(A.left, B)。（4，4）
    #进入以后，先执行bool(A.left and B)，然后执行recur(A.left, B)（4，4） 为真，return了recur(A.left.left,B.left)and recur(A.left.right, B.right)即recur(1,1)and recur(2, none)
    
    # 好巧不巧 recur(A.left.right, B.right) 即recur(2, none)中的B.right是没有的，返回Ture
    # recur(A.left.left,B.left)中A.left.left,B.left是相等的，return了recur(A.left.left.left,B.left.left)and recur(A.left.left.right, B.left.right)
    # 其中recur(A.left.left.left,B.left.left)中的B.left.left是没有的，返回Ture    recur(A.left.left.right, B.left.right)中B.left.right也是没有的，返回Ture
    
