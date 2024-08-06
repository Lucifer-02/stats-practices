from lucifer_stats.histogram import histogram

from testing import assert_equal

def test_histogram():
  assert_equal(histogram([1,2,3]), ([1,2,3], [1/3, 1/3, 1/3]))