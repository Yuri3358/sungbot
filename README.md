<h1>Projeto Sungbot</h1>

<h2>Conceito</h2>

<p>O nome vem da concatenação das palavras <strong>sung</strong>lasses e bot, o sungbot serve como objeto de estudo para a criação de bots para o discord utilizando Python.</p>
<p>A ideia da criação de um Discord bot surgiu em 2018, mas que foi concretizada somente dois anos depois ao estudar programação, sendo essa ideia meu motivo para aprender a programar.</p>

<h2>Lista de módulos</h2>

<h3>Calculator</h5>
    <p>Módulo referente ao comando <code>/calc</code>, responsável por calcular o resultado de expressões matemáticas.</p>
    <p>Forma de utilização: <code>/calc {expressão}</code></p>
<hr>

<h3>Currencyrates</h5>
    <p>Arquivo que contêm o comando <code>/dolar</code>, que faz cálculos com a cotação atual da moeda ao par do real.</p>
    <p>Forma de utilização: <code>/dolar [quantia]</code></p>
<hr>

<h3>Icon</h5>
    <p>Exibe em uma embed o ícone do usuário mencionado (se nenhum é especificado o alvo passa a ser o autor do comando).</p>
    <p>Forma de utilização: <code>/icon [usuario]</code></p>
<hr>

<h3>Ping</h5>
    <p>Mostra quantos milisegundos levam para o bot responder o usuário</p>
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
    <p>Dá ao utilizador informações relevantes sobre websites (data de criação, cidade e estado [quando houver]).</p>
    <p>Forma de utilização: <code>/whois {site}</code></p>
<hr>

<h3>Plot</h3>
    <p>Gera um gráfico em linha dada uma função f(x), ex.:x*10, x*2</p>
    <p>Forma de utilização: <code>/plot {x} {y} [highlight_x] [highlight_y]</code></p>
<hr>

<h3>CEP</h3>
    <p>Mostra informações sobre um CEP</p>
    <p>Forma de utilização <code>/cepinfo {cep}</code></p>
<hr>

<h3>Img</h3>
    <p>Retorna uma paginação de imagens obtidas a partir do Google.</p>
    <p>Forma de utilização <code>/img {search}</code></p>
<hr>

<h3>Weather</h3>
    <p>Retorna algumas informações meteorológicas sobre o local especificado.</p>
    <p>Forma de utilização <code>/weather {city}</code></p>

<h2>Dependências</h2>
    <h3>Arquivos</h3>
        <p>.env contendo o token de acesso ao seu bot e das APIs utilizadas</p>
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
