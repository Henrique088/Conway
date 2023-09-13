import tkinter

def cria_matriz (linha, coluna):
    m = []
    for y in range(linha):
        f=[]
        for x in range(coluna):
            f.append(0)
        m.append(f)

    return  m

def cria_button (matriz,matriz_jogo,linha=0, coluna=0):
    matriz[linha][coluna] = tkinter.Button(Conway, text="0",fg="red", command=lambda: muda(matriz,matriz_jogo, linha, coluna))
    matriz[linha][coluna].grid(column=linha, row=coluna)

def muda(matriz,matriz_jogo, linha=0, coluna=0):
    matriz[linha][coluna] = tkinter.Button(Conway, text="1", fg="green", bg="yellow", command=lambda: muda2(matriz,matriz_jogo, linha, coluna))
    matriz[linha][coluna].grid(column=linha, row=coluna)
    matriz_jogo[linha][coluna] = 1

def muda2(matriz,matriz_jogo, linha=0, coluna=0):
    matriz[linha][coluna] = tkinter.Button(Conway, text="0", fg="red", command=lambda: muda(matriz, matriz_jogo, linha, coluna))
    matriz[linha][coluna].grid(column=linha, row=coluna)
    matriz_jogo[linha][coluna] = 0


def jogo(matriz_jogo,matriz):
    alive = 0
    matriz_jogo_temp = cria_matriz(10,10)

    for i in range(10):
        for j in range(10):

            if matriz_jogo[i][j] == 1 :
                try:
                   if matriz_jogo[i-1][j-1] == 1:
                       alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i-1][j] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i -1 ][j +1] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i][j-1] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i][j+1] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i+1][j -1] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i+1][j] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i+1][j + 1] == 1:
                        alive += 1
                except:
                   pass

            else:
                try:
                    if matriz_jogo[i - 1][j - 1] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i - 1][j] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i - 1][j + 1] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i][j - 1] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i][j + 1] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i + 1][j - 1] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i + 1][j] == 1:
                        alive += 1
                except:
                    pass

                try:
                    if matriz_jogo[i + 1][j + 1] == 1:
                        alive += 1
                except:
                    pass

            if alive <2 or alive >3:

                matriz_jogo_temp[i][j]  = 0
                alive = 0

            elif alive == 3:
                matriz_jogo_temp[i][j] = 1
                alive = 0
            else:

                if matriz_jogo[i][j] ==0:
                    matriz_jogo_temp[i][j] = 0
                else:
                    matriz_jogo_temp[i][j] = 1
                alive =0

    atualizando_board(matriz_jogo, matriz_jogo_temp, matriz)

def atualizando_board(matriz_jogo, matriz_jogo_temp, matriz):

    for linha in range(10):
        for coluna in range(10):
           if matriz_jogo_temp[linha][coluna] == 0:
               muda2(matriz,matriz_jogo,linha,coluna)

           else:
               muda(matriz,matriz_jogo,linha,coluna)


if __name__== '__main__':
    Conway = tkinter.Tk()

    Conway.title("Conway")
    Conway.geometry("408x455")
    Conway.minsize(360,355)
    Conway.maxsize(360,455)
    matriz = cria_matriz(10, 10)
    matriz_jogo = cria_matriz(10, 10)
    for linha in range(10):
        for coluna in range(10):
            cria_button(matriz, matriz_jogo, linha, coluna)

    comeca = tkinter.Button(Conway, text="Rodar", bd=3, fg="blue", font="arial", justify="center",
                            command=lambda: jogo(matriz_jogo, matriz))
    comeca.grid(columnspan=10, rowspan=1, padx=5, pady=10)

    texto = tkinter.Label(Conway, text = "Jogo do Conway", anchor="w", width=44)

    texto.grid(column= 0, row=15, columnspan=15, rowspan=15)

    Conway.mainloop()