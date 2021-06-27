import pytest
import os

from whatthelog.markovchain.masm import MarkovChain
from whatthelog.definitions import PROJECT_ROOT


@pytest.fixture()
def masm():
    return MarkovChain(os.path.join(PROJECT_ROOT, 'tests/resources/testlogs/'),
                       config_file=os.path.join(PROJECT_ROOT, 'resources/config.json'))


def test_get_duplicate_rows(masm: MarkovChain):
    masm.transitionMatrix = [[0.5, 0, 0.5],
                             [  0, 1,   0],
                             [0.5, 0, 0.5]]

    result = masm.find_duplicates(threshold=0.0, row_duplicates=True)

    assert len(result) == 1
    assert len(result[0]) == 2
    assert result[0] == [0, 2]


def test_get_duplicate_columns(masm: MarkovChain):
    masm.transitionMatrix = [[  0, 0.5, 0.5],
                             [0.2, 0.3, 0.3],
                             [  0, 0.5, 0.5]]

    result = masm.find_duplicates(threshold=0.0, row_duplicates=False)

    assert len(result) == 1
    assert len(result[0]) == 2
    assert result[0] == [1, 2]

def test_get_duplicate_rows_2(masm: MarkovChain):
    masm.transitionMatrix = [[0.3, 0.3, 0.3],
                             [0.3, 0.3, 0.3],
                             [0.3, 0.3, 0.3]]

    result = masm.find_duplicates(threshold=0.0, row_duplicates=True)

    assert len(result) == 1
    assert len(result[0]) == 3
    assert result[0] == [0, 1, 2]


def test_get_duplicate_columns_2(masm: MarkovChain):
    masm.transitionMatrix = [[0.3, 0.3, 0.3],
                             [0.3, 0.3, 0.3],
                             [0.3, 0.3, 0.3]]

    result = masm.find_duplicates(threshold=0.0, row_duplicates=False)

    assert len(result) == 1
    assert len(result[0]) == 3
    assert result[0] == [0, 1, 2]


def test_get_duplicate_threshold_1(masm: MarkovChain):
    masm.transitionMatrix = [[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]]

    result = masm.find_duplicates(threshold=1, row_duplicates=False)

    assert len(result) == 1
    assert len(result[0]) == 3
    assert result[0] == [0, 1, 2]

    result = masm.find_duplicates(threshold=1, row_duplicates=True)

    assert len(result) == 1
    assert len(result[0]) == 3
    assert result[0] == [0, 1, 2]


def test_get_duplicate_threshold_0(masm: MarkovChain):
    masm.transitionMatrix = [[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]]

    result = masm.find_duplicates(threshold=0, row_duplicates=False)

    assert len(result) == 0

    result = masm.find_duplicates(threshold=0, row_duplicates=True)

    assert len(result) == 0


def test_find_prop_1(masm: MarkovChain):
    masm.transitionMatrix = [[  0,   1,   0],
                             [0.3, 0.3, 0.3],
                             [0.3, 0.3, 0.3]]

    result = masm.find_prop_1(threshold=0.0)

    assert len(result) == 1
    assert len(result[0]) == 2
    assert result[0] == [0, 1]


def test_find_prop_1_2(masm: MarkovChain):
    masm.transitionMatrix = [[  0, 0.9, 0.1],
                             [0.3, 0.3, 0.3],
                             [0.3, 0.3, 0.3]]

    result = masm.find_prop_1(threshold=0.2)

    assert len(result) == 1
    assert len(result[0]) == 2
    assert result[0] == [0, 1]


def test_merge_state(masm: MarkovChain):
    masm.transitionMatrix = [[  0, 0.9, 0.1],
                             [0.3, 0.3, 0.3],
                             [0.3, 0.3, 0.3]]

    masm.remove(0, 1)

    assert len(masm.transitionMatrix) == 2
    assert len(masm.transitionMatrix[0]) == 2
    # View guidelines in the paper
    assert masm.transitionMatrix == [[0.75, 0.2], [0.6, 0.3]]
