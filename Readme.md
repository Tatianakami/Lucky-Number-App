Gerador de Números para Loteria
🎲 Sobre o Projeto
Este é um projeto simples, porém completo, de uma aplicação web para gerar números da sorte para loteria. A aplicação é composta por um front-end interativo e um back-end em Python usando o framework Flask. O objetivo é demonstrar a comunicação entre as duas partes de uma aplicação web, onde o usuário interage com a interface (front-end) e a lógica de negócios (back-end) é processada no servidor.

✨ Funcionalidades
Geração de 15 números únicos e aleatórios entre 1 e 25.

Interface de usuário moderna e responsiva, construída com HTML e Tailwind CSS.

Comunicação assíncrona entre o front-end e o back-end usando JavaScript Fetch API.

Servidor web leve e eficiente, utilizando Python com Flask.

🛠️ Tecnologias Utilizadas
Back-end:

Python

Flask

Front-end:

HTML5

Tailwind CSS (via CDN)

JavaScript ES6+

🚀 Como Rodar o Projeto
Para executar esta aplicação em sua máquina, siga os passos abaixo:

1. Pré-requisitos
Certifique-se de ter o Python instalado. Recomenda-se o uso de um ambiente virtual.

2. Estrutura do Projeto
O projeto deve ter a seguinte estrutura de pastas para que o Flask encontre os arquivos corretamente:

/gerador_loteria_web
├── app.py
└── /templates
    └── index.html

3. Instalação
Navegue até o diretório raiz do projeto (gerador_loteria_web) no seu terminal e instale o Flask com o seguinte comando:

pip install Flask

4. Execução
Após a instalação, ainda no terminal, execute o servidor Flask:

python app.py

O servidor será iniciado em http://127.0.0.1:5000.

5. Acesso à Aplicação
Abra o seu navegador e acesse o endereço http://127.0.0.1:5000 para usar a aplicação.

📸 Demonstração do Projeto
<br>
<div align="center">
<img src="/assets/jpglot.jpg" alt="Demonstração visual do projeto." style="border-radius: 8px;">
</div>
<br>

<br>

📝 Próximos Passos
Este é um projeto inicial, mas pode ser expandido com várias funcionalidades, como:

Gerar números para diferentes tipos de loteria.

Salvar os jogos gerados em um banco de dados.

Adicionar animações e transições na interface.