options = ["indices","crypto","currency","commodities","stock"]
asset_class = input(f"What asset class do you want to calculate?{options}: ").lower()
execution = input("are we buying or selling?(type in b or s): ")
if (input("is this a JPY pair (Y/N): ")) == "y":  is_jpy = True
risk = int(input("How much dollars you willing to risk?:$ "))
entry_point = float(input("Where do you plan to enter: "))
stop_loss = float(input("Where is your plan for exit "))
take_profit = float(input("What's your take profit price"))


def calc_pips(asset_class,execution,risk,entry_point,stop_loss,take_profit):
    sl_pips = abs(entry_point - stop_loss)
    if asset_class == "currency" and not "JPY":
        sl_pips = sl_pips * 1000
    else:
        sl_pips = sl_pips * 100
    lotsize = round(risk/sl_pips,2)
    profits = round((entry_point - take_profit) * lotsize,2)
    loss = round(sl_pips * lotsize,2)
    if execution == "s":
        profits = abs(profits)
    return(f"your profit will be {profits}, your loss will be {loss} and you should use a lotsize of {lotsize}")


print(calc_pips("indices"))




