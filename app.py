from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Lógica para gerar os números da loteria
def gerar_numeros_loteria(quantidade, maximo):
    numeros_possiveis = list(range(1, maximo + 1))
    numeros_sorteados = random.sample(numeros_possiveis, quantidade)
    numeros_sorteados.sort()
    return numeros_sorteados

@app.route('/')
def index():
    # Esta rota renderiza a página HTML
    return render_template('index.html')

@app.route('/gerar_numeros')
def gerar_numeros_api():
    # Esta rota é a API que será chamada pelo front-end
    numeros = gerar_numeros_loteria(15, 25)
    # Retorna os números em formato JSON
    return jsonify(numeros)

if __name__ == '__main__':
    # Roda a aplicação Flask
    # O modo de depuração (debug=True) reinicia o servidor automaticamente
    # sempre que  fizer uma alteração no código.
    app.run(debug=True)
