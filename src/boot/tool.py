def text_to_bin(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read().replace(' ', '').replace('\n', '').replace('r', '')
        print(content)

text_to_bin('stage1.bits')
