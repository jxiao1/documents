Python Excel
============

Overview
--------

http://www.python-excel.org/

**openpyxl**
The recommended package for reading and writing Excel 2010 files (ie: .xlsx)

https://openpyxl.readthedocs.io/en/default/

**xlwd**
This package is for reading data and formatting information from older Excel files (ie: .xls)

http://xlrd.readthedocs.io/en/latest/


**xlwt**
This package is for writing data and formatting information to older Excel files (ie: .xls)

http://xlwt.readthedocs.io/en/latest/


openpyxl
--------

Install: ``sudo pip install openpyxl``

Workboot in Memory
~~~~~~~~~~~~~~~~~~

Create new workbook::

    from openpyxl import Workbook
    wb = Workbook()

    # Write-only mode
    wb = Workbook(write_only=True)

Get the worksheet::

    ws = wb.active  # Get the active sheet (The first by default)
    ws = wb['Mysheet']  # Get the sheet by name

Change the worksheet name::

    ws.title = "New Title"  #

Get all the sheet names::

    print(wb.sheetnames)  # or

    for sheet in wb:
        print(sheet.title)

Get the column letter::

    from openpyxl.utils import get_column_letter
    get_column_letter(1)  # 'A' for column 1

Create new worksheet::

    ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
    ws2 = wb.create_sheet("Mysheet", 0) # insert at first position

Copy sheet within a single workbook::

    source = wb.active
    target = wb.copy_worksheet(source)

The background color of the tab holding this title is white by default.
You can change this via the sheet_properties.tabColor property::

    ws.sheet_properties.tabColor = "1072BA"  # RRGGBB

Access one cell::

    c = ws['A1']
    ws['A1'] = 'Name'
    d = ws.cell(row=4, column=2)  # return cell, d.value contains the value
    d = ws.cell(row=4, column=2, value=10)   # change/assign to new value

    cell_range = ws['A1':'C2']  # cells from A1 to C2
    colC = ws['C']              # The whole column
    ow10 = ws[10]               # The whole row
    col_range = ws['C:D']       # Two columns
    row_range = ws[5:10]        # Two rows

    # Cells in each rows
    >>> for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    ...    for cell in row:
    ...        print(cell)
    <Cell Sheet1.A1>
    <Cell Sheet1.B1>
    <Cell Sheet1.C1>
    <Cell Sheet1.A2>
    <Cell Sheet1.B2>
    <Cell Sheet1.C2>

    # Cells in each columns
    >>> for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
    ...     for cell in col:
    ...         print(cell)
    <Cell Sheet1.A1>
    <Cell Sheet1.A2>
    <Cell Sheet1.B1>
    <Cell Sheet1.B2>
    <Cell Sheet1.C1>
    <Cell Sheet1.C2>

    # all cells in row
    >>> tuple(ws.rows)
    ((<Cell Sheet.A1>, <Cell Sheet.B1>, <Cell Sheet.C1>),
    (<Cell Sheet.A2>, <Cell Sheet.B2>, <Cell Sheet.C2>),
    ...)

    >>> tuple(ws.columns)
    ((<Cell Sheet.A1>, <Cell Sheet.A2>, ...),
    (<Cell Sheet.B1>, <Cell Sheet.B2>, ...),
    (<Cell Sheet.C1>, <Cell Sheet.C2>, ...))

    ws['A1'].row            # 1
    ws['A1'].column         # 'A'
    ws['A1'].coordinate     # 'A1'

Write-only cell::

    from openpyxl.writer.write_only import WriteOnlyCell
    from openpyxl.styles import Font
    cell = WriteOnlyCell(ws, value="hello world")
    cell.comment = Comment(text="A comment", author="Author's Name")
    cell.font = Font(name='Courier', size=36)
    ws.append([cell, 3.14, None])


Working with style:

See also: https://openpyxl.readthedocs.io/en/default/styles.html

Builtin styles: https://openpyxl.readthedocs.io/en/default/styles.html#using-builtin-styles


Merge/Unmerge cells::

    ws.merge_cells('A1:B1')
    ws.unmerge_cells('A1:B1')

    ws.merge_cells(start_row=2,start_column=1,end_row=2,end_column=4)
    ws.unmerge_cells(start_row=2,start_column=1,end_row=2,end_column=4)

Set the width of column::

    ws.column_dimensions['A'].width = 16

Using formulae::

    ws['D1'] = '=SUM(A1:C1)'

Using number format::

    ws['A2'] = datetime.datetime(2010, 7, 21)
    ws['A2'].number_format   # 'yyyy-mm-dd h:mm:ss'
    
    ws['A2'].number_format   # 'General'
    ws['A2'] = 0.12          # 0.12 when open by MS office
    ws['A2'].number_format = '0%'
    ws['A2'].value           # value still 0.12, but shown as 12%

Insert an image::

    from openpyxl.drawing.image import Image
    img = Image('logo.png')
    ws.add_image(img, 'A1')

Adding a comment to a cell::

    # One comment can only be assgined to one cell
    from openpyxl.comments import Comment
    ws["A1"].comment = Comment("Text", "Author")

Create a chart::

    >>> for i in range(1, 11):
    ...     ws['A%d'%i] = i
    >>> from openpyxl.chart import BarChart, Reference, Series
    >>> values = Reference(ws, min_col=1, min_row=1, max_col=1, max_row=10)
    >>> chart = BarChart()
    >>> chart.add_data(values)
    >>> ws.add_chart(chart, "E15")
    >>> wb.save("SampleChart.xlsx")

See also: https://openpyxl.readthedocs.io/en/default/charts/introduction.html

Fold columns::

    ws.column_dimensions.group('A','D', hidden=True)

Using filters and sorts::

    ws.auto_filter.ref = "A1:B15"
    ws.auto_filter.add_filter_column(0, ["Kiwi", "Apple", "Mango"])
    ws.auto_filter.add_sort_condition("B2:B15")

Save to a file::

    wb.save('myfile.xlsx')


Loading from a file
~~~~~~~~~~~~~~~~~~~

::
    >>> from openpyxl import load_workbook
    >>> wb2 = load_workbook('test.xlsx')
    >>> print wb2.get_sheet_names()
    ['Sheet2', 'New Title', 'Sheet1']

    # Read-only mode
    wb = load_workbook(filename='large_file.xlsx', read_only=True)
