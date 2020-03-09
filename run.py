from app.invoicestats import InvoiceStats


def main():
    print("\n"
          "  1. Add Invoices (multiple comma separated)\n"
          "  2. Add Invoice (single)\n"
          "  3. Clear\n"
          "  4. Get Median\n"
          "  5. Get Mean\n"
          "  6. View all Invoices\n"
          "  7. Exit")

    while True:
        try:
            option = input("\nSelect an option: ")
            option = int(option)
            invoice_data = InvoiceStats()

            if option == 1:
                value = input("\nInput a set of invoice amounts: ")
                invoice_data.add_invoices(value)
            elif option == 2:
                value = input("\nAdd a invoice amount: ")
                invoice_data.add_invoice(value)
            elif option == 3:
                invoice_data.clear_invoices()
            elif option == 4:
                output = invoice_data.get_medium()
                print(f"The median is: {output:.2f}")
            elif option == 5:
                output = invoice_data.get_mean()
                print(f"The mean is: {output:.2f}")
            elif option == 6:
                invoice_data.view_all()
            elif option == 7:
                break
            else:
                print("Not a valid option, please enter a number between 1 and 7")
                
                # Using mutliple elifs for switch-case style logic should be avoided. You can use a dictionary instead. Something like this. 
                # User inputs and printing could be encapsulated to another function.
            
                        invoice_options = {1: invoice_data.add_invoices(),
                               2: invoice_data.add_invoice(),
                               3: invoice_data.clear_invoices(),
                               4: invoice_data.get_medium(),
                               5: invoice_data.get_mean(),
                               6: invoice_data.view_all(),
                               7: exit()}
            
            output = invoice_options.get(option, raise_non_valid_option())

        except Exception as error:
            print(error)


if __name__ == '__main__':
    main()
