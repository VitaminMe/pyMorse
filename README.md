pyMorse
======

This is a library that enables the conversion of text to Morse Code.
Currently implemented is that standard / minimal Morse Code set.
Morse code operators would have applied additional conversions to abbreviate
the text content and encrypt it (e.g. `SubstituteConverter`).

Use Makefile to run, install or test.  A Runner class is used to provide
a simple text user interface to enable encoding and decoding.  No sound effects
(dots/dashes) are applied in this library.  The Runner converts into Morse code
using a default substitution shift value of 5.  As a result SOS != "... --- ..."
because SOS is first shifted to "xtx" then to "-..- - -..-".
