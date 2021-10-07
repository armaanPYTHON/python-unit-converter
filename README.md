# python-unit-converter
This is a self made python module for simple conversion from one unit to another. I really had to bust my head trying to figure how to make the code smaller and smaller (more general, rather than just if/else statements).


This project basically has one main file (the ucon module). 2 other python files that are attached are other simple self made modules among which one of them (txtopp) has already been made as a separate repository on this same account.

The main ucon module basically takes user input and reads it.
The input is then matched with preexisting standard conversions (only for 1 unit).
The matched data if is the same, the code is continued, and if not, then the standard conversion is copied and the copy is modified.
The modified dataset is used to calculate the return value (with simple arithmetic).
The function then returns the calculated value as a string.

Thank You!
