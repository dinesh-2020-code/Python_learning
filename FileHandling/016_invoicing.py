'''
    Random Access
        -> Random access is the term used for accessing data from any part of a file.
        -> Random access in files means data can be read from (and write to) any location in the file
        The file pointer can be changed to any location in the file, for reading and writing.
    
    File Pointer: 
        -> The file pointer keeps track of where you are in the file.
        -> When you write data to the file, data is written at the current position of the file pointer.
        The file pointer then moves forward, as data is written.
        -> When reading from a text file, reading takes place from the file pointer's position. The file
        pointer moves forward as data is read.

    Random access in text files:
        -> Random access, in Python, is very limited with text files.
        -> It's possible to position the file pointer relative to the start of the file, or position it
        at the end of the file, but those are the only options available.
        -> For true random access to your text data, you'd have to either open the file in binary mode,
        or read the entire contents of the file into a string.

    File pointers in text files:
        -> With text files we only have 2 options when seeking:
            (i) we can seek to the start of the file, 
            (ii) we can seek to the end of the file. You can't seek backwards from the end
    
    seek and tell and Unicode
        -> With text files, you can seek to the start or end of the file.
        You can also seek to a position within the file, but the position must be a position that
        you obtained by calling `tell`. You can't just provide any integer value, and expect to end
        up anywhere useful.
        -> There is a good reason for that, and it's all to do with character encodings. 
        As you now know, characters can be encoded using 1, 2, or 4 bytes (in UTF-8). Other encodings
        also use multiple bytes for various chars.
        -> If you attempt to seek to a position that you didn't obtain using `tell`, you could end up in
        middle of a multi-byte character.
        Reading from that position is going to cause problems. The char will be invalid, and strange things
        will happen. 
'''


import datetime
from os import SEEK_SET
from typing import TextIO


def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    year, number = invoice_number.split('-')
    return int(year), int(number)


def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    invoice_year, number = parse_invoice_number(invoice_number)
    year = get_year()
    if year == invoice_year:
        number += 1
    else:
        invoice_year = year
        number = 1
    new_invoice_number = f'{invoice_year}-{number:04d}'
    return new_invoice_number


def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float,
                   last_line_ptr: int = 0) -> int:
    """Create a new invoice number, and write it to a file on disk.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    :param last_line_ptr: The position of the start of the last line in the
    file. This will be obtained by the previous call to `record_invoice`.
    :return: The position of the start of the last line in teh file. This can
    be used in subsequent call to `record_invoice`.
    """
    invoice_file.seek(last_line_ptr, SEEK_SET)
    last_row = ''
    for line in invoice_file:
        print("*", end='')  # TODO delete after testing
        last_row = line
    if last_row:
        invoice_number, _, _ = last_row.split('\t')
        new_invoice_number = next_invoice_number(invoice_number)
    else:
        # if the file is empty, we'll start numbering from 1.
        year = get_year()
        new_invoice_number = f'{year}-{1:04d}'

    last_line_ptr = invoice_file.tell()
    print(f'{new_invoice_number}\t{company}\t{amount}', file=invoice_file)
    return last_line_ptr


data_file = 'invoices.csv'

with open(data_file, 'r+') as invoices:
    last_line = record_invoice(invoices, 'ACME Roadrunner', 18.40)
    last_line = record_invoice(invoices, 'Squirrel Storage', 320.55, last_line)
# Test code:
# current_year = get_year()
# test_data = [
#     ('2019-0005', (2019, 5), f'{current_year}-0001'),
#     (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
#     (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
#     (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
# ]

# for test_string, result, next_number in test_data:
#     parts = parse_invoice_number(test_string)
#     if parts == result:
#         print(f'{test_string} parsed successfully')
#     else:
#         print(f'{test_string} failed to parse. Expected {result} got {parts}')

#     new_number = next_invoice_number(test_string)
#     if next_number == new_number:
#         print(f'New number {new_number} generated correctly for {test_string}')
#     else:
#         print(f'New number {new_number} is not correct for {test_string}')

#     print('-' * 80)

