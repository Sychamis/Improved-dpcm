def amplitude_diff(slice, amplitude, step):
    """Takes a string of 256 hex numbers, an amplitude and an initial step and checks how well dpcm can recreate the sound with these settings (the lower the better)"""
    diff = 0
    for el in range(128):
        byte = int(slice[el*2 : el*2 + 2], 16)
        
        if step < byte:
            step += amplitude
        else:
            step -= amplitude

        diff += abs(byte - step)
    return diff

with open(input("Output file path: "), 'w') as out:
    audio = open(input("Input file path: "),'r').read()# Hex
    amplitudes_tests = {}
    amplitudes = ""
    last_audio_byte = audio[len(audio) - 2:]
    audio += (128 * last_audio_byte)[len(audio) % 256:]# Fills the audio string so its length can be divided by 256 (uses the last byte to prevent a "pop" sound)
    step = 127
    length = len(audio) // 256
    for i in range(length):
        slice = audio[i*256 : i*256 + 256]
        for a in range(16):
            amplitudes_tests[hex(a)[2:]] = amplitude_diff(slice, a, step)
        
        best_amplitude = min(amplitudes_tests, key=amplitudes_tests.get)# Takes the amplitude that has the lowest score
        amplitudes += best_amplitude
        best_amplitude = int(best_amplitude, 16)

        for hex_digit in range(32):
            hex_bits = 0
            for bit in range(4):# 4 cycles -> 1 hex digit
                byte = int(slice[(hex_digit*4 + bit) * 2 : (hex_digit*4 + bit) * 2 + 2], 16)

                if step < byte:
                    hex_bits += 1 << 3 - bit
                    step += best_amplitude
                else:
                    hex_bits += 0
                    step -= best_amplitude

            out.write(hex(hex_bits)[2:])# 4 bits -> hex

        print(f"{i}/{length}", end = '\r')

    out.write(amplitudes)
