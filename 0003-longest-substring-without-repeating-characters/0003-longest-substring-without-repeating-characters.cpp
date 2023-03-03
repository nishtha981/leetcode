class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int l=0,r=0;
        int len=s.size(),length=0;
        vector<int> str(256,-1);
        while(r<len)
        {
            if(str[s[r]]!=-1)
                l=max(str[s[r]]+1,l);
            str[s[r]]=r;
            
            length=max(length,r-l+1);
            r++;
        }
        return length;
    }
};