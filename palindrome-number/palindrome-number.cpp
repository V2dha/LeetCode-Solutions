class Solution {
public:
    bool isPalindrome(int x) {
        int temp=x, rem=0;
        double rev=0;
        if(x<0)
            return false;
        else
            {while(x!=0){
                rem = x%10;
                rev = (rev*10) + rem;
                x = x/10;
            }
            if(rev==temp){
                return true;
            }
            else
                return false;}
    }
};
