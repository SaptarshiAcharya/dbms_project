import random
import time
import matplotlib.pyplot as plt

# Define a basic Splay Tree Node
class SplayTreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# Define the Splay Tree
class SplayTree:
    def __init__(self):
        self.root = None

    def _splay(self, root, key):
        if not root or root.key == key:
            return root

        temp = SplayTreeNode(None, None)
        left_tree = temp
        right_tree = temp

        while root and root.key != key:
            if key < root.key:
                if not root.left:
                    break
                if key < root.left.key:
                    root = self._rotate_right(root)
                    if not root.left:
                        break
                right_tree.left = root
                right_tree = root
                root = root.left
            else:
                if not root.right:
                    break
                if key > root.right.key:
                    root = self._rotate_left(root)
                    if not root.right:
                        break
                left_tree.right = root
                left_tree = root
                root = root.right

        left_tree.right = root.left
        right_tree.left = root.right
        if root:
            root.left = temp.right
            root.right = temp.left
        return root

    def _rotate_right(self, x):
        y = x.left
        if y:
            x.left = y.right
            y.right = x
        return y

    def _rotate_left(self, x):
        y = x.right
        if y:
            x.right = y.left
            y.left = x
        return y

    def insert(self, key, value):
        if not self.root:
            self.root = SplayTreeNode(key, value)
            return
        self.root = self._splay(self.root, key)
        if self.root.key == key:
            return
        node = SplayTreeNode(key, value)
        if key < self.root.key:
            node.left = self.root.left
            node.right = self.root
            self.root.left = None
        else:
            node.right = self.root.right
            node.left = self.root
            self.root.right = None
        self.root = node

    def search(self, key):
        if not self.root:
            return None
        self.root = self._splay(self.root, key)
        return self.root.value if self.root and self.root.key == key else None

# Simulate Dataset
dataset = {i: f"Data_{i}" for i in range(1, 10001)}  # 10,000 entries

# Splay Tree implementation
splay_tree = SplayTree()

# Insert data into Splay Tree
for key, value in dataset.items():
    splay_tree.insert(key, value)

# Simulate query workload
hot_keys = [100, 200, 300, 400, 500]
queries = hot_keys * 50 + [random.randint(1, 10000) for _ in range(500)]  # Repeated hot keys

# Traditional Search
start_time = time.time()
traditional_results = []
for key in dataset:
    if key in queries:
        traditional_results.append(dataset[key])
traditional_time = time.time() - start_time

# Splay Tree Search
start_time = time.time()
splay_results = [splay_tree.search(q) for q in queries]
splay_time = time.time() - start_time

# Heuristic-Based Cost Optimization
plans = [f"Plan_{i}" for i in range(1, 6)]
plan_costs = {plan: random.randint(10, 50) for plan in plans}

start_time = time.time()
selected_plans = [min(plan_costs, key=lambda x: plan_costs[x]) for _ in queries]
cbo_time = time.time() - start_time

# Visualization
methods = ["Traditional Search", "Splay Tree (Caching)", "Heuristic-Based Optimization"]
times = [traditional_time, splay_time, cbo_time]

plt.figure(figsize=(10, 6))
plt.bar(methods, times, color=["blue", "green", "orange"])
plt.title("Performance Comparison of Query Optimization Methods", fontsize=16)
plt.ylabel("Execution Time (seconds)", fontsize=14)
plt.xlabel("Optimization Method", fontsize=14)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Annotate the bars with their values
for i, time in enumerate(times):
    plt.text(i, time + 0.0005, f"{time:.6f}s", ha="center", fontsize=12, color="black")

plt.show()

# Print Results
print("Performance Comparison:")
print(f"Traditional Search Time: {traditional_time:.6f} seconds")
print(f"Splay Tree Search Time: {splay_time:.6f} seconds")
print(f"Heuristic-Based Optimization Time: {cbo_time:.6f} seconds")
