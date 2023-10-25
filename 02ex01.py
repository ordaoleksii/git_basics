#!/usr/bin/env python3
"""Calculate deposit percent yield based on time period.
Imagine your friend wants to put money on a deposit.He has got many offers from different banks:
- First bank declares +A% each day;- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...
Your friend gets a terrible headache calculating all this stuff,and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.
Let's implement this.
A simplified task:
Given the SUM amount of money, and PERCENT yield promised in aFIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.
Math formula:p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))"""

# TODO: add lines to calculate yields for some common periods#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield#       as well
# TODO: (extra) Output only percents if the initial SUM is#       not known at the moment the script is run

USAGE = """USAGE: {script} initial_sum percent fixed_period set_period
\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()
def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)
    return initial_sum * growth
def main():
    """Gets called when run as a script."""
    initial_sum = float(input("initial_sum: "))
    percent = float(input("percent: "))
    fixed_period = float(input("fixed_period: "))
    set_period = float(input("set_period: "))
    res = round(deposit(initial_sum, percent, fixed_period, set_period), 2)
    print(f"Yield: {res}")
    # Calculate yields for common periods
    common_periods = [1, 12, 60, 120]  # 1 month, 1 year, 5 years, 10 years
    for period in common_periods:
        yield_value = round(deposit(initial_sum, percent, fixed_period, period), 2)
        print(f"Yield for {period} periods: {yield_value}")
if __name__ == '__main__':
    main()
