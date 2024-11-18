import random
import time

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

        # Create a temporary node to hold the splay structure
        temp = SplayTreeNode(None, None)
        left_tree = temp
        right_tree = temp

        while root and root.key != key:
            if key < root.key:
                if not root.left:
                    break
                if key < root.left.key:  # Zig-Zig (Left Left)
                    root = self._rotate_right(root)
                    if not root.left:
                        break
                # Link Right
                right_tree.left = root
                right_tree = root
                root = root.left
            else:
                if not root.right:
                    break
                if key > root.right.key:  # Zag-Zag (Right Right)
                    root = self._rotate_left(root)
                    if not root.right:
                        break
                # Link Left
                left_tree.right = root
                left_tree = root
                root = root.right

        # Reassemble
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



# Generate a large dataset
dataset = {i: f"Data_{i}" for i in range(1, 10001)}  # 10,000 entries

# Splay Tree implementation
splay_tree = SplayTree()

# Insert data into the Splay Tree
for key, value in dataset.items():
    splay_tree.insert(key, value)

# Simulate a skewed query workload with repeated hot keys
hot_keys = [100, 200, 300, 400, 500]
queries = hot_keys * 500 + [random.randint(1, 1000000000) for _ in range(50)]  # 50 repetitions of hot keys

# Measure traditional search time
start_time = time.time()
traditional_results = []
for key in dataset:
    if key in queries:
        traditional_results.append(dataset[key])
traditional_time = time.time() - start_time

# Measure Splay Tree search time
start_time = time.time()
splay_results = [splay_tree.search(q) for q in queries]
splay_time = time.time() - start_time

# Print Results
print("Performance Comparison:")
print(f"Traditional Search Time: {traditional_time:.6f} seconds")
print(f"Splay Tree Search Time: {splay_time:.6f} seconds")

# Visualization (Optional)
try:
    import matplotlib.pyplot as plt

    plt.bar(["Traditional", "Splay Tree"], [traditional_time, splay_time], color=["blue", "green"])
    plt.title("Query Execution Time Comparison")
    plt.ylabel("Time (seconds)")
    plt.show()
except ImportError:
    print("Matplotlib not installed. Skipping visualization.")
