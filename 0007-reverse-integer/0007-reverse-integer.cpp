class Solution {
public:
    int reverse(int x) {
    int newnums = 0, flag = 0;
    int n = 0;
    if (x < 0)
    {
        flag = 1;
        x = abs(x);
    }
    cout << "x is equal to " << x; 
    while (x != 0)
    { 
        if (abs(newnums) > 214748364)
        {
            return 0;
        }
        newnums = (newnums * 10) + x%10;
        x = x / 10;
    }
    if (flag == 1)
    {
        return (newnums*-1);
    }
    else
    {
        return (newnums);
    }
        
    }
};