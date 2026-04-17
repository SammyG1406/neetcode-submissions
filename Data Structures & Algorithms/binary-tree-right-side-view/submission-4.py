# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        ## will need to add the nods into a queue from the right
        ## first check the right child add that to the queue

        q=collections.deque()
        q.append(root)

        while q:
            qlen=len(q)
            added=0
            for i in range(qlen):
                element=q.popleft()
                if element:
                    q.append(element.right)
                    q.append(element.left)
                    if added==0:
                        result.append(element.val)
                        added=1
                
        
        return result

            