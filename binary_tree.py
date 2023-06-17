from binarytree import Node, tree


def create_binary_tree():
    value = input("Enter the value for the root node (or leave blank [Enter] to quit): ")
    if value == '':
        return None

    root = Node(value)
    queue = [root]

    while queue:
        current_node = queue.pop(0)

        left_value = input(
            f"Enter the value for the left child of {current_node.value} (or leave blank [Enter] to quit): ")
        if left_value != '':
            current_node.left = Node(left_value)
            queue.append(current_node.left)

        right_value = input(
            f"Enter the value for the right child of {current_node.value} (or leave blank [Enter] to quit): ")
        if right_value != '':
            current_node.right = Node(right_value)
            queue.append(current_node.right)

    return root


def inorder_traversal(node):
    if node is None:
        return []

    result = []
    result += inorder_traversal(node.left)
    result.append(node.value)
    result += inorder_traversal(node.right)

    return result


def preorder_traversal(node):
    if node is None:
        return []

    result = [node.value]
    result += preorder_traversal(node.left)
    result += preorder_traversal(node.right)

    return result


def postorder_traversal(node):
    if node is None:
        return []

    result = []
    result += postorder_traversal(node.left)
    result += postorder_traversal(node.right)
    result.append(node.value)

    return result


def search_value(node, value, path=[], level=0):
    if node is None:
        return False, [], -1

    if node.value == value:
        path.append(node.value)
        return True, path, level

    # Recursively search in the left subtree
    target, left_path, left_level = search_value(node.left, value, path + [node.value], level + 1)
    if target:
        return True, left_path, left_level

    # Recursively search in the right subtree
    target, right_path, right_level = search_value(node.right, value, path + [node.value], level + 1)
    if target:
        return True, right_path, right_level

    return False, [], -1


def calculate_tree(node):
    if node is None:
        return {'height': 0, 'depth': 0, 'size': 0}

    left_height = calculate_tree(node.left)
    right_height = calculate_tree(node.right)

    if isinstance(left_height, dict) and isinstance(right_height, dict):
        height = max(left_height['height'], right_height['height']) + 1
        depth = height - 1
        size = left_height['size'] + right_height['size'] + 1

        data = {
            'height': height,
            'depth': depth,
            'size': size
        }

        return data
    else:
        # Handle the case where the left or right subtree is not None but does not have left or right attributes
        raise ValueError("Invalid node structure")


# Main program

run_program = True
creation_mode = True


def creation_menu():
    print("\n========================== Binary Tree Creation Menu =========================\n")
    print("1. Visualize the tree")
    print("2. Traverse the tree")
    print("3. Search a value in the tree")
    print("4. Show all (Visualization, Traverse, Height, Depth, Size)")
    print("5. Back to main menu (delete current tree)")
    print("6. Exit")


def main_menu():
    print("\n================================= Binary Tree ================================\n")
    print("1. Binary Tree Creation")
    print("2. Random Binary Tree Creation")
    print("3. Exit")


main_menu()
# check if the input is an integer, raise ValueError if not
choice = input("\nEnter your choice: ")
if not choice.isdigit():
    raise ValueError("Invalid input. Please enter a number.")

choice = int(choice)  # Convert the input to an integer

while run_program:
    if choice == 1:
        print("\n============================ Binary Tree Creation ============================\n")
        binary_tree = create_binary_tree()
        print("Tree Created Successfully!")

        creation_menu()
        creation_choice = input("\nEnter your choice (false input will destroy current progress): ")
        if not creation_choice.isdigit():
            raise ValueError("Invalid input. Please enter a number.")

        creation_choice = int(creation_choice)  # Convert the input to an integer

        while creation_mode:
            if creation_choice == 1:
                print("\nBinary Tree Visualization:")
                print(binary_tree)
                creation_menu()
                creation_choice = int(input("\nEnter your choice (false input will destroy current progress): "))

            if creation_choice == 2:
                print(binary_tree)
                print("\npre-order traversal:", preorder_traversal(binary_tree))
                print("in-order traversal:", inorder_traversal(binary_tree))
                print("post-order traversal:", postorder_traversal(binary_tree))
                creation_menu()
                creation_choice = int(input("\nEnter your choice (false input will destroy current progress): "))

            if creation_choice == 3:
                value_to_search = input("\nEnter the value to search: ")
                found, path, level = search_value(binary_tree, value_to_search)

                if found:
                    print(binary_tree)
                    print(f"\nThe value {value_to_search} is found in the tree. In level: {level}")
                    print(f"Full path: {path}")

                else:
                    print(binary_tree)
                    print(f"\nThe value {value_to_search} is not found in the tree.")

                creation_menu()
                creation_choice = int(input("\nEnter your choice (false input will destroy current progress): "))

            if creation_choice == 4:
                print("\nBinary Tree Visualization:")
                print(binary_tree)
                print("\npre-order traversal:", preorder_traversal(binary_tree))
                print("in-order traversal:", inorder_traversal(binary_tree))
                print("post-order traversal:", postorder_traversal(binary_tree))

                tree_data = calculate_tree(binary_tree)
                print(f"\nThe height (total level) of the tree is: {tree_data['height']}")
                print(f"The depth of the tree is: {tree_data['depth']}")
                print(f"The size of the tree is: {tree_data['size']}")

                creation_menu()
                creation_choice = int(input("\nEnter your choice (false input will destroy current progress): "))

            if creation_choice == 5:
                print("\nExiting creation menu...")
                main_menu()
                creation_mode = False
                choice = int(input("\nEnter your choice: "))

            if creation_choice == 6:
                print("\nExiting...")
                print("\nMade with love by: Agus Ardiansyah_L200214197")
                run_program = False
                creation_mode = False

    if choice == 2:
        tree_height = int(input("\nEnter the depth of the tree: "))
        is_perfect = input("Is the tree perfect? (y/n): ")
        letters = input("Do you want to use letters instead of numbers? (y/n): ")

        if is_perfect == "y":
            is_perfect = True
        else:
            is_perfect = False

        if letters == "y":
            letters = True
        else:
            letters = False

        my_bst = tree(height=tree_height, is_perfect=is_perfect, letters=letters)
        print("\nRandom Binary Tree Visualization:")
        print(my_bst)
        print("\npre-order traversal:", preorder_traversal(my_bst))
        print("in-order traversal:", inorder_traversal(my_bst))
        print("post-order traversal:", postorder_traversal(my_bst))

        bst_data = calculate_tree(my_bst)
        print(f"\nThe height (total level) of the tree is: {bst_data['height']}")
        print(f"The depth of the tree is: {bst_data['depth']}")
        print(f"The size of the tree is: {bst_data['size']}")

        main_menu()
        choice = int(input("\nEnter your choice: "))

    if choice == 3:
        print("Exiting...")
        print("\nMade with love by: Agus Ardiansyah_L200214197")
        run_program = False