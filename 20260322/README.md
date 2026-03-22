# QR Decoder
Given a 6x6 matrix (array of arrays), representing a QR code, return the string of binary data in the code.

The QR code may be given in any rotation of 90 degree increments.
A correctly oriented code has a 2x2 group of 1's (orientation markers) in the bottom-left, top-left, and top-right corners.
The three 2x2 orientation markers are not part of the binary data.
The binary data is read left-to-right, top-to-bottom (like a book) when the QR code is correctly oriented.
A code will always have exactly one valid orientation.
For example, given:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "110000",
  "110001"
]
or given the same code with a different orientation:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "000011",
  "100011"
]
Return "000000000000000000000001", all the binary data excluding the three 2x2 orientation markers.
