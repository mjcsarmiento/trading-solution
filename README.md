# Trading Technical Challenge
This application uses Python to determine potential best trades based on historical data from CSV file. This consists of two different solutions which user can choose to run this application.

## Setup
This application runs in Python 3.
To run this application:
```
cd tracking-solution
python3 trading.py
```

## Using The Application
The application will ask for a CSV file to run, having `data_all.csv` as its default, if not supplied. There are other sample CSV files which can be used, but if the user wishes to use a different CSV file, it is highly recommended to include the file within the same directory to input its filename easily. (See example below)
```
Select .csv file to analyze (default - data_all.csv): data_3600.csv
```
Once file is selected, user can select solution (1) or (2) to run. (See example below)
```
Select solution (1 or 2): 1
```
After configuring both, the application will print out all the buy and sell positions with its profit and the total profit of all trades.
