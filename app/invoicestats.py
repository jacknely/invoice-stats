import math


class InvoiceStats:

    def __init__(self):
        self.invoices = []
    
    def __len__(self):
        return len(self.invoices)

    def invoice_options(self, option):
        invoice_options = {
            1: self.add_invoices(),
            2: self.add_invoice(),
            3: self.clear_invoices(),
            4: self.get_medium(),
            5: self.get_mean(),
            6: self.view_all(),
            7: exit()
        }

        return invoice_options.get(option, self.raise_non_valid_option())

    def add_invoices(self):
        """ method to add multiple invoice amounts and print to screen """
        invoices = self.get_user_input()
        invoices = invoices.split(",")
        invoices = [self.check_format(invoice) for invoice in invoices]
        invoices = [self.check_value(invoice) for invoice in invoices]
        self.invoices = self.invoices + invoices
        print(self.invoices)

        return True

    def add_invoice(self):
        """ method to add single invoice amount and print to screen """
        value = self.get_user_input()
        value = self.check_format(value)
        value = self.check_value(value)
        self.invoices = self.invoices + value
        print(self.invoices)

        return True

    def clear_invoices(self):
        """ clear all stored invoices """
        self.invoices[:] = []

        return True

    def get_medium(self):
        """ prints the median of all stored invoice amounts """
        self.invoices.sort()
        if self.__len__ % 2 == 0:
            median1 = self.invoices[self.__len__ // 2]
            median2 = self.invoices[self.__len__ // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = self.invoices[self.__len__ // 2]
        rounded_median = self.round_down(median, 2)

        return rounded_median

    def get_mean(self):
        """ gets the mean of all stores invoice amounts """
        sum_values = sum(self.invoices)
        mean = sum_values / self.__len__
        rounded_mean = self.round_down(mean, 2)

        return rounded_mean

    def view_all(self):
        """ prints all stored invoice amounts """
        print("\nCurrent saved invoice amounts:")
        [print(f"  - {invoice:.2f}") for invoice in self.invoices]

    @staticmethod
    def get_user_input():
        return input("enter a value:")

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

    @staticmethod
    def raise_non_valid_option():
        raise ValueError(
            'Please select a option between 1 and 7.')
