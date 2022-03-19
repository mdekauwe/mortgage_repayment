import matplotlib.pyplot as plt
import numpy as np
import sys

def get_repayments(principal, n_months, interest_rate):

    m = principal * \
        interest_rate * (1. + interest_rate) ** n_months / \
        ((1 + interest_rate) ** n_months - 1.)

    return (m)


principal = float(sys.argv[1])
n_years = 26
n_months = n_years * 12
#interest_rate = 2.09 / 100. / 12.
#repayments_per_month = get_repayments(principal, n_months, interest_rate)
#print(principal, n_months, interest_rate)
#print("%.2f" % repayments_per_month)

interest_rate_st = 2.0
interest_rate_en = 7.0
interest_rates = np.linspace(interest_rate_st, interest_rate_en)
repayments_per_month = np.zeros(len( interest_rates ) )

for i in range(len(interest_rates)):
    interest_rate = interest_rates[i] / 100 / 12.
    repayments_per_month[i] = get_repayments(principal, n_months, interest_rate)

plt.plot(interest_rates, repayments_per_month, ls="--", marker="o")
plt.ylabel("Monthly repayment (\xA3)")
plt.xlabel("Interest rate (%)")
plt.show()
