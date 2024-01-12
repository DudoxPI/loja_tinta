import itertools
import math

galao_litros = 18
lata_litros = 3.6
galao_preco = 80
lata_preco = 25
cobertura = 6
area_ser_pintada = 250

tinta_gasta = area_ser_pintada/cobertura
tinta_gasta = math.ceil(tinta_gasta)
print(
    f'Para pintar {area_ser_pintada}m2, iremos gastar {tinta_gasta} litros\n'
    'E esta seriam as duas melhores opções:\n'
    )
lista_g = list((range(1, math.ceil(tinta_gasta/galao_litros+1))))
lista_l = list((range(1, math.ceil(tinta_gasta/lata_litros+1))))

mistura_latas = itertools.product(lista_g, lista_l)
mistura_latas = list(mistura_latas)

for i, j in mistura_latas:
    qtde_final = i*18 + j*3.6
    valor_final = i*80 + j*25
    # print(i, j, qtde_final, valor_final)
    if qtde_final >= tinta_gasta:
        proximos = math.isclose(qtde_final, tinta_gasta, rel_tol=0.05)
        if proximos == True:
            print(f'Galão {i} Lata {j} pintam {qtde_final} e terá um valor de R$ {valor_final}')
