from cv2 import *
from numpy import *
# from reconhecimentoDeFace.OpenCVFaceRecog import *


def desenharRetangulo(imagem, retangulo):
    (x, y, w, h) = retangulo
    rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)

def selecionarImagem(imagem, retangulo):
    (x, y, w, h) = retangulo
    imagemCopiada = imagem.copy()
    imagemRecortada = imagemCopiada[y:y+h, x:x+w]
    return imagemRecortada

imagemEntrada = imread("image.jpeg",0)
imagemSemRuido = GaussianBlur(imagemEntrada, (5, 5), 0)

coordenadaEntrada1 = (345,245,20,20)
coordenadaEntrada2 = (377,245,20,20)
coordenadaEntrada3 = (407,245,20,20)

desenharRetangulo(imagemSemRuido,coordenadaEntrada1)
desenharRetangulo(imagemSemRuido,coordenadaEntrada2)
desenharRetangulo(imagemSemRuido,coordenadaEntrada3)

classeA = selecionarImagem(imagemSemRuido,coordenadaEntrada1)
classeB = selecionarImagem(imagemSemRuido,coordenadaEntrada2)
classeC = selecionarImagem(imagemSemRuido,coordenadaEntrada3)

imshow("Imagem Sem Ruido", imagemSemRuido)
imshow("ClasseA", classeA)
imwrite("imagensSalvas/classeA.jpg",classeA)
imshow("ClasseB", classeB)
imwrite("imagensSalvas/classeB.jpg",classeB)
imshow("ClasseC", classeC)
imwrite("imagensSalvas/classeC.jpg",classeC)

waitKey(0)
destroyAllWindows()
