import json
from datetime import datetime
from zoneinfo import ZoneInfo


def check_and_modify(todays_price):
    today_str =  datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")
    status_code = 0
    try:
        with open("./price_tracker.json", "r") as file:
            data = json.load(file)
        max_price = data["max_price"]
        percent_change = ((max_price-todays_price)/max_price) * 100
        if (todays_price > max_price):
            max_price = todays_price
            status_code = -1
        elif percent_change >= 5.0:
            status_code = 1

        data["max_price"] = max_price
        data["history"].append({
            "timestamp": today_str,
            "price": todays_price,
            "percent_change": round(percent_change, 2)
        })


        with open("./price_tracker.json", "w") as file:
            json.dump(data, file, indent=4)

        return status_code
            

    except:
        with open("./price_tracker.json", "w") as file:
            data = {
                "max_price": todays_price,
                "history": [
                    {
                        "timestamp": today_str,
                        "price": todays_price,
                        "percent_change": 0.0
                    }
                ]
            }
            with open("./price_tracker.json","w") as file:
                json.dump(data, file, indent=4)
            return 0


