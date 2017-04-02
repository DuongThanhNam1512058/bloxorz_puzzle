
# coding: utf-8

# In[19]:

"""
------------------------------------------------------
This program is used to build a general structure to resolve some toy problems in AI.
The puzzle is below:

http://www.coolmath-games.com/0-bloxorz

Tha algorithms used here are BFS, DFS.
code written by jimmy shen on March, 2017.
----------------------------------------------------
"""
import copy
import numpy as np
import matplotlib.pyplot as plt


def display_2dlist(list):
    a = np.array(list)
    #print(a)
    plt.imshow(a, cmap='gray')
    plt.show()
    
def find_an_element_in_2dlist(two_d_list, element):
        for i in range(len(two_d_list)):
            for j in range(len(two_d_list[0])):
                if two_d_list[i][j] == element:
                    return True, i , j
        return False, -1 , -1
            
#background
X=0
#board
O=150

#target hole:
T=255


#block lying down
L=200
'''block standing up, here 100 is more darker than 200. 
This is the reason that i am using a samller value to represent the standing up
'''
#block stand up
U=100


#original version
initial_state_list=[[X, X, X, X, X, X, O, O, O, O, O, O, O, X, X],
                    [O, O, O, O, X, X, O, O, O, X, X, O, O, X, X],
                    [O, O, O, O, O, O, O, O, O, X, X, O, O, O, O],
                    [O, U, O, O, X, X, X, X, X, X, X, O, O, T, O],
                    [O, O, O, O, X, X, X, X, X, X, X, O, O, O, O],
                    [X, X, X, X, X, X, X, X, X, X, X, X, O, O, O]]

#simple version
"""initial_state_list=[[X, X, X, X, X, X, O, O, L, L, O, O, O, X, X],
                    [O, O, O, O, X, X, O, O, O, X, X, O, O, X, X],
                    [O, O, O, O, O, O, O, O, O, X, X, O, O, O, O],
                    [O, O, O, O, X, X, X, X, X, X, X, O, O, T, O],
                    [O, O, O, O, X, X, X, X, X, X, X, O, O, O, O],
                    [X, X, X, X, X, X, X, X, X, X, X, X, O, O, O]]
"""

goal_state_list   =[[X, X, X, X, X, X, O, O, O, O, O, O, O, X, X],
                    [O, O, O, O, X, X, O, O, O, X, X, O, O, X, X],
                    [O, O, O, O, O, O, O, O, O, X, X, O, O, O, O],
                    [O, O, O, O, X, X, X, X, X, X, X, O, O, U, O],
                    [O, O, O, O, X, X, X, X, X, X, X, O, O, O, O],
                    [X, X, X, X, X, X, X, X, X, X, X, X, O, O, O]]

display_2dlist(initial_state_list)
display_2dlist(goal_state_list)
#Define problem, node, search class for the eight puzzle problem
import math
MAX_DPETH = 100
class Node():
    def __init__(self, node_state, parent_node, depth):
        self.node_state = node_state
        self.parent_node = parent_node
        self.depth = depth
    def get_parent_node(self):
        return self.parent_node
    def get_node_state(self):
        return self.node_state

class Problem():
  
    def __init__(self, name, init_state, goal_state):
        self.name = name
        self.init_state = init_state
        self.goal_state = goal_state
        print("This is {0}".format(self.name))
    def is_goal(self, visited_node, goal_state_list):
        if visited_node.node_state == goal_state_list:
            return True
        else:
            return False
    def duplication_check(self, node_list):
        for node_close_list in SearchListMaintain.close_list:
            if node_list ==node_close_list.node_state:
                return True
        for node_open_list in SearchListMaintain.open_list:
            if node_list == node_open_list.node_state:
                return True
        return False
    
    def generating_children_nodes(self, current_node):
        #print("Current node 0000")
        #Problem.game_state_print(current_node.node_state)
        if current_node.depth >= MAX_DPETH:
            return []
        else:
            children_nodes=[]
            current_node_board_status=copy.deepcopy(current_node.node_state)
            
            #if the block is standing up, then it can ly to the up down left and right
            U_exist, index_i_previous, index_j_previous=find_an_element_in_2dlist(current_node_board_status, U)
            L_exist, index_i_previous_L, index_j_previous_L=find_an_element_in_2dlist(current_node_board_status, L)
            print("U_exist, index_i_previous, index_j_previous",U_exist, index_i_previous, index_j_previous)
            print("L_exist, index_i_previous_L, index_j_previous_L",L_exist, index_i_previous_L, index_j_previous_L)
            if (U_exist):
                #up
                if(index_i_previous<=1):
                    pass
                elif(current_node_board_status[index_i_previous-1][index_j_previous] == X or 
                     current_node_board_status[index_i_previous-2][index_j_previous] == X or
                     current_node_board_status[index_i_previous-1][index_j_previous] == T or 
                     current_node_board_status[index_i_previous-2][index_j_previous] == T):
                    pass
                else:
                    up_board=copy.deepcopy(current_node_board_status)
                    #print("current_node_board_status result")
                    #Problem.game_state_print(current_node_board_status)
                    up_board[index_i_previous][index_j_previous] = O
                    #print("up_board result 0")
                    #Problem.game_state_print(up_board)
                    up_board[index_i_previous-1][index_j_previous] = L
                    #print("up_board result 1")
                    #Problem.game_state_print(up_board)
                    up_board[index_i_previous-2][index_j_previous] = L
                    #print("up_board result 2")
                    #Problem.game_state_print(up_board)
                    if self.duplication_check(up_board):
                        pass
                    else:
                        children_nodes.append(Node(up_board, current_node, current_node.depth+1))
                        #print("up_board result UP")
                        #Problem.game_state_print(up_board)
                #down
                if(index_i_previous >= 4):
                    pass
                elif(current_node_board_status[index_i_previous+1][index_j_previous] == X or 
                     current_node_board_status[index_i_previous+2][index_j_previous] == X or
                     current_node_board_status[index_i_previous+1][index_j_previous] == T or 
                     current_node_board_status[index_i_previous+2][index_j_previous] == T):
                    pass
                else:
                    down_board=copy.deepcopy(current_node_board_status)
                    down_board[index_i_previous][index_j_previous] = O
                    down_board[index_i_previous+1][index_j_previous] = L
                    down_board[index_i_previous+2][index_j_previous] = L
                    if self.duplication_check(down_board):
                        pass
                    else:
                        children_nodes.append(Node(down_board, current_node, current_node.depth+1))
                        #print("down_board result DOWN")
                        #Problem.game_state_print(down_board)
                #left
                if(index_j_previous <= 1):
                    pass
                elif(current_node_board_status[index_i_previous][index_j_previous-1] == X or 
                     current_node_board_status[index_i_previous][index_j_previous-2] == X or
                     current_node_board_status[index_i_previous][index_j_previous-1] == T or 
                     current_node_board_status[index_i_previous][index_j_previous-2] == T):
                    pass
                else:
                    left_board=copy.deepcopy(current_node_board_status)
                    left_board[index_i_previous][index_j_previous] = O
                    left_board[index_i_previous][index_j_previous-1] = L
                    left_board[index_i_previous][index_j_previous-2] = L
                    if self.duplication_check(left_board):
                        pass
                    else:
                        children_nodes.append(Node(left_board, current_node, current_node.depth+1))
                        #print("left_board result LEFT")
                        #Problem.game_state_print(left_board)
                
                #right
                if(index_j_previous >= 13):
                    pass
                elif(current_node_board_status[index_i_previous][index_j_previous+1] == X or 
                     current_node_board_status[index_i_previous][index_j_previous+2] == X or
                     current_node_board_status[index_i_previous][index_j_previous+1] == T or 
                     current_node_board_status[index_i_previous][index_j_previous+2] == T):
                    pass
                else:
                    right_board=copy.deepcopy(current_node_board_status)
                    right_board[index_i_previous][index_j_previous] = O
                    right_board[index_i_previous][index_j_previous+1] = L
                    right_board[index_i_previous][index_j_previous+2] = L
                    if self.duplication_check(right_board):
                        pass
                    else:
                        children_nodes.append(Node(right_board, current_node, current_node.depth+1))
                        #print("right_board result RIGHT")
                        #Problem.game_state_print(right_board)
            if (L_exist):
                #the block has the share   of     L L
                if current_node_board_status[index_i_previous_L][index_j_previous_L+1]==L:
                
                 #up
                    if(index_i_previous_L<1):
                        pass
                    elif(current_node_board_status[index_i_previous_L-1][index_j_previous_L] == X or 
                        current_node_board_status[index_i_previous_L-1][index_j_previous_L+1] == X or
                        current_node_board_status[index_i_previous_L-1][index_j_previous_L] == T or 
                        current_node_board_status[index_i_previous_L-1][index_j_previous_L+1] == T):
                        pass
                    else:
                        up_board=copy.deepcopy(current_node_board_status)
                        up_board[index_i_previous_L][index_j_previous_L] = O
                        up_board[index_i_previous_L][index_j_previous_L+1] = O
                        up_board[index_i_previous_L-1][index_j_previous_L] = L
                        up_board[index_i_previous_L-1][index_j_previous_L+1] = L
                        if self.duplication_check(up_board):
                            pass
                        else:
                            children_nodes.append(Node(up_board, current_node, current_node.depth+1))
                  
                     #down
                    if(index_i_previous_L>4):
                        pass
                    elif(current_node_board_status[index_i_previous_L+1][index_j_previous_L] == X or 
                        current_node_board_status[index_i_previous_L+1][index_j_previous_L+1] == X or
                        current_node_board_status[index_i_previous_L+1][index_j_previous_L] == T or 
                        current_node_board_status[index_i_previous_L+1][index_j_previous_L+1] == T):
                        pass
                    else:
                        down_board=copy.deepcopy(current_node_board_status)
                        down_board[index_i_previous_L][index_j_previous_L] = O
                        down_board[index_i_previous_L][index_j_previous_L+1] = O
                        down_board[index_i_previous_L+1][index_j_previous_L] = L
                        down_board[index_i_previous_L+1][index_j_previous_L+1] = L
                        if self.duplication_check(down_board):
                            pass
                        else:
                            children_nodes.append(Node(down_board, current_node, current_node.depth+1))
                
                 #left
                    if(index_j_previous_L<1):
                        pass
                    elif(current_node_board_status[index_i_previous_L][index_j_previous_L-1] == X):
                        pass
                    else:
                        left_board=copy.deepcopy(current_node_board_status)
                        left_board[index_i_previous_L][index_j_previous_L] = O
                        left_board[index_i_previous_L][index_j_previous_L+1] = O
                        left_board[index_i_previous_L][index_j_previous_L-1] = U
                        if self.duplication_check(left_board):
                            pass
                        else:
                            children_nodes.append(Node(left_board, current_node, current_node.depth+1))
                            
                
                     #right
                    if(index_j_previous_L>13):
                        pass
                    elif(current_node_board_status[index_i_previous_L][index_j_previous_L+2] == X):
                        pass
                    else:
                        right_board=copy.deepcopy(current_node_board_status)
                        right_board[index_i_previous_L][index_j_previous_L] = O
                        right_board[index_i_previous_L][index_j_previous_L+1] = O
                        right_board[index_i_previous_L][index_j_previous_L+2] = U
                        if self.duplication_check(right_board):
                            pass
                        else:
                            children_nodes.append(Node(right_board, current_node, current_node.depth+1))
                #the block has the share   of    L    
                #                                L 
                if current_node_board_status[index_i_previous_L+1][index_j_previous_L]==L:
                    #print("current_node_board_status aaaa")
                    #Problem.game_state_print(current_node_board_status)
                    #up
                    if(index_i_previous_L<1):
                        pass
                    elif(current_node_board_status[index_i_previous_L-1][index_j_previous_L] == X):
                        pass
                    else:
                        up_board=copy.deepcopy(current_node_board_status)
                        up_board[index_i_previous_L][index_j_previous_L] = O
                        up_board[index_i_previous_L+1][index_j_previous_L] = O
                        up_board[index_i_previous_L-1][index_j_previous_L] = U
                        if self.duplication_check(up_board):
                            pass
                        else:
                            children_nodes.append(Node(up_board, current_node, current_node.depth+1))
                            #print("UPAAA")
                            #Problem.game_state_print(up_board)
                  
                     #down
                    if(index_i_previous_L>=4):
                        pass
                    elif(current_node_board_status[index_i_previous_L+2][index_j_previous_L] == X):
                        pass
                    else:
                        down_board=copy.deepcopy(current_node_board_status)
                        down_board[index_i_previous_L][index_j_previous_L] = O
                        down_board[index_i_previous_L+1][index_j_previous_L] = O
                        down_board[index_i_previous_L+2][index_j_previous_L] = U
                        if self.duplication_check(down_board):
                            pass
                        else:
                            children_nodes.append(Node(down_board, current_node, current_node.depth+1))
                            #print("DOWNAAA")
                            #Problem.game_state_print(down_board)
                
                 #left
                    if(index_j_previous_L<1):
                        pass
                    elif(current_node_board_status[index_i_previous_L][index_j_previous_L-1] == X or
                         current_node_board_status[index_i_previous_L][index_j_previous_L-1] == T or
                         current_node_board_status[index_i_previous_L+1][index_j_previous_L-1] == X or
                         current_node_board_status[index_i_previous_L+1][index_j_previous_L-1] == T ):
                        pass
                    else:
                        left_board=copy.deepcopy(current_node_board_status)
                       
                        left_board[index_i_previous_L][index_j_previous_L] = O
                        #print("left_board init 1")
                        #Problem.game_state_print(left_board)
                        left_board[index_i_previous_L+1][index_j_previous_L] = O
                        #print("left_board init 2")
                        #Problem.game_state_print(left_board)
                        left_board[index_i_previous_L][index_j_previous_L-1] = L
                        #print("left_board init 3")
                        #Problem.game_state_print(left_board)
                        left_board[index_i_previous_L+1][index_j_previous_L-1] = L
                        #print("left_board init 4")
                        #Problem.game_state_print(left_board)
                        if self.duplication_check(left_board):
                            pass
                        else:
                            children_nodes.append(Node(left_board, current_node, current_node.depth+1))
                            #print("LEFTAAA")
                            #Problem.game_state_print(left_board)
                
                     #right
                    if(index_j_previous_L>13):
                        pass
                    elif(current_node_board_status[index_i_previous_L][index_j_previous_L+1] == X or
                         current_node_board_status[index_i_previous_L][index_j_previous_L+1] == T or
                         current_node_board_status[index_i_previous_L+1][index_j_previous_L+1] == X or
                         current_node_board_status[index_i_previous_L+1][index_j_previous_L+1] == T
                        ):
                        pass
                    else:
                        right_board=copy.deepcopy(current_node_board_status)
                        #print("right_board init")
                        #Problem.game_state_print(right_board)
                        right_board[index_i_previous_L][index_j_previous_L] = O
                        #print("right_board init 1")
                        Problem.game_state_print(right_board)
                        right_board[index_i_previous_L+1][index_j_previous_L] = O
                        #print("right_board init 2")
                        #Problem.game_state_print(right_board)
                        right_board[index_i_previous_L][index_j_previous_L+1]=L
                        #print("right_board init 3")
                        #Problem.game_state_print(right_board)
                        right_board[index_i_previous_L+1][index_j_previous_L+1]=L
                        #print("right_board init 4")
                        #Problem.game_state_print(right_board)
                        if self.duplication_check(right_board):
                            pass
                        else:
                            children_nodes.append(Node(right_board, current_node, current_node.depth+1))
                            #print("RIGHTAAA")
                            #Problem.game_state_print(right_board)
            #print("Current node")
            #Problem.game_state_print(current_node.node_state)
            #print("print the child node status")
            """ for c_node in children_nodes:
                Problem.game_state_print(c_node.node_state)
                """
              
            return  children_nodes

      #using a class method to print the status of the board
    @classmethod
    def game_state_print(cls, node_state_list):
        display_2dlist(node_state_list)
        print('-'*10)


class SearchListMaintain():
    max_open_list=0
    max_close_list=0
    open_list=[]
    close_list=[]
    node_index=1
    def __init__(self, name):
        self.name=name
        print("this is the search list maintain center for the {0} problem".format(self.name))


class SearchEngine():
    def __init__(self, name, problem):
        self.name = name
        self.problem = problem
        print("The {0} algorithm is used to search the solution.".format(self.name))


class BFS(SearchEngine):
    def __init__(self, name, problem, init_state_list):
        SearchEngine.__init__(self, name, problem)
        self.init_state_list = init_state_list
    def searching(self, problem):
        root_node = Node(initial_state_list, [], 0)
        duplicate_node = False
        SearchListMaintain.open_list.append(root_node)
        while True:
            extracted_node = self.node_extract()
            #print(extracted_node.get_node_state())
            if self.problem.is_goal(extracted_node, self.problem.goal_state):
                print("solution founded.")
                return extracted_node
            else:
                SearchListMaintain.close_list.append(extracted_node)
                #generating the children nodes and update the tree structure of the problem
                children_nodes = self.problem.generating_children_nodes(extracted_node)
                SearchListMaintain.open_list.extend(children_nodes)

    def node_extract(self):
        if len(SearchListMaintain.open_list) == 0:
            print("error, solution cannot be found")
        else:
            """print("open list")
            for list_open in SearchListMaintain.open_list:
                Problem.game_state_print(list_open.node_state)"""
            
            node_extracted = SearchListMaintain.open_list[0]
            del SearchListMaintain.open_list[0]
            """ print("node_extracted")
            Problem.game_state_print(node_extracted.node_state)"""
           
            return node_extracted


class DFS(BFS):
    def __init__(self, name, problem, init_state_list):
        BFS.__init__(self, name, problem, init_state_list)
    def node_extract(self):
        if len(SearchListMaintain.open_list) == 0:
            print("error, solution cannot be found")
        else:
            node_extracted = SearchListMaintain.open_list[-1]
            del SearchListMaintain.open_list[-1]
            return node_extracted
def get_path_list(right_node_founded):
    path_list=[right_node_founded]
    while True:
        if path_list[0].get_parent_node() == []:
            return path_list
        else:
            path_list.insert(0, path_list[0].get_parent_node())


def print_path_list(list):
    for item in list:
        Problem.game_state_print(item.node_state)




#initial_state_list = goal_state_list[:]
eight_puzzle_search_list_maintian=SearchListMaintain("moving box")
#print(SearchListMaintain.max_open_list)
#print(hash(tuple(initial_state_list)))

moving_box = Problem("moving box", initial_state_list, goal_state_list)

#BFS searching....
bfS_search = BFS("BFS", moving_box, initial_state_list)


right_node = bfS_search.searching(moving_box)

path_list = get_path_list(right_node)
print("print the whole solution:")
print_path_list(path_list)


"""DFS searching....
dfS_search = DFS("DFS", moving_box, initial_state_list)

right_node_DFS = dfS_search.searching(moving_box)

path_list_DFS = get_path_list(right_node_DFS)
print("print the whole solution of DFS:")
print_path_list(path_list_DFS)"""


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



