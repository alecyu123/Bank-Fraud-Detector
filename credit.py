# You should modify initialize()
def initialize():
    '''Assign initial values to variables needed for credit to work and global it'''

    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    global disabled, MONTHLY_INTEREST_RATE

    disabled = False

    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0

    last_update_day, last_update_month = 1, 1

    last_country = None
    last_country2 = None

    MONTHLY_INTEREST_RATE = 0.05

def date_same_or_later(day1, month1, day2, month2):
    '''Returns True iff day and month are ahead of the last'''

    if month1 > month2:
        return True
    elif month1 == month2:
        if day1 >= day2:
            return True
        else:
            return False
    else:
        return False

def all_three_different(c1, c2, c3):
    '''Returns True iff each parameter is unique from the others and one of them is not None'''

    if c1 != c2 and c2 != c3 and c3 != c1 and c2 != None:
        return True
    else:
        return False

def purchase(amount, day, month, country):
    '''Assigns parameter amount being paid to variable cur_balance_owing_recent and updates recent dates'''

    global disabled, last_country, last_country2, last_update_day, last_update_month, cur_balance_owing_recent
    if disabled == True:
        return "error"
    elif all_three_different(last_country, last_country2, country):
        disabled = True
        return "error"
    else:
        if date_same_or_later(day, month, last_update_day, last_update_month):
            update_balance(day, month)
            cur_balance_owing_recent += amount
            last_update_day = day
            last_country2 = last_country
            last_country = country
        else:
            return "error"


def amount_owed(day, month):
    '''Updates and returns cur_balance_owing_intst according to outstanding payments with interest and cur_balance_owing_recent'''

    if date_same_or_later(day, month, last_update_day, last_update_month):
        update_balance(day, month)
        return cur_balance_owing_intst + cur_balance_owing_recent
    else:
        return "error"

def pay_bill(amount, day, month):
    '''Pays cur_balance_owing_intst first and cur_balance_owing_recent only
    after cur_balance_owing_intst is fully paid ; does not account for payments
    larger than amount owed'''

    global cur_balance_owing_intst, cur_balance_owing_recent, last_fully_paid_month
    if date_same_or_later(day, month, last_update_day, last_update_month):
        update_balance(day, month)
        if amount <= cur_balance_owing_intst:
            cur_balance_owing_intst -= amount

        else:
            cur_balance_owing_recent -= (amount - cur_balance_owing_intst)
            cur_balance_owing_intst = 0


    else:
        return "error"


def update_balance(day, month):
    '''Updates the cur_balance_owing_intst and cur_balance_owing_recent according to how many months it has been since last update'''

    global last_update_month, last_update_day, last_fully_paid_month, cur_balance_owing_intst, cur_balance_owing_recent, MONTHLY_INTEREST_RATE
    m = month - last_update_month
    if m > 0:
        cur_balance_owing_intst *= 1 + MONTHLY_INTEREST_RATE
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_recent = 0
        if m > 1:
            cur_balance_owing_intst *= (1 + MONTHLY_INTEREST_RATE) ** (m - 1)

    last_update_month = month
    last_update_day = day




# Initialize all global variables outside the main block.
initialize()

if __name__ == '__main__':
    # Describe your testing strategy and implement it below.
    # What you see here is just the simulation from the handout, which
    # doesn't work yet.
    initialize()
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      # 80.0
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      # 30.0     (=80-50)
    print("Now owing:", amount_owed(6, 3))      # 31.5     (=30*1.05)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 71.5     (=31.5+40)
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))      # 41.5     (=71.5-30)
    print("Now owing:", amount_owed(1, 5))      # 43.65375 (=1.5*1.05*1.05+40*1.05)
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      # 83.65375
    print(purchase(50, 3, 5, "United States"))  # error    (3 diff. countries in
                                                #          a row)

    print("Now owing:", amount_owed(3, 5))      # 83.65375 (no change, purchase
                                                #           declined)
    print(purchase(150, 3, 5, "Canada"))        # error    (card disabled)
    print("Now owing:", amount_owed(1, 6))      # 85.8364375
                                                # (43.65375*1.05+40)
    initialize()
    purchase(1, 1, 1, "Canada")
    print("Now owing:", amount_owed(1, 1))		# Testing for all_three_different
                                                # (c1, c2, c3) to not return

    purchase(1, 1, 1, "France")					# True when purchasing in same
                                                # countries twice
    print("Now owing:", amount_owed(1, 1))
    purchase(1, 1, 1, "Canada")
    print("Now owing:", amount_owed(1, 1))
    purchase(1, 1, 1, "Canada")
    print("Now owing:", amount_owed(1, 1))		# Purchase Accepted
    purchase(1, 1, 1, "US")
    print("Now owing:", amount_owed(1, 1))		# Purchase Accepted
    purchase(1, 1, 1, "Canada")
    print("Now owing:", amount_owed(1, 1))		# Purchase Accepted
    purchase(1, 1, 2, "Germany")
    print("Now owing:", amount_owed(1, 2))		# Purchase Declined because
                                                # different countries 3 times
                                                # in a row

    print("Now owing:", amount_owed(20, 1))		# Testing for date_same_or_later
                                                # to return "error" for non -
                                                # chronological timeline

    print("Now owing:", amount_owed(6, 7))		# Testing for interest to work

    initialize()									# Testing to see if pay_bill
                                                # will first deduct from
                                                # cur_balance_owing_intst
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      # 80.0
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      # 30.0     (=80-50)
    print("Now owing:", amount_owed(6, 3))      # 31.5     (=30*1.05)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 71.5     (=31.5+40)
    pay_bill(40, 7, 3)							# 31.5	   (=0+31.5)
    print("Now owing:", amount_owed(8, 3))
    print("Now owing:", amount_owed(6, 4))		# 31.5	   (=31.5+0), no interest
                                                # yet since interest
                                                # balance payed first

    print("Now owing:", amount_owed(6, 5))		# 33.075   (= 31.5*1.05+0)


