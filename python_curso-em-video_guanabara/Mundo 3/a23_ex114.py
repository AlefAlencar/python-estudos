# verifique se o site pudim.com.br está acessível
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('ERRO: site inacessível no momento.')
else:
    print('OK')
    print(site.read())
