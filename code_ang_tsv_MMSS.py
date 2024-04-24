#gera angulos a partir do tsv em output_angle.tsv

import csv
import numpy as np
import math
import glob



diretorio = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv_Videos/input/MMSS'
# Busca por todos os arquivos TSV no diretório especificado
arquivos_tsv = glob.glob(f'{diretorio}/*.tsv')
# Verifica se há pelo menos um arquivo TSV na pasta
if arquivos_tsv:
    # Assume que estamos usando o primeiro arquivo encontrado
    input_file = arquivos_tsv[0]


output_angle = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv_Videos/angulos/MMSS/ang_MMSS_tsv.tsv'

def calculate_angle(point1, point2, point3):
    # Calculate vectors from point2 to point1 and point2 to point3
    vector1 = [point1[0] - point2[0], point1[1] - point2[1], point1[2] - point2[2]]
    vector2 = [point3[0] - point2[0], point3[1] - point2[1], point3[2] - point2[2]]
    #print(vector1)
    #print(vector2)
    # Calculate the dot product of the two vectors
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

    # Calculate the magnitudes of the two vectors
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))

    # Calculate the angle in radians
    angle_radians = math.acos(dot_product / (magnitude1 * magnitude2))

    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees




def calculate_angle_2d(point1, point2, point3):
    # Calculate vectors from point2 to point1 and point2 to point3 (disregarding Z coordinates)
    vector1 = [point1[0] - point2[0], point2[1] - point1[1]]
    vector2 = [point3[0] - point2[0], point2[1] - point1[1]]

    # Calculate the dot product of the two vectors
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

    # Calculate the magnitudes of the two vectors
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))

    # Calculate the angle in radians
    angle_radians = math.acos(dot_product / (magnitude1 * magnitude2))

    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees

count = 0


#
# explicar csv_out
#
# Read the input TSV file and create an output TSV file
with open(input_file, 'r') as tsv_in, open(output_angle, 'w', newline='') as tsv_out:
    reader = csv.reader(tsv_in, delimiter='\t')
    writer = csv.writer(tsv_out, delimiter='\t')
    frame = 0
    count = 0
    for row in reader:


    


        # Abdução ombro direito SHOULDER1 SHOULDER2 ELBOW1

        # Abdução ombro direito SHOULDER1 SHOULDER2 ELBOW1

        x1, y1, z1 = map(float, row[9:12])  # shoulder2
        x2, y2, z2 = map(float, row[6:9])  # shoulder1
        x3, y3, z3 = map(float, row[12:15])  # elbow1

        # Arredondando os pontos para 5 casas decimais
        x1, y1, z1 = round(x1, 5), round(y1, 5), round(z1, 5)
        x2, y2, z2 = round(x2, 5), round(y2, 5), round(z2, 5)
        x3, y3, z3 = round(x3, 5), round(y3, 5), round(z3, 5)

        ponto1 = [x1, y1, z1]
        ponto2= [x2, y2, z2]
        ponto3 = [x3, y3, z3]

        ang_abd_ombro_direito = calculate_angle(ponto1, ponto2, ponto3) #calcula abertura no ponto do meio
        



        #/////////////////////////////////////////////////////

        # Abducao ombro esquerdo SHOULDER1 SHOULDER2 ELBOW2 

        x12, y12, z12 = map(float, row[6:9])  # SHOULDER1
        x22, y22, z22 = map(float, row[9:12])  # SHOULDER2
        x32, y32, z32 = map(float, row[15:18])  # ELBOW2
        x12, y12, z12 = round(x12, 5), round(y12, 5), round(z12, 5)
        x22, y22, z22 = round(x22, 5), round(y22, 5), round(z22, 5)
        x32, y32, z32 = round(x32, 5), round(y32, 5), round(z32, 5)
        ponto1_ = [x12, y12, z12]
        ponto2_= [x22, y22, z22]
        ponto3_ = [x32, y32, z32]

        ang_abd_ombro_esquerdo = calculate_angle(ponto1_, ponto2_, ponto3_) #calcula abertura no ponto do meio
        
        #/////////////////////////////////////////////////////

        # Flexao cotovelo direito SHOULDER1 ELBOW1 WRIST1 

        x13, y13, z13 = map(float, row[6:9])  # SHOULDER1
        x23, y23, z23 = map(float, row[12:15])  # ELBOW1
        x33, y33, z33 = map(float, row[0:3])  # WRIST1
        x13, y13, z13 = round(x13, 5), round(y13, 5), round(z13, 5)
        x23, y23, z23 = round(x23, 5), round(y23, 5), round(z23, 5)
        x33, y33, z33 = round(x33, 5), round(y33, 5), round(z33, 5)
        ponto19 = [x13, y13, z13]
        ponto29= [x23, y23, z23]
        ponto39 = [x33, y33, z33]
     

        ang_flex_cotovelo_direito =calculate_angle(ponto19, ponto29, ponto39)


        #///////////////////////////////////////////////////////////
        
        # Flexao cotovelo esquerdo SHOULDER2 ELBOW2 WRIST2
        x14, y14, z14 = map(float, row[9:12])  # SHOULDER2
        x24, y24, z24 = map(float, row[15:18])  # ELBOW2
        x34, y34, z34 = map(float, row[3:6])  # WRIST2
        x14, y14, z14 = round(x14, 5), round(y14, 5), round(z14, 5)
        x24, y24, z24 = round(x24, 5), round(y24, 5), round(z24, 5)
        x34, y34, z34 = round(x34, 5), round(y34, 5), round(z34, 5)
        ponto16 = [x14, y14, z14]
        ponto26= [x24, y24, z24]
        ponto36 = [x34, y34, z34]
  



        ang_flex_cotovelo_esquerdo =calculate_angle(ponto16, ponto26, ponto36)

     
        #///////////////////////////////////////////////////////////

        # Flexao Ombro direito HIP1 SHOULDER1 ELBOW1
        
        x15, y15, z15 = map(float, row[18:21])  # HIP1
        x25, y25, z25 = map(float, row[6:9])  # SHOULDER1
        x35, y35, z35 = map(float, row[0:3])  # WRIST1
        x15, y15, z15 = round(x15, 5), round(y15, 5), round(z15, 5)
        x2, y2, z2 = round(x2, 5), round(y2, 5), round(z25, 5)
        x35, y35, z35 = round(x35, 5), round(y35, 5), round(z35, 5)
        ponto51 = [x15, y15, z15]
        ponto52= [x25, y25, z25]
        ponto53 = [x35, y35, z35]


        ang_flex_ombro_direito = calculate_angle(ponto51, ponto52, ponto53)
        #//////////////////////////////////////////////////////////

        # Flexao Ombro esquerdo HIP2 SHOULDER2 ELBOW2
        
        x16, y16, z16 = map(float, row[21:24])  # HIP2
        x26, y26, z26 = map(float, row[18:21])  # SHOULDER2
        x36, y36, z36 = map(float, row[15:18])  # ELBOW2
        x16, y16, z16 = round(x16, 5), round(y16, 5), round(z16, 5)
        x26, y26, z26 = round(x26, 5), round(y26, 5), round(z26, 5)
        x36, y36, z36 = round(x36, 5), round(y36, 5), round(z36, 5)
        ponto14 = [x16, y16, 0]
        ponto24= [x26, y26, 0]
        ponto34 = [x36, y36,0]

        ang_flex_ombro_esquerdo = calculate_angle(ponto14, ponto24, ponto34)

        new_row = [frame,"abd ombro direito:", ang_abd_ombro_direito,  "abd ombro esquerdo:", ang_abd_ombro_esquerdo,"flex cotovelo direito:", ang_flex_cotovelo_direito, "flex cotovelo esquerdo:", ang_flex_cotovelo_esquerdo,
                    "flex ombro direito:", ang_flex_ombro_direito, "flex ombro esquerdo:", ang_flex_ombro_esquerdo]
        frame += 1
        writer.writerow(new_row)
    count += 1


