from alg_ShF import encode_ShF_str
from alg_stH import encode_stH_str
from alg_dinH import encode_dinH_str


def decode(string, codes):
    outputString = ''
    codedChar = ''
    for char in string:
        codedChar += char
        if codedChar in codes.values():
            outputString += list(codes.keys())[list(codes.values()).index(codedChar)]
            codedChar = ''
    return outputString


if (__name__ == "__main__"):
    string = input()

    codesSF = dict()
    outputSF = encode_ShF_str(string, codesSF)
    decodeSF = decode(outputSF, codesSF)
    len_SF = 0
    for i in codesSF.values():
        len_SF += len(i)

    codesHS = dict()
    outputHS = encode_stH_str(string, codesHS)
    decodeHS = decode(outputHS, codesHS)
    len_HS = 0
    for i in codesHS.values():
        len_HS += len(i)

    codesHD = dict()
    outputHD = encode_dinH_str(string, codesHD)
    decodeHD = decode(outputHD, codesHD)
    len_HD = 0
    for i in codesHD.values():
        len_HD += len(i)

    tableLayout = "{:<8}| {:<15}| {:<15}| {:<15}"
    headers = tableLayout.format("Char", "SF", "HS", "HD")
    print("_" * len(headers))
    print(headers)
    print("_" * len(headers))
    for ch in codesSF.keys():
        print(tableLayout.format(ch, codesSF[ch], codesHS[ch], codesHD[ch]))
    print("_" * len(headers))
    print(tableLayout.format("Total", len_SF, len_HS, len_HD))
    print('')

    print("Shannon-Fano encoding:\n\tencoded:", outputSF, "\n\tlength:", len(outputSF),
          "\n\tdecoded:", decodeSF)
    print("Static Huffman encoding:\n\tencoded:", outputHS, "\n\tlength:", len(outputHS),
          "\n\tdecoded:", decodeHS)
    print("Dynamic Huffman encoding:\n\tencoded:", outputHD, "\n\tlength:", len(outputHD),
          "\n\tdecoded:", decodeHD)
