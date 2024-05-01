import copy
import pytest
from rainbow_merge_game import (
    check_structure_changed,
    handle_merges,
    handle_falls,
    check_first_column,
    check_for_black,
)

# Sample game board for testing
pre_list = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
]

blocks_list = copy.deepcopy(pre_list)


def test_handle_merges():
    def merge_function(x, y, blocks_list):
        return False  # Ensure no merges occur for this test

    merged_block = handle_merges(blocks_list, merge_function)
    assert merged_block is None  # No merges should occur


def test_handle_falls():
    fallen_block = handle_falls(blocks_list)
    assert fallen_block is None  # No falls should occur
