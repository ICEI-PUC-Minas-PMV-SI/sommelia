from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

class Wine:

    def __init__(self, df_name):
        self.df = pd.read_parquet(f"model/{df_name}")
        
        self.sentence_model_mpnet = SentenceTransformer('all-mpnet-base-v2')
        self.sentence_model_distil = SentenceTransformer('all-distilroberta-v1')
        self.sentence_model_mini = SentenceTransformer('all-MiniLM-L6-v2')


    def recomendar_vinho(self, texto, top_n=5, model="mini", peso=0.5):
        """
        Recebe um texto de entrada e retorna os vinhos mais similares semanticamente.
        Peso pondera entre Similaridade e Pontuação. 0.0 Considera só pontuação e 1.0 considera só similaridade
        """
        sentence_model = {
            "mini": self.sentence_model_mini,
            "mpnet": self.sentence_model_mpnet,
            "distil": self.sentence_model_distil
        }.get(model)

        if sentence_model is None:
            raise ValueError("Modelo desconhecido")

        coluna = {
            "mini": 'embedding_mini',
            "mpnet": 'embedding_mpnet',
            "distil": 'embedding_distil',
        }.get(model)

        # Gerar embedding do texto de entrada
        query_emb = sentence_model.encode([texto], normalize_embeddings=True)

        # Calcular similaridade com todas as descrições
        all_embeddings = np.vstack(self.df[coluna])
        sim = cosine_similarity(query_emb, all_embeddings).flatten()

        # Normaliza os Points entre 0 e 1
        ## TODO: Isso pode ser feito na engenharia de dados
        points_norm = (self.df["points"] - self.df["points"].min()) / (self.df["points"].max() - self.df["points"].min())

        # Define o Score final com base no Peso, Pontuação Normalizada e Similaridade
        score_final = peso * sim + (1 - peso) * points_norm

        # Pegar os índices com maior a pontuação final
        top_idx = score_final.argsort()[-top_n:][::-1]

        # Retornar DataFrame com similaridade
        resultados = self.df.iloc[top_idx][['description', 'title', 'country', 'region_1', 'price', 'points']].copy()
        # resultados['similaridade'] = sim[top_idx]
        # resultados["points_norm"] = points_norm.iloc[top_idx]
        resultados["score_final"] = round(score_final[top_idx].iloc[0] * 100, 2)

        return resultados.reset_index(drop=True)
