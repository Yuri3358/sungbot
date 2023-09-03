<h1>Projeto Sungbot</h1>

<h2>Conceito</h2>

<p>O nome vem da concatenação das palavras <strong>sung</strong>lasses e <strong>bot</strong>, o sungbot serve como objeto de estudo para a criação de bots para o discord utilizando Python.</p>
<p>A ideia da criação de um bot no Discord surgiu em 2018, mas que foi concretizada somente dois anos depois ao estudar programação, sendo essa ideia meu motivo para aprender a programar.</p>

<h2>Lista de módulos</h2>

<h3>Calculator</h5>
    <p>Realiza operações matemáticas simples: soma, multiplicação, divisão e potenciação.</p>
    <p>Forma de utilização: <code>/calc {expressão}</code></p>
<hr>

<h3>Currencyrates</h5>
    <p>Converte qualquer quantia em Real Brasileiro, se nenhuma quantia é passada, retornará a cotação atual.</p>
    <p>Forma de utilização: <code>/dolar [quantia]</code></p>
<hr>

<h3>Icon</h5>
    <p>Exibe em uma embed o ícone do usuário mencionado (se nenhum é especificado o alvo passa a ser o autor do comando).</p>
    <p>Forma de utilização: <code>/icon [usuario]</code></p>
<hr>

<h3>Ping</h5>
    <p>Retorna quantos milisegundos levam para o bot responder o usuário</p>
    <p>Forma de utilização: <code>/ping</code></p>
<hr>

<h3>Rockpaper</h5>
    <p>Jogo simples de pedra, papel e tesoura.</p>
    <p>Forma de utilização: <code>/jokenpo</code></p>
<hr>

<h3>Rolldice</h5>
    <p>Rola um dado cujo padrão de faces é 6</p>
    <p>Forma de utilização: <code>/roll [faces]</code></p>
<hr>

<h3>Whois</h5>
    <p>Retorna informações relevantes sobre websites (data de criação, cidade e estado [quando houver]).</p>
    <p>Forma de utilização: <code>/whois {site}</code></p>
<hr>

<h3>Plot</h3>
    <p>Gera um gráfico em linha dada uma função f(x), ex.:x*10, x*2</p>
    <p>Forma de utilização: <code>/plot {x} {y} [highlight_x] [highlight_y]</code></p>
<hr>

<h3>CEP</h3>
    <p>Retorna informações sobre um CEP.</p>
    <p>Forma de utilização: <code>/cepinfo {cep}</code></p>
<hr>

<h3>Img</h3>
    <p>Retorna imagens obtidas a partir do Google em forma de paginação.</p>
    <p>Forma de utilização: <code>/img {search}</code></p>
<hr>

<h3>Weather</h3>
    <p>Retorna algumas informações meteorológicas sobre o local especificado.</p>
    <p>Forma de utilização: <code>/weather {city}</code></p>
<hr>

<h3>Userinfo</h3>
    <p>Retorna informações básicas sobre um usuário.</p>
    <p>Forma de utilização: <code>/userinfo {id | mention}</code></p>
<hr>
<h3>MAD (Modo de Autodestruição)</h3>
    <p>Apaga todos os chats do servidor, somente o proprietário do bot pode utilizá-lo</p>
    <p>Forma de utilização <code>/mad {code}</code></p>
<hr>
<h2>Dependências</h2>
    <h3>Arquivos</h3>
        <p>.env contendo o token de acesso ao seu bot e das APIs utilizadas e o código do comando <code>/mad</code></p>
        <h3>Lista de APIs utilizadas (com tokens obrigatórios)</h3>
        <p><a href="https://serpapi.com/" target="_blank">SerpApi</a> - Google Images</p>
        <p><a href="https://tomorrow.io/" target="_blank">Tomorrow.io</a> - Clima</p>
    <hr>
    <h3>Bibliotecas</h3>
        <li>python-dotenv</li>
        <li>python-whois</li>
        <li>pycord</li>
        <li>matplotlib</li>
    <hr>
