from flask import Flask, request, jsonify
from wine import Wine
import numpy as np

app = Flask(__name__)

# Carrega o modelo apenas uma vez
w = Wine("somellia_model.parquet")

VALID_MODELS = {"mini", "mpnet", "distil"}


def _normalize_record_types(record):
    """Converte numpy e outros tipos não-JSON-friendly para tipos nativos do Python"""
    for k, v in record.items():
        if isinstance(v, (np.integer,)):
            record[k] = int(v)
        elif isinstance(v, (np.floating,)):
            record[k] = float(v)
        elif isinstance(v, (np.ndarray,)):
            record[k] = v.tolist()
    return record

@app.route("/")
def index():
    return "API de Recomendação de Vinhos está ativa."

@app.route("/recomendar", methods=["POST"])
def recomendar():
    data = request.get_json(force=True, silent=False)
    if data is None:
        return jsonify({"error": "JSON inválido"}), 400

    texto = data.get("texto") or data.get("description") or data.get("q")
    if not texto or not isinstance(texto, str):
        return jsonify({"error": "Campo 'texto' (string) é obrigatório"}), 400

    qtd = data.get("qtd", 10)
    model = data.get("model", "mini")
    peso = data.get("peso", 0.5)

    try:
        qtd = int(qtd)
    except (ValueError, TypeError):
        return jsonify({"error": "Campo 'qtd' deve ser inteiro"}), 400

    try:
        peso = float(peso)
    except (ValueError, TypeError):
        return jsonify({"error": "Campo 'peso' deve ser número (float)"}), 400

    if model not in VALID_MODELS:
        return jsonify({"error": f"Modelo inválido. Model deve ser um de {sorted(VALID_MODELS)}"}), 400

    if not 0.0 <= peso <= 1.0:
        return jsonify({"error": "Campo 'peso' deve estar entre 0.0 e 1.0"}), 400

    try:
        resultados = w.recomendar_vinho(texto, top_n=qtd, model=model, peso=peso)
    except Exception as e:
        return jsonify({"error": f"Ocorreu um erro ao gerar recomendações: {str(e)}"}), 500

    # Converte DataFrame em lista de dicionários e normaliza tipos
    records = resultados.to_dict(orient="records")
    records = [_normalize_record_types(r) for r in records]

    return jsonify({"data": records}), 200


if __name__ == "__main__":
    # Para desenvolvimento local: flask app.py
    app.run(host="0.0.0.0", port=5000, debug=True)