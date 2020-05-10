# Wav Format Processor

As some Python audio libraries present some issues working with 24-bit audio files (SciPy) and sampling frequencies greater than 48 kHz (WAVE), this simple Python class allows the user to obtain the number of channels, sampling frequency and bit-depth from any .wav file.

Following the canonical form of the WAVE file format, the information is extracted from the first 36 bytes (more specifically, from the bytes 12 to 36) of the total file. Bytes from 12 to 36 correspond to the FMT subchunk, describing the parameters retrieved in this class (number of channels, sampling frequency and bit-depth).

<p align="center">
  <img width="612" height="567" src="http://soundfile.sapp.org/doc/WaveFormat/xwav-sound-format.gif.pagespeed.ic.tIS-Bqb8Y1.png">
</p>

SOURCE: http://soundfile.sapp.org/doc/WaveFormat/

The parameters are retrieved in string format.

_______________________________________________

Debido a que algunas librerías de audio para Python presentan ciertos problemas al utilizar archivos de 24 bits (SciPy) o de frecuencias de sampleo mayores a 48 kHz (WAVE), se presenta esta sencilla clase de Python para obtener los parámetros número de canales, frecuencia de sampleo y profundidad de bits de cualquier archivo .wav.
 
Siguiendo la forma canónica de representación de archivos con formato WAVE, se extrae la información de los primeros 36 bytes del archivo (específicamente, desde el byte 12 al 36). Estos bytes corresponden al subconjunto FMT, que describe los parámetros que se extraen de esta clase (número de canales, frecuencia de sampleo y profundidad de bits). 
