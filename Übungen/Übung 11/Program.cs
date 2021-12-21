/// <summary>
/// Determinstic algorithm for solving the SOS (Sum of subsets)-problem.
/// Based on a recursive traversal of a binary tree containing all possible subsets and their respective sums,
/// this algorithm determines wether a subset of <c>b</c> exists, such that the sum of this subset equals <c>a</c>.
/// </summary>
/// <param name="b">The <c>int</c>-array containg the set for the SOS-problem.</param>
/// <param name="a">The sum to target.</param>
/// <returns><c>true</c>, if <c>b</c> contains a subset adding up to <c>a</c>, otherwise <c>false</c></returns>
bool SOS(int[] b, int a, int length) 
{
    // Base cases
    if (a == 0) 
        return true; 
    if (length == 0 &&  a != 0) 
        return false;

    // Ignore all elements larger than the sum we are aiming at.
    if (b[length - 1] > a) 
        return SOS(b, a, length-1);
    /*
     Compute all possible computation paths: 
     First try to build up the sum including the last element of the current list range.
     Then try to build up the sum except the lasst element of the current list range, so we cover all cases of the given set.
     If we find one path building up a subset resulting in the given sum, return 1, else return 0.
    */
    return SOS(b, a, length-1) || SOS(b, a - b[length - 1], length - 1);
}

Random random = new Random();

/// <summary>
/// Function simulationg a fair coinflip.
/// </summary>
/// <returns></returns>
bool CoinFlip() 
{
    return random.Next() % 2 == 0;
}


/// <summary>
/// Probablibistic algorithm for solving the SOS (Sum of subsets)-problem.
/// Based on a fair coinflip, an element of the array gets added to the sum.
/// If the computed sum matches the given <c>a</c>, it will return <c>true</c>, otherwise <c>false</c>.
/// Probabilty of getting a correct result: 1/2^N > 0
/// </summary>
/// <param name="b">The <c>int</c>-array containg the set for the SOS-problem.</param>
/// <param name="a">The sum to target.</param>
/// <returns><c>true</c>, if <c>b</c> contains a subset adding up to <c>a</c>, otherwise <c>false</c></returns>
bool SOS_Prob(int[] b, int a) 
{
    int sum = 0;
    for (int i = 0; i < b.Length; i++) 
    {
        if (CoinFlip()) 
        {
            sum += b[i];
        }
    }
    return sum == a;
}



// Recursive, determnistic approach
Console.WriteLine("Deterministic algorithm");
Console.WriteLine("---------------------------------------------------------");
Console.WriteLine(SOS(new[] {12, 8, 4, 9, 3, 14, 6}, 38, 7));
Console.WriteLine(SOS(new[] {3, 5, 8, 12, 13, 17}, 19, 6));
Console.WriteLine(SOS(new[] {82313219, 89653282, 131596355, 74973315, 61341954, 45613571, 30409731,44042242, 106958851, 26746881, 119029763, 7372803, 57212929, 108134402, 13893635}, 484069451, 15));
Console.WriteLine(SOS(new[] {82313219, 89653282, 131596355, 74973315, 61341954, 45613571, 30409731,44042242, 106958851, 26746881, 119029763, 7372803, 57212929, 108134402, 13893635}, 396705997, 15));

Console.WriteLine();

// Probabilistic approach
Console.WriteLine("Probabilistic algorithm");
Console.WriteLine("---------------------------------------------------------");
Console.WriteLine(SOS_Prob(new[] {12, 8, 4, 9, 3, 14, 6}, 38));
Console.WriteLine(SOS_Prob(new[] {3, 5, 8, 12, 13, 17}, 19));
Console.WriteLine(SOS_Prob(new[] {82313219, 89653282, 131596355, 74973315, 61341954, 45613571, 30409731,44042242, 106958851, 26746881, 119029763, 7372803, 57212929, 108134402, 13893635}, 484069451));
Console.WriteLine(SOS_Prob(new[] {82313219, 89653282, 131596355, 74973315, 61341954, 45613571, 30409731,44042242, 106958851, 26746881, 119029763, 7372803, 57212929, 108134402, 13893635}, 396705997));