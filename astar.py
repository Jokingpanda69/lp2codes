import heapq

class PuzzleNode:

    def __init__(self,state,parent=None,move=None,depth=0,cost=0):
        self.state,self.parent,self.move,self.depth,self.cost = state,parent,move,depth,cost
    
    def __lt__(self,other):
        return (self.cost + self.depth) < (other.cost + other.depth)

class PuzzleSolver:

    def __init__(self,initial_state):
        self.initial_state = initial_state
    
    def find_blank(self,state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i,j
            
    def calculate_cost(self, state):
        cost = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for i in range(3):
            for j in range(3):
                if state[i][j]!= goal_state[i][j]:
                    cost += 1
        return cost

    def generate_children(self,node):
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        row,col = self.find_blank(node.state)
        children =[]

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if (0<= new_row < 3 and 0<= new_col < 3):
                new_state = [row[:] for row in node.state]
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                child = PuzzleNode(new_state,node,move,node.depth+1,self.calculate_cost(new_state))
                children.append(child)
        return children

    def __call__(self):
        initial_node = PuzzleNode(self.initial_state)
        open_list, closed_list = [initial_node], set()
        moves = []

        while open_list:
                current_node = heapq.heappop(open_list)
                if current_node.state == [[1,2,3], [4,5,6], [7,8,0]]:
                    while current_node.parent:
                        moves.append(current_node.state)
                        current_node = current_node.parent
                    moves.append(self.initial_state)
                    moves.reverse()
                    return moves
                closed_list.add(tuple(map(tuple, current_node.state)))
                for child in self.generate_children(current_node):
                    if tuple(map(tuple, child.state)) not in closed_list:
                        heapq.heappush(open_list, child)

        return None

initial_state = [[1,3,2], [4,7,6], [0,5,8]]
solver = PuzzleSolver(initial_state)
solution = solver()
for state in solution:
    print(state)