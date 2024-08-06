from histogram import histogram

from testing import assert_equal

def test_histogram():
  data = List[Int](1,2,3)
  expect = (List[Int](1,2,3), List[Float64](1/3,1/3,1/3))
  assert_equal(histogram(data), expect)
