"""
@Author: Harry Vu
@Description: Calculating cost of electricity
@Last modified: Sep 16, 2021
"""

while True:
    totalUsageDiscount = 0.96     # 4% disc
    onPeakDiscount = 0.95         # 5% disc
    seniorDiscount = 0.89         # 11% disc
    tax = 1.13                    # 13% tax

    offRate = 0.085     # $0.085/kWh
    onRate = 0.176      # $0.176/kWh
    midRate = 0.119     # $0.119/kWh

    tudCheck = False    # Boolean set to true when TUD is applied

    offKwh = float(input("Enter kwh during Off Peak period: "))
    if offKwh == 0.0:     # Program exit if Off Peak period usage = 0
        exit(0)
    onKwh = float(input("Enter kwh during On Peak period: "))
    midKwh = float(input("Enter kwh during Mid Peak period: "))
    seniorYN = input("Is owner senior?: ")
    seniorYN = seniorYN.lower()     # Convert input seniorYN to lowercase

    elecCostGross = offKwh * offRate + onKwh * onRate + midKwh * midRate

    if offKwh + onKwh + midKwh < 400 and seniorYN == "n":       # Under 400 TU, not senior
        elecCostGross *= totalUsageDiscount
        tudCheck = True     # True after applied TUD
    elif offKwh + onKwh + midKwh < 400 and seniorYN == "y":     # Under 400 TU, senior
        elecCostGross *= totalUsageDiscount * seniorDiscount
        tudCheck = True
    elif seniorYN == "n":                                       # Original
        elecCostGross = elecCostGross
    elif seniorYN == "y":                                       # Discount for senior
        elecCostGross = elecCostGross * seniorDiscount

    if onKwh < 150 and tudCheck is False and seniorYN == "n":       # Over 400 TU, under 150 OPU, not senior
        elecCostGross = (offKwh * offRate + onKwh * onRate * onPeakDiscount + midKwh * midRate)
    elif onKwh < 150 and tudCheck is False and seniorYN == "y":     # Over 400 TU, under 150 OPU, senior
        elecCostGross = (offKwh * offRate + onKwh * onRate * onPeakDiscount + midKwh * midRate) * seniorDiscount

    print("Electricity cost: $" + "{:.2f}".format(elecCostGross * tax))
    print()
