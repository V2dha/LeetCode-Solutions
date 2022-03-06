class Solution:
    def countOrders(self, n: int) -> int:
        """
        Consider n = 3 orders.

Now consider one particular sequence; S = [(P1, D1), (P2, D2), (P3, D3)]
Now let us consider an arrangement like this, where P1 comes before P2 and P2 comes before P3, i.e., P1 ... P2 ... P3 ...
Now we observe that -

D3 can only be placed in one position (1 ways), i.e., at the last after P3. So, the sequence becomes - P1 ... P2 ... P3 ... D3 ...
D2 can be placed at any one of three positions (3 ways), i.e., between P2 and P3, or between P3 and D3, or after D3. So, one of the sequence becomes - P1 ... P2 ... P3 ... D2 ... D3 ...
D1 can be placed at any one of the above five positions (5 ways).
So, for the above particular sequence S we have - 1 * 3 * 5 = 15 ways.
But the sequence can be arranged in 3! ways. So, the ans is 3! * (1 * 3 * 5).

In general, the ans is - n! * (1 * 3 * 5 * ... * (2*n-1)).

Time Complexity - O(n)
Space Complexity - O(1)
        """
        res = 1
        for i in range(1, n+1):
            res *= i*(2*i-1)
        return res%(10**9+7)