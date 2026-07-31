from fetcher import fetch
from modifier import check_and_modify
from notifier import notify

def main():
    todays_price = fetch()
    todays_status = check_and_modify(todays_price)
    notify(todays_status)
    from fetcher import fetch
    from modifier import check_and_modify
    from notifier import notify


    todays_price = fetch()
    todays_status = check_and_modify(todays_price)
    notify(todays_status)


if __name__ == "__main__":
    main()
