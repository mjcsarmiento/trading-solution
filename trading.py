import csv
import sys
from decimal import Decimal

file = input('Select .csv file to analyze (default - data_all.csv): ') or 'data_all.csv'

solution = input('Select solution (1 or 2): ')

if not solution.isdigit() or (solution.isdigit() and int(solution) not in [1,2]):
    print('\nPlease select 1 or 2 for solution.')
    sys.exit(0)

with open(file) as csvfile:
    reader = csv.reader(csvfile)

    # Get all values and remove first row which contains column names
    data = [(row[0], Decimal(row[1])) for row in reader if not row[1].isalpha()]

    solution = int(solution)
    if solution == 1:
        potential_profits = []
        # Get all best trades from each minute to 30-59 minutes from buy
        for i in range(len(data)):
            if i + 30 > len(data) - 1:
                break

            open_trade = data[i]

            close_start_index = i + min(30, len(data) - i)
            close_end_index = i + min(59, len(data) - i)
            potential_close_trades = data[close_start_index:close_end_index + 1]
            max_value = max(t[1] for t in potential_close_trades)
            index = [i for i, item in enumerate(potential_close_trades) if item[1] == max_value][0]
            close_trade = potential_close_trades[index]

            profit = close_trade[1] - open_trade[1]
            trade_data = {
                'profit': profit,
                'open': open_trade,
                'close': close_trade,
            }
            potential_profits.append(trade_data)

        # Get best trade for every 30 minutes to maximize the amount of times to trade
        total_profit = 0
        index = 0
        while len(data) > index + 31:
            # Set end index to + 31 to make 30th value inclusive
            trades = potential_profits[index:index + 31]

            # Get max profit of every 30 minutes
            max_profit = max(t['profit'] for t in trades)
            index = [i for i, item in enumerate(trades) if item['profit'] == max_profit][0]

            profit = trades[index]['profit']
            open_trade = trades[index]['open']
            close_trade = trades[index]['close']
            if profit > 0:
                total_profit += profit
                print('Open at {}, close at {} for profit {}'.format(open_trade, close_trade, profit))

            next_trade_index = int(close_trade[0]) + 1
            index += next_trade_index

        print('Total profit {}'.format(total_profit))
    else:
        total_profit = 0
        index = 0
        while len(data) > index:
            open_start_index = index
            open_end_index = open_start_index + min(31, len(data) - open_start_index - 1)
            open_trade = min(data[index:open_end_index])
            index = int(open_trade[0])

            # Check if closing trade is still possible, break loop if not
            if index + 30 > len(data) - 1:
                break

            close_start_index = index + min(30, len(data) - index)
            close_end_index = index + min(59, len(data) - index)

            close_trade = max(data[close_start_index:close_end_index])
            index = int(close_trade[0]) + 1

            profit = close_trade[1] - open_trade[1]
            if profit > 0:
                total_profit += profit
            else:
                # If negative profit, move starting pointer for getting open trades
                index = open_start_index + 1
                continue

            print('Open at {}, close at {} for profit {}'.format(open_trade, close_trade, profit))
        print('Total profit is {}'.format(total_profit))
