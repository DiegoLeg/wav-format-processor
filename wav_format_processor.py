#WAVE does not allow sampling frequency >48kHz
#Scipy.io.wavfile does not work with 24 bits files.

import struct

class WavFormatProcessor():
    
    def wav_file_properties(self, filename):
        """Obtengo los parametros mas importantes de un archivo .wav.
        
        Parameters:
        filename: nombre del archivo a analizar
        
        Return:
        number_channels: Numero de canales
        sample_rate: Frecuencia de sampleo
        bit_depth: Profundiad de bits
        """

        wave_file = open(filename, "rb")
        
        # subchunk where the format parameters are specified = fmt.
        fmt = wave_file.read(36)  # read the first 36 bytes.

        number_channels_string = fmt[22:24] # number of channels is located on bytes 22 and 23 of the fmt subchunk.
        number_channels = struct.unpack("<H", number_channels_string)[0]
        # print(number_channels)

        sample_rate_string = fmt[24:28]  # sampling frequency is located on bytes 24, 25, 26 and 27 of the fmt subchunk.
        sample_rate = struct.unpack("<I", sample_rate_string)[0]
        # print (sample_rate)

        bit_depth_string = fmt[34:36]  # bit-depth is located on bytes 34 y 35 of the fmt subchunk.
        bit_depth = struct.unpack("<H", bit_depth_string)[0]
        # print (bit_depth)

        return (number_channels, sample_rate, bit_depth)
