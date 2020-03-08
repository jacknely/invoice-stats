import math


class InvoiceStats:
    invoices = []

    @classmethod
    def add_invoices(cls, invoices: str):
        """ method to add multiple invoice amounts and print to screen """
        invoices = invoices.split(",")
        invoices = [cls.check_format(invoice) for invoice in invoices]
        invoices = [cls.check_value(invoice) for invoice in invoices]
        cls.invoices = cls.invoices + invoices
        print(cls.invoices)

        return True

    @classmethod
    def add_invoice(cls, value: str):
        """ method to add single invoice amount and print to screen """
        value = cls.check_format(value)
        value = cls.check_value(value)
        cls.invoices.append(value)
        print(cls.invoices)

        return True

    @classmethod
    def clear_invoices(cls):
        """ clear all stored invoices """
        cls.invoices[:] = []

        return True

    @classmethod
    def get_medium(cls):
        """ prints the median of all stored invoice amounts """
        count = len(cls.invoices)
        cls.invoices.sort()
        if count % 2 == 0:
            median1 = cls.invoices[count // 2]
            median2 = cls.invoices[count // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = cls.invoices[count // 2]
        rounded_median = cls.round_down(median, 2)

        return rounded_median

    @classmethod
    def get_mean(cls):
        """ gets the mean of all stores invoice amounts """
        count = len(cls.invoices)
        sum_values = sum(cls.invoices)
        mean = sum_values / count
        rounded_mean = cls.round_down(mean, 2)

        return rounded_mean

    @classmethod
    def view_all(cls):
        """ prints all stored invoice amounts """
        print("\nCurrent saved invoice amounts:")
        [print(f"  - {invoice:.2f}") for invoice in cls.invoices]

    @staticmethod
    def check_format(number: str):
        """ validates user input """
        split_number = str(number).split(".")
        if len(split_number) < 2:  # check for decimal
            raise ValueError(
                f'{number} is not a valid input. Input should be to two decimal places.')
        elif len(split_number[1]) != 2:  # check for 2 significant figures
            raise ValueError(
                f'{number} is not a valid input. Input should be to two decimal places.')
        else:
            return float(number)

    @staticmethod
    def check_value(number: float):
        """ validates user input """
        if 200000 < number:
            raise ValueError(
                f'{number} is not a valid input. Invoice amount must be between 0 and 200,000 USD')
        if number < 0:
            raise ValueError(
                f'{number} is not a valid input. Invoice amount must be between 0 and 200,000 USD')
        return number

    @staticmethod
    def round_down(n, decimals=0):
        """ method for rounding down to a given number of decimal places """
        multiplier = 10 ** decimals
        return math.floor(n * multiplier) / multiplier
