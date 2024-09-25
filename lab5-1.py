def calculate_frequency(sentence):
    frequency = [0] * 65536
    for symbol in sentence:
        frequency[ord(symbol)] += 1
    return frequency

def build_huffman_array(frequency):
    huffman_array = []
    for i in range(65536):
        if frequency[i] > 0:
            huffman_array.append([i, frequency[i], ""])
    huffman_array.sort(key=lambda x: x[1])
    return huffman_array

def shannon_fano_encode(sentence, huffman_array):
    encoded_sentence = ""
    for symbol in sentence:
        for element in huffman_array:
            if element[0] == ord(symbol):
                code = ""
                for i in range(len(huffman_array)):
                    if element == huffman_array[i]:
                        while i > 0:
                            code = "0" + code if i % 2 == 0 else "1" + code
                            i = i // 2
                        break
                encoded_sentence += code
                break
    return encoded_sentence

def main():
    sentence = input("Введите строку: ")
    frequency = calculate_frequency(sentence)
    huffman_array = build_huffman_array(frequency)
    encoded_sentence = shannon_fano_encode(sentence, huffman_array)
    print("Зашифрованная строка:", encoded_sentence)

if __name__ == "__main__":
    main()


