/*
function maxStocks(N, stocks_and_values, amount):
    //create a 2D array to store results of subproblems (memoization)
    dp[N + 1][amount + 1]

    // Initialize base cases
    for i from 0 to N:
        dp[i][0] = 0  //zero investment yields zero stocks
    for j from 0 to amount:
        dp[0][j] = 0  //no stocks available, regardless of the investment amount

    //dp array using dynamic programming
    for i from 1 to N:
        for j from 1 to amount:
            if stocks_and_values[i - 1][1] > j:
                //if the current stock's value is greater than the remaining amount, skip it
                dp[i][j] = dp[i - 1][j]
            else:
                //choose the maximum between including and excluding the current stock
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stocks_and_values[i - 1][1]] + stocks_and_values[i - 1][0])

    // The final result is stored in dp[N][amount]
    return dp[N][amount]
*/
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int maxStocks(int N, vector<vector<int>>& stocks_and_values, int amount) {
    vector<vector<int>> dp(N + 1, vector<int>(amount + 1, 0));

    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= amount; ++j) {
            if (stocks_and_values[i - 1][1] > j) {
                dp[i][j] = dp[i - 1][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stocks_and_values[i - 1][1]] + stocks_and_values[i - 1][0]);
            }
        }
    }

    return dp[N][amount];
}

int main() {
    ifstream infile("input.txt"); // Assuming input file is named input.txt

    // Read N (number of stocks)
    int N;
    infile >> N;

    // Read stock information
    vector<vector<int>> stocks_and_values(N, vector<int>(2));
    for (int i = 0; i < N; ++i) {
        infile >> stocks_and_values[i][0] >> stocks_and_values[i][1];
    }

    // Read investment amount
    int amount;
    infile >> amount;

    infile.close();

    // Calculate and print the result
    int result = maxStocks(N, stocks_and_values, amount);
    cout << "Maximum number of stocks that can be purchased: " << result << endl;

    return 0;
}
