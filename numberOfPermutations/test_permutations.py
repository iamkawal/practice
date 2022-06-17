from permutations import FindNumberOfPermutations

testCases = \
    [{"smallString": "abc", "bigString": "aaa", "result": 0},\
    {"smallString": "abc", "bigString": "acb", "result": 1},\
    {"smallString": "abc", "bigString": "acbbca", "result": 2},\
    {"smallString": "abc", "bigString": "acbcabcaabbca", "result": 6}
]




def test_permutations():

     assert FindNumberOfPermutations(testCases[0]["smallString"], testCases[0]["bigString"]) != testCases[0]["result"], "something happend"