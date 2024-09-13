import string

def criar_mapeamento_cesar(deslocamento):
    alfabeto = string.ascii_lowercase
    mapeamento = str.maketrans(alfabeto, alfabeto[deslocamento:] + alfabeto[:deslocamento])
    return mapeamento

def cifrar_cesar(texto, deslocamento):
    texto_minusculo = texto.lower()
    mapeamento = criar_mapeamento_cesar(deslocamento)
    return texto_minusculo.translate(mapeamento)

def inverter_blocos(texto, tamanho_bloco):
    blocos = [texto[i:i+tamanho_bloco] for i in range(0, len(texto), tamanho_bloco)]
    return ''.join(blocos[::-1])

def cifrar_com_permutacao(texto, deslocamento, tamanho_bloco):
    texto_cifrado = cifrar_cesar(texto, deslocamento)
    texto_permutado = inverter_blocos(texto_cifrado, tamanho_bloco)
    return texto_permutado

def decifrar_com_permutacao(texto_cifrado, deslocamento, tamanho_bloco):
    texto_invertido = inverter_blocos(texto_cifrado, tamanho_bloco) 
    texto_decifrado = cifrar_cesar(texto_invertido, -deslocamento)  
    return texto_decifrado

def restaurar_caracteres(texto_cifrado, texto_decifrado):
    resultado = []
    index_cifrado = 0
    for char in texto_cifrado:
        if char.isalnum():
            resultado.append(texto_decifrado[index_cifrado])
            index_cifrado += 1
        else:
            resultado.append(char)
    return ''.join(resultado)

def main():
    texto_claro = input("Digite o texto claro: ")
    
    if not texto_claro.strip():
        print("Erro: O texto de entrada não pode estar vazio.")
        return
    
    deslocamento = int(input("Digite o deslocamento: "))
    tamanho_bloco = int(input("Digite o tamanho do bloco: "))
    
    texto_cifrado = cifrar_com_permutacao(texto_claro, deslocamento, tamanho_bloco)
    texto_decifrado = decifrar_com_permutacao(texto_cifrado, deslocamento, tamanho_bloco)
    
    print("\nTexto Claro:", texto_claro)
    print("Texto Cifrado:", texto_cifrado)
    print("Texto Decifrado:", restaurar_caracteres(texto_cifrado, texto_decifrado))

if __name__ == "__main__":
    main()