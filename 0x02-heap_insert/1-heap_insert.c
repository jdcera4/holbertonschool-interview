#include "binary_trees.h"

/**
 * heap_insert - Inserts a value into a Max Binary Heap
 *
 * @root: Double pointer to the root node of the Heap
 * 
 * @value: The value store in the node to be inserted
 * 
 * Return: A tree with max heap ordering
 */

heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *node, *parent;

	/* For an empty tree, create nodes and return tree pointer to tree */
	if (*root == NULL)
	{
		node = binary_tree_node(*root, value);
		*root = node;
		return (*root);
	}
	node = *root;

	/* Traverse tree */
	while (node != NULL)
	{
		parent = node;
		/* Ignore duplicates */
		if (node->n == value)
			return node_swap(node);

		/* Sort tree into BST formation */
		if (value > node->n)
			node = parent->left;
		else
			node = node->right;
	}

	/* Sort parent nodes */
	if (value > parent->n)
	{
		parent->left = binary_tree_node(parent, value);
		return (parent->left);
	}
	else
	{
		parent->right = binary_tree_node(parent, value);
		return (parent->right);
	}
}


/**
 * node_swap - Swaps current node with larger node
 *
 * @node: Pointer to current node
 * 
 * Return: A new node
 */

heap_t *node_swap(heap_t *node)
{
	while (node && node->parent)
	{
		while (node->n > node->parent->n)
		{
			node = node->parent;
			node->n += node->parent->n;
			node->parent->n -= node->n;
			node->parent->n = node->n - node->parent->n;
		}
	}
	return (node);
}
