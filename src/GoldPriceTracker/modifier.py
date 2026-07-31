import json
from datetime import datetime
from zoneinfo import ZoneInfo

today = str(datetime.now(ZoneInfo("Asia/Kolkata")))

data = ""

def check_and_modify(todays_price):
    try:
        with open("price_tracker.json", "r") as file:
            data = json.load(file)
            max_price = data["max_price"]
            percent_change = ((max_price-todays_price)/max_price) * 100
            if (todays_price > max_price):
                max_price = todays_price
                return -1
            elif percent_change >= 5.0:
                return 1

        with open("price_tracker.json", "w") as file:
            data["max_price"] = max_price
            data["history"].append({today: todays_price, "change in percent": percent_change
                                    })
            json.dump(data, file, indent=4)
            

    except:
        with open("price_tracker.json", "w") as file:
            data = {}
            history = []
            history.append({today : todays_price})
            data = {
                "max_price": todays_price,
                "history": history
            }
            json.dump(data, file, indent=4)
            return 0


