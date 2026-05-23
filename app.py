from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# =========================
# "BANCO DE DADOS SIMPLES"
# =========================
alunos = []
agenda = []

# =========================
# ROTAS - HOME
# =========================
@app.route("/")
def home():
    return jsonify({"mensagem": "API da escola funcionando!"})

# =========================
# ALUNOS
# =========================

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

@app.route("/alunos", methods=["POST"])
def criar_aluno():
    if not request.json:
        return jsonify({"erro": "Dados inválidos"}), 400

    data = request.json

    if not data.get("nome") or not data.get("idade"):
        return jsonify({"erro": "Nome e idade são obrigatórios"}), 400

    aluno = {
        "id": len(alunos) + 1,
        "nome": data.get("nome"),
        "idade": data.get("idade")
    }

    alunos.append(aluno)

    return jsonify({
        "mensagem": "Aluno criado com sucesso!",
        "aluno": aluno
    })

# =========================
# AGENDA
# =========================

@app.route("/agenda", methods=["GET"])
def listar_agenda():
    return jsonify(agenda)

@app.route("/agenda", methods=["POST"])
def criar_evento():
    if not request.json:
        return jsonify({"erro": "Dados inválidos"}), 400

    data = request.json

    if not data.get("titulo") or not data.get("data"):
        return jsonify({"erro": "Título e data são obrigatórios"}), 400

    evento = {
        "id": len(agenda) + 1,
        "titulo": data.get("titulo"),
        "data": data.get("data")
    }

    agenda.append(evento)

    return jsonify({
        "mensagem": "Evento criado com sucesso!",
        "evento": evento
    })

# =========================
# RODAR SERVIDOR
# =========================
if __name__ == "__main__":
    app.run(debug=True)