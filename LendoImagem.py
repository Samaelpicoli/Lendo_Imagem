#bibliotecas que serão usadas
import pyautogui
import cv2
import pytesseract
import time

#baixar o pytesseract na sua máquina e passar o caminho do executável
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\samael.picoli\Documents\tesseract\tesseract.exe"

#pegando as coordenadas
local1 = input('Coloque o cursor no canto superior esquerdo da região que você deseja capturar e pressione enter...')
pos1 = pyautogui.position()

local2 = input('Coloque o cursor no canto inferior direito da região que deseja capturar e pressione enter...')
pos2 = pyautogui.position()

width = pos2[0] - pos1[0]
height = pos2[1] - pos1[1]
x = pos1[0]
y = pos1[1]

#tirando a foto, passando o nome e as coordenadas 
foto = pyautogui.screenshot("imagem.png", region=(x,y,width,height))
img = cv2.imread("imagem.png") #lê a foto
res=pytesseract.image_to_string(img) #transforma em string 

print(res)
#caso for rodar no cmd (recomendável, para conseguir pegar a imagem em outras janelas, colocar um time)
#time.sleep(100)
