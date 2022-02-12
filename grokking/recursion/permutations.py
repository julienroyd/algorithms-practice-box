"""
We can generate all the permutations of some sequence using recursive functions.
1. To think of all the possibilities, draw the tree.
   -> n = number of levels. a = number of choices. a^n = number of permutations.
2. Then build the list of possibilities, use a recursive function where the order of
   actions and callbacks are the arms of the tree.
"""

"""
Example 1: Permutations of Heads or Tails (with replacement)
If we do n=3 throws and there are a=2 choices {H,T}, then there are 2^3 = 8 possible sequences (permutations).
       ______________
      /             \
     H               T
    /  \            /  \
   /    \          /    \
  H      T        H      T
 / \    / \      / \    / \
H   T  H   T    H   T  H   T
"""
def generate_coin_sequences(n):
    ans = []
    def recursive_flip(S):
        if len(S) == n:
            ans.append("".join(S))
        else:
            # Acting at a decision point...

            S.append("H")       # does option 1 (i.e. Heads)
            recursive_flip(S)   # goes to next level
            S.pop()             # un-does it

            S.append("T")       # does option 2 (i.e. Tail)
            recursive_flip(S)   # goes to next level
            S.pop()             # un-does it

    S = []
    recursive_flip(S)
    print(f"ans={ans}")

if __name__ == '__main__':
    generate_coin_sequences(n=2)
