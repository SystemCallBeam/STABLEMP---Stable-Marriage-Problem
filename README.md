# STABLEMP---Stable-Marriage-Problem
There are given n men and n women. Each woman ranks all men in order of her preference (her first choice, her second choice, and so on). Similarly, each man sorts all women according to his preference. The goal is to arrange n marriages in such a way that if a man m prefers some woman w more than his wife, then w likes her husband more than m. In this way, no one leaves his partner to marry somebody else. This problem always has a solution and your task is to find one.

Input
The first line contains a positive integer t <= 100 indicating the number of test cases. Each test case is an instance of the stable marriage problem defined above. The first line of each test case is a positive integer n <= 500 (the number of marriages to find). The next n lines are the woman's preferences: ith line contains the number i (which means that this is the list given by the ith woman) and the numbers of men (the first choice of ith woman, the second choice,...). Then, the men's preferences follow in the same format.

Output
For each test case print n lines, where each line contains two numbers m and w, which means that the man number m and the woman number w should get married.
