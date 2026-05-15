def text_to_bin(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        bit_string = f.read().replace(' ', '').replace('\n', '').replace('r', '')

    byte_array = bytearray()
    for i in range(0, len(bit_string), 8):
        byte_byte = bit_string[i:i+8]
        if len(byte_byte) == 8:
            byte_array.append(int(byte_byte, 2))

    with open(output_file, 'wb') as f:
        f.write(byte_array)

text_to_bin('../src/boot/stage1.bits', '../src/build/stage1.bin')
