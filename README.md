# Improved-dpcm

This repo is about an improved version of dpcm compression, in which step size is dynamically changed.

The audio converter uses unsigned 8 bit audio stored as hexadecimal in text file.

To convert an audio file into that format without code, you can import your file into audacity, select File -> Export audio,
Set Format to other uncompressed files, Channels to mono, Header to RAW (header-less) and encoding as unsigned 8-bit PCM.

*If you are using tenacity, first mix your track down to mono if it's in stereo (select Tracks -> Mix -> Mix Stereo Down to Mono). Then select File -> Export -> Export audio, set Other uncompressed files, save and set Format Options to RAW (header-less) and Unsigned 8-bit PCM.*

Then go to https://tomeko.net/online_tools/file_to_hex.php, untick the two checkboxes and paste the result into a text file.

Now run hex_audio_converter.py and enter the file paths it asks you for.

To create the bytebeat file, Paste the code from the player.js file and fill in the file="" string with the content from your output file.


An example file is also included, it uses a 20 second audio clip of Scarlet Fire by Otis McDonald.

It is meant to be used on https://dollchan.net/bytebeat on bytebeat mode at 44100 Hz.
