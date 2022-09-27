from operator import index
import xml.etree.ElementTree as Et
import conexao



#testando a conexão
cursor = conexao.conexao_banco()


numero_nfe = input('Digite o numero da Nfe:' )

print('Atualizando nfe...')
conexao.atualiza_nfe(numero_nfe)
print('Nfe atualizada com sucesso...')


caminho_arquivo = input(
    "Digite o nome do arquivo seguido de '.xml' Aqui ==>>   '")


tree = Et.parse(f'{caminho_arquivo}')
root = tree.getroot()


# dados da nfe
#valorADD = float(input('digite o valor da aliquota em "%" Aqui ==>> '))


#valorADD = valorADD / 100

#pegando valor da calculado
valorCalculo = float(input('digite o valor calculado:'))
#valorCalculo = valorCalculo / 100
'''for c in root.iter():
    print(c.tag)'''
# pegando chave Nfe


def pegando_chaveNfe(root):
    chave = dict(root[0].attrib)
    chaveAlterada = str(chave['Id']).replace('NFe', '')
    return chaveAlterada


'''def adicionar_valor(valor):
    v = float(valor)
    resultado = v + (v * valorADD)
    return f'{resultado:.2f}'''

#adicionar valor de aliquota
def valor_aliquota(valor):
    x = float(valor_calculado())
    v = float(valor)
    
    v = float(v * x)/100
    print('Resultado...'+ str(v))
    return f'{v:.2f}'

# def retorna_valorItem(xml):
def valor_baseICMS(valor):
    v = ( valorCalculo / valor) * 100  #float(valor) * valorADD
    return f'{v:.2f}'
# adicionando acrecimo na aliquota
totalicmsuf = []
#calcular aliquota ICMS
def valor_calculado():
    icmsBase = 0
    for xml in root.iter('{http://www.portalfiscal.inf.br/nfe}ICMSUFDest'):
    
        icmsBase = float(xml[0].text)
        
        break
      
    percentual_base = valor_baseICMS(icmsBase)
    print('valor base'+ str(percentual_base))
    return percentual_base
c=0
for xml in root.iter('{http://www.portalfiscal.inf.br/nfe}ICMSUFDest'):
    
    xml[6].text = valor_aliquota(xml[0].text)
    totalicmsuf.append(float(xml[6].text))
    print(xml[6].text +' totalItem: '+ str(c))
    c += 1

    
#adicionar valor total ICMSUFDEST
for xml in root.iter('{http://www.portalfiscal.inf.br/nfe}ICMSTot'):
    total = str(f'{sum(totalicmsuf):.2f}')
    xml[4].text = total #valor_aliquota(xml[0].text)
    print(xml[4].text)


tree.write(f'{pegando_chaveNfe(root)}-nfe.xml',
           encoding="UTF-8", xml_declaration=True)
print("xml alterado com sucesso!")
