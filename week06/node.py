from __future__ import annotations  # for cool type hinting


class Node:
    """A simple binary tree node for a basic Huffman encoder."""

    def __init__(self,  symbol: str | None, frequency: int):
        """Object constructor.

        Inputs
        ------
        frequency : int
          The frequency represented by this node. If the node has also a symbol,
          this is the frequency of the symbol. If no symbol is present, this is
          the sum of frequencies of the node's subtrees.
        symbol : char
          The symbol whose frequency we capture. If symbol is None, the node
          captures frequencies for subtrees under the node.

        Returns
        -------
        Instance of Node object with fields:
          frequency : as described above
          symbol : as described above
          left : pointer to left node child (default none)
          right : pointer to right node child (default none)
        """
        self.__frequency: int = frequency
        self.__symbol: str | None = symbol
        self.__left: None | Node = None
        self.__right: None | Node = None

    def __lt__(self, other: Node):
        """Redefine < for node to be based on frequency value"""
        return self.__frequency < other.get_frequency()

    def set_left(self, left: Node | None):
        """Setter for left child."""
        self.__left = left

    def set_right(self, right: Node | None):
        """Setter for right child."""
        self.__right = right

    def has_left(self):
        """Predicate accessor for left child"""
        return self.__left is not None

    def has_right(self):
        """Predicate accessor for right child"""
        return self.__right is not None

    def get_left(self):
        """Accessor for left child"""
        return self.__left

    def get_right(self):
        """Accessor for right child."""
        return self.__right

    def get_symbol(self) -> str:
        """Accessor for the symbol in a leaf node"""
        return self.__symbol

    def get_frequency(self):
        """Accessor for frequency."""
        return self.__frequency

    def is_leaf(self) -> bool:
        """Determines if node is leaf node, indicated by the
        absence of both child pointers."""
        return self.__left is None and self.__right is None

    def __str__(self):
        """String representation of object."""
        return f"[ {self.__symbol}: {self.__frequency} ]"