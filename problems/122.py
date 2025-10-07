def maxProfit(prices: list[int]) -> int:
    founding = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            founding += prices[i+1] - prices[i]
    
    return founding

def main():
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))

if __name__ == "__main__":
    main()