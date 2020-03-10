# Invoice Stats
Invoices are agreements to transfer money between companies. This is a python 
class to aggregate and gather basic stats on the invoices processed.

## Requirements
- Python 3.8
- Pytest
- Pytest-Mocker

Install from requirements.txt

## Usage
Run program in command line at root folder of application:
````
python run.py
````

The following options will be displayed:

````
  1. Add Invoices (multiple comma separated)
  2. Add Invoice (single)
  3. Clear
  4. Get Median
  5. Get Mean
  6. View all Invoices
  7. Exit
````
Input a number between 1 and 7 then press enter.

### 1. Add Invoices
To add multiple invoices enter data as follows:
```
34.09, 1840.02, 90.09
```
Each entry must be in Dollar.Cent format ($$.CC) and separated by a comma.

### 2. Add Invoice
Add a single invoice in the same format as above.

### 3. Clears
Clears all invoices stored.

### 4. Get Medium
Returns the medium value for invoices stored in instance of InvoiceStats().

### 5. Get Mean
Returns the mean value for invoices stored in instance of InvoiceStats().

### 6. View all Invoices
Outputs all stored invoices within instance of InvoiceStats().

### 7. Exit
Leaves the program


## Review
- Happy that I didnt end up with a large while loop for all main menu options in 'run.py'
- Good amount of unit and integration test coverage

## Further Improvements
- More friendly way of passing 'values' to functions from 'run.py'
- As per above so that *args can be removed from functions that don't require a value
- Add regression testing
- Improve input validation and exceptions
