int SOS(int[] b, int a, int length) {
    
    // Base cases
    if (a == 0) 
        return 1; 
    if (length == 0 &&  a != 0) 
        return 0;

    // Ignore all elements larger than the sum we are aiming at.
    if (b[length - 1] > a) 
        return SOS(b, a, length-1);
    
    /*
     Compute all possible computation paths: 
     First try to build up the sum including the last element of the current list range.
     Then try to build up the sum except the lasst element of the current list range, so we cover all cases of the given set.
     If we find one path building up a subset resulting in the given sum, return 1, else return 0.
    */
    if (SOS(b, a, length-1) == 1 || SOS(b, a - b[length - 1], length - 1) == 1)
        return 1;

    return 0;
}



Console.WriteLine(SOS(new[] {12, 8, 4, 9, 3, 14, 6}, 38, 7));
Console.WriteLine(SOS(new[] {3, 5, 8, 12, 13, 17}, 19, 6));
Console.WriteLine(SOS(new[] {82313219, 89653282, 131596355, 74973315, 61341954, 45613571, 30409731,44042242, 106958851, 26746881, 119029763, 7372803, 57212929, 108134402, 13893635}, 484069451, 15));
Console.WriteLine(SOS(new[] {82313219, 89653282, 131596355, 74973315, 61341954, 45613571, 30409731,44042242, 106958851, 26746881, 119029763, 7372803, 57212929, 108134402, 13893635}, 396705997, 15));