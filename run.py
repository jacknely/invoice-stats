from app.invoicestats import InvoiceStats


def main():
    print(
        "\n"
        "  1. Add Invoices (multiple comma separated)\n"
        "  2. Add Invoice (single)\n"
        "  3. Clear\n"
        "  4. Get Median\n"
        "  5. Get Mean\n"
        "  6. View all Invoices\n"
        "  7. Exit"
    )

    invoice_data = InvoiceStats()

    invoice_options = {
        1: invoice_data.add_invoices,
        2: invoice_data.add_invoice,
        3: invoice_data.clear_invoices,
        4: invoice_data.get_medium,
        5: invoice_data.get_mean,
        6: invoice_data.view_all,
    }
    while (option := int(input("\nSelect an option: "))) != 7:
        try:
            if option == 1:
                value = input("\nInput a set of invoice amounts: ")
            elif option == 2:
                value = input("\nAdd a invoice amount: ")
            else:
                value = None
            if output := invoice_options.get(option)(value):
                print(output)
        except TypeError:
            print("Ensure you have entered a number between 1 and 7")


if __name__ == "__main__":
    main()
