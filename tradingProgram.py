from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.live import StockDataStream
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus
import plotly.graph_objects as go
import plotly.express as px
import alpaca_trade_api as api
import time

#ADD REAL AND PAPER OPTION FOR BOTH TRADING TYPES3

def order():
    def limitOrder():
        accountType = input("Paper or Real? ")
        if accountType == "Paper":
            trading_client_paper = TradingClient("PK4QWK27RIXPO7TSPFZE", "rYdkMPN7maso16TpwkvAnebOMl7dlnUU7hEzp1BT")
            print("Account Number: ", trading_client_paper.get_account().account_number)
            print("Buying Power: ", trading_client_paper.get_account().buying_power)
            print("Balance: ", trading_client_paper.get_account().cash)
            print(trading_client_paper.get_account().currency)
            def limit_order_BUY_DAY():
                limit_order_data = LimitOrderRequest(
                    symbol=input("Enter the stock that you would like to invest in: "),
                    qty = int(input("How many shares do you want to buy: ")),
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    limit_price = int(input("Limit Price: ")),
                    stop_price = int(input("Stop Price: ")),
                )
                limit_order = trading_client_paper.submit_order(limit_order_data)
                print(limit_order)
            def limit_order_BUY_GTC():
                limit_order_data = LimitOrderRequest(
                    symbol=input("Enter the stock that you would like to invest in: "),
                    qty = int(input("How many shares do you want to buy: ")),
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.GTC,
                    limit_price = int(input("Limit Price: ")),
                    stop_price = int(input("Stop Price: ")),
                )
                limit_order = trading_client_paper.submit_order(limit_order_data)
                print(limit_order)
            def limit_order_SELL_DAY():
                limit_order_data = LimitOrderRequest(
                    symbol=input("Enter the stock that you would like to invest in: "),
                    qty = int(input("How many shares do you want to buy: ")),
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY,
                    limit_price = int(input("Limit Price: ")),
                    stop_price = int(input("Stop Price: ")),
                )
                limit_order = trading_client_paper.submit_order(limit_order_data)
                print(limit_order)
            def limit_order_SELL_GTC():
                limit_order_data = LimitOrderRequest(
                    symbol=input("Enter the stock that you would like to invest in: "),
                    qty = int(input("How many shares do you want to buy: ")),
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC,
                    limit_price = int(input("Limit Price: ")),
                    stop_price = int(input("Stop Price: ")),
                )
                limit_order = trading_client_paper.submit_order(limit_order_data)
                print(limit_order)

            tradeType = input("Buy or Sell?: ")
            TIF = input("Set the time in force: ")
            if tradeType == "Buy" and TIF == "Day":
                limit_order_BUY_DAY()
            elif tradeType == "Sell" and TIF == "Day":
                limit_order_SELL_DAY()
            elif tradeType == "Buy" and TIF == "GTC":
                limit_order_BUY_GTC()
            elif tradeType == "Sell" and TIF == "GTC":
                limit_order_SELL_GTC()
            time.sleep(1)
            exit = input("If you would like to go back to menu, type 'Exit': ")
            if exit == "Exit":
                menu()

        elif accountType == "Real":
            ALPACA_API_KEY ="AKN1M1WY7OYYTT01MJMO"
            ALPACA_SECRET_KEY = "2coKAKBj8qFBBouEQghxxKn7L1bGqN1cXxbJdNS9"
            alpaca = api.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, "https://api.alpaca.markets")
            #trading_client_real = TradingClient("AKBJPRCOACMY4FGDG5EZ", "8fCyzocX5QWV1GVoW0eMvew0JbP9UfGLg7pzmmi0")
            print("Account Number: ", alpaca.get_account().account_number)
            print("Buying Power: ", alpaca.get_account().buying_power)
            print("Balance: ", alpaca.get_account().cash)
            print(alpaca.get_account().currency)
            print("Remember, w/a REAL account you're limited to 3 trades")
            def limit_order_BUY_DAY():
                limit_order_data = LimitOrderRequest(
                    symbol=input("Enter the stock that you would like to invest in: "),
                    qty = int(input("How many shares do you want to buy: ")),
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    limit_price = int(input("Limit Price: ")),
                    stop_price = int(input("Stop Price: ")),
                )
                limit_order = alpaca.submit_order(limit_order_data)
                print(limit_order)
            def limit_order_BUY_GTC():
                limit_order_data = LimitOrderRequest(
                    symbol=input("Enter the stock that you would like to invest in: "),
                    qty = int(input("How many shares do you want to buy: ")),
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.GTC,
                    limit_price = int(input("Limit Price: ")),
                    stop_price = int(input("Stop Price: ")),
                )
                limit_order = alpaca.submit_order(limit_order_data)
                print(limit_order)
            def limit_order_SELL_DAY():
                limit_order_data = LimitOrderRequest(
                    symbol=input("Enter the stock that you would like to invest in: "),
                    qty = int(input("How many shares do you want to buy: ")),
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY,
                    limit_price = int(input("Limit Price: ")),
                    stop_price = int(input("Stop Price: ")),
                )
                limit_order = alpaca.submit_order(limit_order_data)
                print(limit_order)
            def limit_order_SELL_GTC():
                limit_order_data = LimitOrderRequest(
                    symbol=input("Enter the stock that you would like to invest in: "),
                    qty = int(input("How many shares do you want to buy: ")),
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC,
                    limit_price = int(input("Limit Price: ")),
                    stop_price = int(input("Stop Price: ")),
                )
                limit_order = alpaca.submit_order(limit_order_data)
                print(limit_order)

            tradeType = input("Buy or Sell?: ")
            TIF = input("Set the time in force: ")
            if tradeType == "Buy" and TIF == "Day":
                limit_order_BUY_DAY()
            elif tradeType == "Sell" and TIF == "Day":
                limit_order_SELL_DAY()
            elif tradeType == "Buy" and TIF == "GTC":
                limit_order_BUY_GTC()
            elif tradeType == "Sell" and TIF == "GTC":
                limit_order_SELL_GTC()
            time.sleep(1)
            exit = input("If you would like to go back to menu, type 'Exit': ")
            if exit == "Exit":
                menu()

    def marketOrder():
        accountType = input("Paper or Real? ")
        if accountType == "Paper":
            trading_client_paper = TradingClient("PK4QWK27RIXPO7TSPFZE", "rYdkMPN7maso16TpwkvAnebOMl7dlnUU7hEzp1BT")
            print("Account Number: ", trading_client_paper.get_account().account_number)
            print("Buying Power: ", trading_client_paper.get_account().buying_power)
            print("Balance: ", trading_client_paper.get_account().cash)
            print(trading_client_paper.get_account().currency)
            def market_order_buy_day():
                market_order_data = MarketOrderRequest(
                    symbol=input("Enter the stock that you would like to BUY: "),
                    qty = int(input("BUY Quantity: ")),
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                )
                market_order = trading_client_paper.submit_order(market_order_data)
                print(market_order)
            def market_order_sell_day():
                market_order_data = MarketOrderRequest(
                    symbol=input("Enter the stock that you would like to SELL in: "),
                    qty = int(input("SELL Quantity: ")),
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY
                )
                market_order = trading_client_paper.submit_order(market_order_data)
                print(market_order)
            def market_order_buy_gtc():
                market_order_data = MarketOrderRequest(
                    symbol=input("Enter the stock that you would like to BUY in: "),
                    qty = int(input("BUY Quantity: ")),
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.GTC
                )
                market_order = trading_client_paper.submit_order(market_order_data)
                print(market_order)
            def market_order_sell_gtc():
                market_order_data = MarketOrderRequest(
                    symbol=input("Enter the stock that you would like to SELL in: "),
                    qty = int(input("SELL Quantity: ")),
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC
                )  
                market_order = trading_client_paper.submit_order(market_order_data)
                print(market_order)
            tradeType = input("Buy or Sell?: ")
            TIF = input("Set the time in force: ")
            if tradeType == "Buy" and TIF == "Day":
                market_order_buy_day()
            elif tradeType == "Sell" and TIF == "Day":
                market_order_sell_day()
            elif tradeType == "Buy" and TIF == "GTC":
                market_order_buy_gtc()
            elif tradeType == "Sell" and TIF == "GTC":
                market_order_sell_gtc()
            time.sleep(1)
            exit = input("If you would like to go back to menu, type 'Exit': ")
            if exit == "Exit":
                menu()
        if accountType == "Real":
            ALPACA_API_KEY ="AKN1M1WY7OYYTT01MJMO"
            ALPACA_SECRET_KEY = "2coKAKBj8qFBBouEQghxxKn7L1bGqN1cXxbJdNS9"
            alpaca = api.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, "https://api.alpaca.markets")
            #trading_client_real = TradingClient("AKN1M1WY7OYYTT01MJMO", "2coKAKBj8qFBBouEQghxxKn7L1bGqN1cXxbJdNS9")
            print("Account Number: ", alpaca.get_account().account_number)
            print("Buying Power: ", alpaca.get_account().buying_power)
            print("Balance: ", alpaca.get_account().cash)
            print(alpaca.get_account().currency)
            def market_order_buy_day():
                market_order_data = MarketOrderRequest(
                    symbol=input("Enter the stock that you would like to BUY: "),
                    qty = int(input("BUY Quantity: ")),
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                )
                market_order = alpaca.submit_order(market_order_data)
                print(market_order)
            def market_order_sell_day():
                market_order_data = MarketOrderRequest(
                    symbol=input("Enter the stock that you would like to SELL in: "),
                    qty = int(input("SELL Quantity: ")),
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY
                )
                market_order = alpaca.submit_order(market_order_data)
                print(market_order)
            def market_order_buy_gtc():
                market_order_data = MarketOrderRequest(
                    symbol=input("Enter the stock that you would like to BUY in: "),
                    qty = int(input("BUY Quantity: ")),
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.GTC
                )
                market_order = alpaca.submit_order(market_order_data)
                print(market_order)
            def market_order_sell_gtc():
                market_order_data = MarketOrderRequest(
                    symbol=input("Enter the stock that you would like to SELL in: "),
                    qty = int(input("SELL Quantity: ")),
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC
                )  
                market_order = alpaca.submit_order(market_order_data)
                print(market_order)
            tradeType = input("Buy or Sell?: ")
            TIF = input("Set the time in force: ")
            if tradeType == "Buy" and TIF == "Day":
                market_order_buy_day()
            elif tradeType == "Sell" and TIF == "Day":
                market_order_sell_day()
            elif tradeType == "Buy" and TIF == "GTC":
                market_order_buy_gtc()
            elif tradeType == "Sell" and TIF == "GTC":
                market_order_sell_gtc()
            time.sleep(1)
            exit = input("If you would like to go back to menu, type 'Exit': ")
            if exit == "Exit":
                menu()

    orderType = input("Would you like to submit a Market Order (M) or a Limit Order? (L): ")
    #TIF = input("Set the time in force: ")
    if orderType == "M":
        marketOrder()
    elif orderType == "L":
        limitOrder()
    
#Cancels any open orders
def cancelOrders():
    trading_client = TradingClient("PK4QWK27RIXPO7TSPFZE", "rYdkMPN7maso16TpwkvAnebOMl7dlnUU7hEzp1BT")
    request_params = GetOrdersRequest(
    status = QueryOrderStatus.OPEN
    
    )
    orders = trading_client.get_orders(request_params)

    for order in orders:
        print(order.id)
        trading_client.cancel_order_by_id(order.id)

#Streams live trades
def streamData():
    try:
        stream = StockDataStream("PK4QWK27RIXPO7TSPFZE", "rYdkMPN7maso16TpwkvAnebOMl7dlnUU7hEzp1BT")
        async def handle_quote(data):
            print(data)
        while True:
            Symbol = input("Which symbol do you want to stream?\nOR type 'Back' to go back to menu:")
            if Symbol == 'Back':
                menu()
            else:
                stream.subscribe_quotes(handle_quote, Symbol)
                stream.run()
    except KeyboardInterrupt:
        print('Stream Interrupted')



def getPositions():
    accountType = input("Real or Paper? ")
    if accountType == "Paper":
        trading_client = TradingClient("PK4QWK27RIXPO7TSPFZE", "rYdkMPN7maso16TpwkvAnebOMl7dlnUU7hEzp1BT")
        def backtomenu():
            back = input("Type 'Back' to go back to menu: ")
            if back == "Back":
                menu()
            else:
                print("Invalid input. Please try again.")
                time.sleep(1) 
                showPos()
        def status():
            stats = input("To see additional stock stats, type 'STATS': ")
            if stats == "STATS":
                pos = trading_client.get_all_positions()
                for position in pos:
                    print("Current price: " + position.symbol, position.current_price)
                    print("Balance: ", trading_client.get_account().cash)
                    print("Last day price: " + position.lastday_price)
                    print("Change today: " + position.change_today)
                time.sleep(5)
                backtomenu()
            else:
                backtomenu()
        def showPos():
            print("Here is your current position(s): ")
            pos = trading_client.get_all_positions()
            time.sleep(1)
        
            for position in pos:
                print("Current price: " + position.symbol, position.current_price)
                print("Balance: ", trading_client.get_account().cash)
                time.sleep(1)
                status()
            
        
        showPos() 
            
    elif accountType == "Real":
        ALPACA_API_KEY ="AKN1M1WY7OYYTT01MJMO"
        ALPACA_SECRET_KEY = "2coKAKBj8qFBBouEQghxxKn7L1bGqN1cXxbJdNS9"
        alpaca = TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY, "https://api.alpaca.markets")
        print("Here is your current position(s): ")
        pos = alpaca.get_all_positions() #FIX
        for position in pos:
            print(position.symbol, position.current_price)
            print("Change today: " + position.change_today)
            print("Last day price: " + position.lastday_price)
    
        time.sleep(2)
        def backtomenu():
            back = input("Type 'Back' to go back to menu: ")
            if back == "Back":
                menu()
            else:
                print("Invalid input. Please try again.")
                backtomenu()
        backtomenu()
        

def stockHistogram():
    def bars():
        ALPACA_API_KEY ="PK4QWK27RIXPO7TSPFZE"
        ALPACA_SECRET_KEY = "rYdkMPN7maso16TpwkvAnebOMl7dlnUU7hEzp1BT"

        alpaca = api.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY)

    #Setting parameters before calling method
        symbol = input("Input a symbol: ")
        timeframe = input("Enter a time frame to present the data in Ex:'1Day', '1Min', etc: ")
        #Test this on Tuesday
        start = input("Input a start date (YEAR-MONTH-DAY)/0000-00-00: ")
        end = input("Input the end date (YEAR-MONTH-DAY)/0000-00-00: ")
    #Retrieves daily bars in a dataframe and prints the first 5 rows
        trade_bars= alpaca.get_bars(symbol, timeframe, start, end).df
        print(trade_bars.head())
        candlestick_fig = go.Figure(data=[go.Candlestick(x=trade_bars.index,
                    open=trade_bars['open'],
                    high=trade_bars['high'],
                    low=trade_bars['low'],
                    close=trade_bars['close'])])
        candlestick_fig.update_layout(
            title="Candlestick chart for "+symbol +' ('+timeframe+')',
            xaxis_title="Date",
            yaxis_title="Price ($USD)")
        candlestick_fig.show()
        exit = input("In order to go back to menu, type 'Back'")
        if exit == "Back":
            menu()
    def trades():
        ALPACA_API_KEY ="PK4QWK27RIXPO7TSPFZE"
        ALPACA_SECRET_KEY = "rYdkMPN7maso16TpwkvAnebOMl7dlnUU7hEzp1BT"
        alpaca = api.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY)

        symbol = input("Please input a symbol: ")
        limit = 10000
    #Retrieve trades for STOCK in a dataframe and printing the first 5 rows
        trades = alpaca.get_trades(symbol, limit=limit).df
        print(trades.head())

    #displays a histogram that aggregates our data on exchange
        exchange_histogram = px.histogram(trades, x="exchange")
        exchange_histogram.update_layout(
        title="Frequency of exchanges for "+symbol,
        yaxis_title="Number of trades",
        xaxis_title="Exchange")
        exchange_histogram.show()
        exit = input("In order to go back to menu, type 'Back'")
        if exit == "Back":
            menu()

    def choice():
        question = input("Would you like to see data represented in a bar? (Bar)\nOr Would you like the see the trade histogram? (Histogram)\nType Here: ")
        if question == "Bar":
            bars()
        elif question == "Histogram":
            trades()

        if question != "Bar" or "Histogram":
            print("Invalid Input")
            choice()
#Present the user with a choice to view whichever data they would like
    print("WELCOME TO STOCK HISTORY AND DATA")
    choice()
#Reference = https://alpaca.markets/learn/understanding-alpacas-market-data-api-with-pandas-and-plotly/


def menu():
    print("1. Place An Order") #Make a market or limit order as well as cancel all positions
    print("2. Cancel Orders") #Cancel all existing orders here
    print("3. Live Trade Data") #Stream realtime trading data of a preferred stock
    print("4. Current Positions") #Get info about your current positions
    print("5. Historical Trade Data") #Get access to Historical Trade Data
    print("6. Exit") #If user presses this choice, present them with the start function
    choice = input("Enter your choice (1-6): ") #Type a number 1 - 6
    if choice == '1':
        order()
    elif choice == '2':
        cancelOrders()
    elif choice == '3':
        streamData()
    elif choice == '4':
        getPositions()
    elif choice == '5':
        stockHistogram()
    elif choice == '6':
        print("Exiting...")
        time.sleep(1)
        print("GoodBye!")
        quit()
    elif choice != '1' or '2' or '3' or '4' or '5' or '6':
        print("Invalid Input")
        time.sleep(1)
        menu()
        

def start():
    userName = input("Please enter your name: ")
    print("Welcome " + userName)
    time.sleep(1)
    menu()

start()