import math


class InvoiceStats:

    def __init__(self):
        self.invoices: list = []

    @property
    def __len__(self) -> int:
        return len(self.invoices)

    def add_invoices(self, invoices: str) -> list:
        """ method to add multiple invoice amounts and print to screen """
        invoices = invoices.split(",")
        invoices = [self.check_format(invoice) for invoice in invoices]
        invoices = [self.check_value(invoice) for invoice in invoices]
        self.invoices = self.invoices + invoices

        return self.invoices

    def add_invoice(self, invoice: str) -> list:
        """ method to add single invoice amount and print to screen """
        invoice = self.check_format(invoice)
        invoice = self.check_value(invoice)
        self.invoices.append(invoice)

        return self.invoices

    def clear_invoices(self, *args):
        """ clear all stored invoices """
        self.invoices[:] = []

    def get_medium(self, *args) -> str:
        """ prints the median of all stored invoice amounts """
        self.invoices.sort()
        if self.__len__ % 2 == 0:
            median1 = self.invoices[self.__len__ // 2]
            median2 = self.invoices[self.__len__ // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = self.invoices[self.__len__ // 2]
        rounded_median = self.round_down(median, 2)

        return f"The median is: {rounded_median:.2f}"

    def get_mean(self, *args) -> str:
        """ gets the mean of all stores invoice amounts """
        sum_values = sum(self.invoices)
        mean = sum_values / self.__len__
        rounded_mean = self.round_down(mean, 2)

        return f"The mean is: {rounded_mean:.2f}"

    def view_all(self, *args):
        """ prints all stored invoice amounts """
        print("\nCurrent saved invoice amounts:")
        [print(f"  - {invoice:.2f} USD") for invoice in self.invoices]

    @staticmethod
    def check_format(number: str) -> float:
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
    def check_value(number: float) -> float:
        """ validates user input """
        if 200000 < number:
            raise ValueError(
                f'{number} is not a valid input. Invoice amount must be less than 200,000 USD')
        if number < 0:
            raise ValueError(
                f'{number} is not a valid input. Invoice amount must be more than 0 USD')
        return number

    @staticmethod
    def round_down(n: float, decimals=0) -> float:
        """ method for rounding down to a given number of decimal places """
        multiplier = 10 ** decimals
        return math.floor(n * multiplier) / multiplier


