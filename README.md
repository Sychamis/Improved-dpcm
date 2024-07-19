# Improved-dpcm

This repo is about an improved version of dpcm compression, where the step size is dynamically changed.

I included the python "audio converter":
It uses 8 bit audio as a hexadecimal text file.

To convert an audio file into that format without code, you can import your file into audacity, select File -> Export audio,
Set Format to other uncompressed files, Channels to mono, Header to RAW (header-less) and encoding as unsigned 8-bit PCM
Then go to https://tomeko.net/online_tools/file_to_hex.php, untick the two checkboxes and paste the result into a text file.

To create the bytebeat file, copy the code in player.js file in bytebeat and paste the file the python program created in the file="" string.


An example file is also included, it uses a 20 second audio clip of Scarelet by Otis McDonald.

It's meant to be used on https://dollchan.net/bytebeat on bytebeat mode at 44100 Hz.
