# def longest_common_subsequence(seq1, seq2, idx1=0, idx2=0) -> int:
#     if idx1 == len(seq1) or idx2 == len(seq2):
#         return 0
#     elif seq1[idx1] == seq2[idx2]:
#         return 1 + longest_common_subsequence(seq1, seq2, idx1+1, idx2+1)
#     else:
#         option1 = longest_common_subsequence(seq1, seq2, idx1+1, idx2)
#         option2 = longest_common_subsequence(seq1, seq2, idx1, idx2+1)
#         return max(option1, option2)
#
#
# print(longest_common_subsequence('serendipitous', 'precipitation'))


# def longest_common_subsequence_memo(seq1, seq2):
#     memo = {}
#
#     def recursive(idx1=0, idx2=0):
#         key = (idx1, idx2)
#         if key in memo:
#             return memo[key]
#         elif idx1 == len(seq1) or idx2 == len(seq2):
#             memo[key] = 0
#         elif seq1[idx1] == seq2[idx2]:
#             memo[key] = 1 + recursive(idx1+1, idx2+1)
#         else:
#             memo[key] = max(recursive(idx1+1, idx2), recursive(idx1, idx2+1))
#
#         return memo[key]
#
#     return recursive()
#
#
# print(longest_common_subsequence_memo('serendipitous', 'precipitation'))


def longest_common_subsequence_dynamic(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for _ in range(n1+1)] for _ in range(n2+1)]

    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                table[idx1+1][idx2+1] = 1 + table[idx1][idx2]
            else:
                table[idx1+1][idx2+1] = max(table[idx1+1][idx2], table[idx1][idx2+1])

    return table[-1][-1]


print(longest_common_subsequence_dynamic('serendipitous', 'precipitation'))
