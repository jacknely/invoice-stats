import pytest
import random

from app.invoicestats import InvoiceStats


class TestInvoiceStats:

    def setup(self):
        """ Setup a instance of class InvoiceStats for testing """
        self.test_invoice_data = InvoiceStats()

    def teardown_method(self):
        self.test_invoice_data.invoices[:] = []

    test_invoices = [('45.67', [45.67]),
                     ('56.24', [56.24]),
                     (56.32, [56.32])]

    @pytest.mark.parametrize('invoice, invoice_result', test_invoices)
    def test_add_invoice(self, invoice, invoice_result):
        """ test for adding single invoice to system """
        self.test_invoice_data.add_invoice(invoice)
        assert self.test_invoice_data.invoices == invoice_result

    def test_add_invoices(self):
        """ test for 100,000 random invoice inputs """
        test_large_invoice = []
        for i in range(0, 100000):
            number = random.uniform(0, 10000)
            number = round(number, 2)
            split_number = str(number).split(".")  # need to remove all XX.00 values as they round to XX.0
            if len(split_number[1]) < 2:
                number = number + 0.12
            number = round(number, 2)  # had to round again as addition added some tiny error
            test_large_invoice.append(number)
        test_large_invoice_str = ','.join(map(str, test_large_invoice))
        self.test_invoice_data.add_invoices(test_large_invoice_str)
        assert self.test_invoice_data.invoices == test_large_invoice

    @pytest.mark.parametrize('invoice, invoice_result', test_invoices)
    def test_clear_invoices(self, invoice, invoice_result):
        """ test for clearing stored invoices """
        self.test_invoice_data.add_invoice(invoice)
        self.test_invoice_data.clear_invoices()
        assert self.test_invoice_data.invoices == []

    test_mean = [('2.00, 3.00, 4.00', 3.00),
                ('4.00, 1.00', 2.50),
                ('5.00, 1.00, 1.00, 100.00', 26.75)]

    @pytest.mark.parametrize('invoice, mean', test_mean)
    def test_get_mean(self, invoice, mean):
        """ test for calculating medium """
        self.test_invoice_data.add_invoices(invoice)
        assert self.test_invoice_data.get_mean() == mean

    test_medium = [('2.00, 3.00, 4.00', 3.00),
                   ('4.00, 5.00', 4.5),
                   ('5.00, 6.00', 5.5)]

    @pytest.mark.parametrize('invoice, medium', test_medium)
    def test_get_medium(self, invoice, medium):
        """ test for calculating medium """
        self.test_invoice_data.add_invoices(invoice)
        assert self.test_invoice_data.get_medium() == medium


class TestInvoiceStatsExceptions:

    def setup(self):
        """ Setup a instance of class InvoiceStats for testing """
        self.test_invoice_data = InvoiceStats()

    def teardown_method(self):
        self.test_invoice_data.invoices[:] = []

    def test_value_1(self):
        """ test for adding single invoice to system """
        with pytest.raises(ValueError) as error:
            self.test_invoice_data.add_invoice(1)
        assert '1 is not a valid input. Input should' \
               ' be to two decimal places.' == str(error.value)

    def test_values_2(self):
        """ test for adding single invoice to system """
        with pytest.raises(ValueError) as error:
            self.test_invoice_data.add_invoice('bad_string')
        assert 'bad_string is not a valid input. Input should' \
               ' be to two decimal places.' == str(error.value)

    def test_values_3(self):
        """ test for adding single invoice to system """
        with pytest.raises(ValueError) as error:
            self.test_invoice_data.add_invoice(30000000.01)
        assert '30000000.01 is not a valid input. Invoice ' \
               'amount must be between 0 and 200,000 USD' == str(error.value)

    def test_values_4(self):
        """ test for adding single invoice to system """
        with pytest.raises(ValueError) as error:
            self.test_invoice_data.add_invoice(-34.01)
        assert '-34.01 is not a valid input. Invoice ' \
               'amount must be between 0 and 200,000 USD' == str(error.value)


if __name__ == '__main__':
    pytest.main()
