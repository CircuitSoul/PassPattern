import re

senhasValidas = []

def filtro(anypass):
  pattern = re.compile(r'''^.*(?=.{1,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!_\/\\'.\-\¨@#$%*?;>)"(<^&+=]).*$''') #ty allan garcez
  findings = re.findall(pattern, anypass)
  if len(findings)>0:
    senhasValidas.append(anypass)
  
def main(senhasValidas):
  with open('senhas.txt', 'r') as f:
    for i in f:
      filtro(i)
    f.close()
  
  with open('senhasValidas.txt', 'w') as sV:
    for i in senhasValidas:
      sV.write(i)
    sV.close()
  
  
main(senhasValidas)
  
