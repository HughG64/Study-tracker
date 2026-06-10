from datetime import date, timedelta

def calculate_streak(dates: list) -> int:
    count=1
    sorted_dates = sorted(dates)
    for i, value in enumerate(sorted_dates):
        if i == 0:
            continue

        if sorted_dates[i] - sorted_dates[i-1] == timedelta(days=1):
            count += 1
        else:
            count = 1

    return count





