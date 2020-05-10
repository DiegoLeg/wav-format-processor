# Wav Format Processor

As some Python audio libraries present some issues working with 24-bit audio files (SciPy) and sampling frequencies greater than 48 kHz (WAVE), this simple Python class allows the user to obtain the number of channels, sampling frequency and bit-depth from any .wav file.

Following the canonical form of the WAVE file format, the information is extracted from the first 36 bytes (more specifically, from the bytes 12 to 36) of the total file. Bytes from 12 to 36 correspond to the FMT subchunk, describing the parameters retrieved in this class (number of channels, sampling frequency and bit-depth).

http://soundfile.sapp.org/doc/WaveFormat/xwav-sound-format.gif.pagespeed.ic.tIS-Bqb8Y1.png

SOURCE: http://soundfile.sapp.org/doc/WaveFormat/

The paramters are retrieved in string format.
