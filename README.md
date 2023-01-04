# Simulator for credit card transactions. It maintains the balance owed on the credit card by keeping track of new purchases, the interest accrued, and bill payments that can sometimes be partial. In addition, a flagging algorithm makes sure that the card is deactivated (i.e., no further purchases can be made) if fraud is suspected.

# Initially, the amount owed is 0.
# The amount owed is divided into two parts: the amount that is accruing interest, and the amount that is not accruing interest. The only money that is not accruing interest during the month is the money spent on purchases during that same month. Any other money owed is accruing interest.
# An interest of 5% is added to the amount owed in the last second of each month. Assume that no purchases are made between the time the interest is added to the amount owed and the time that the month changes.
# When the credit card bill is paid, and the amount owed is not paid in full, the payment first goes to pay the amount that is accruing interest, and only then to pay the amount that is not accruing interest.
# If the card is used for purchases in three different countries in a row, the card is deactivated. The third purchase does not work, and no further purchases can be made.
