
import requests
import urllib.request

# Usei a fórmula como função para fazer download de múltiplos vídeos sem
# necessitar de uma variável específica dentro de uma classe.

def fbdownload(link):

    # As headers são o cabeçalho para a utilização do request para fazer web scrapping
    # do link contendo o vídeo da plataforma.

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    r = requests.get(link, headers=headers) 
    html = r.text

    # Logo após que o link é requisitado, a página é toda convertida 
    # em texto e armazenada na memória do script

    scrapping = html.find('https:\/\/video.fbfh17-1.fna.fbcdn.net')

    # A fatiação da string que contém o texto do código fonte começa na variável "scrapping"
    # que procura o parâmetro source do vídeo da plataforma

    get_full_link = scrapping + 332 
    
    # O link possui aproximadamente 330 caracteres, então este número é adicionado na variável "get full link"
    # para registrar o parâmetro e tamanho do número de caracteres que precisamos

    full_link = html[scrapping:get_full_link]

    # Esta variável é responsável por conseguir todo o espaço de caracteres onde tem o link na qual
    # precisamos para fazer o download do vídeo

    filter_by_link = full_link.find('"')

    # Este link na qual estamos fatiando é composto por uma respota em json, então na primeira fatiação
    # da variável "scrapping" nós perdemos a primeiro par de áspas que contem o link, fazendo que só exista
    # as áspas do final do link. Então procuramos por ela, pois sabemos que se o link existe, ela estará lá no final
    # e tendo em teoria isto, também temos o final do link.

    get_final_link = full_link[:filter_by_link]

    # Tendo a teoria de código acima, podemos filtrar e fatiar novamente a variável, mas agora contendo
    # o final do link que precisamos possuir. Então fazemos o fatiamento com o final das áspas. Ou seja, com o final
    # do link que precisamos obter

    a = get_final_link.replace("https:\/\/","https://").replace("\/v\/", "/v/").replace("\\u0025", "%").replace("\/", "/")

    # tendo em vista isso, agora precisamos fazer alguns ajustes no nosso link que acabamos de obter, fazendo algumas alterações
    # significativas em relação ao resultado final de um longo processo de fatiamento. Toda esta variavel "A" faz co que o link
    # final possa ser executado e assim finalizando o processo de download do arquivo de vídeo

    correctLink = (a + "&dl=1")
    
    # Um dos parâmetros para download no final dos vídeos do facebook é ter "&dl=1" no final do link para definir
    # que o link está sendo levado automaticamente para download e não para visualização externa

    urllib.request.urlretrieve(correctLink, "fbvideo.mp4")

    # Conseguindo o link final, solicitamos que a biblioteca "urllib" faça o download do vídeo da plataforma Facebook
    # com o nome de "fbvideo.mp4" e sim, este nome pode ser modificado e alterado da forma que melhor desejar

fbdownload("Link")

"""
Considerações finais:
    Todos os vídeos da plataforma Facebook, quando são feitos o upload é automaticamente convertido
    e armazenado nos servidores como ".mp4" para melhor desempenho de funcionalidade, rápida resposta para
    visulização nos aplicativos e também uma forma de poupar custos de armazenamento, pois o formato mp4 é 
    um formato que não consome muito espaço quando convertido pois o arquivo perde qualidade.

    Concluo que este script foi inteiramente criado por mim e bati muito a cabeça para conseguir finalizar ele de 
    uma forma simples. A minha principal ideia foi criar este script para vincular videos com a plataforma "Discord"
    através do meu bot, espero que tenha ficado bem explicativo.
"""