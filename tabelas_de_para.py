import pandas as pd

dados_tratados = pd.read_parquet('ENEM_CO_TRATADO.parquet')

def criar_tabela_de_para_idades():
    dp_idades = {
        'TP_FAIXA_ETARIA': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                             11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        'Faixa Etária': ['Menor de 17 anos', '17 anos', '18 anos', '19 anos', '20 anos',
                         '21 anos', '22 anos', '23 anos', '24 anos', '25 anos',
                         'Entre 26 e 30 anos', 'Entre 31 e 35 anos', 'Entre 36 e 40 anos', 'Entre 41 e 45 anos',
                         'Entre 46 e 50 anos', 'Entre 51 e 55 anos', 'Entre 56 e 60 anos',
                         'Entre 61 e 65 anos', 'Entre 66 e 70 anos', 'Maior de 70 anos'],
        'Média idade': [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 33, 38, 43, 48, 53, 58, 63, 68, 72]
    }

    dp_idades = pd.DataFrame(dp_idades).set_index('TP_FAIXA_ETARIA')

    return dp_idades



def criar_tabela_de_para_cor_raca():
    dp_raca = {
        'TP_COR_RACA': [0, 1, 2, 3, 4, 5, 6],
        'Cor/Raça': ['Não declarado', 'Branca', 'Preta', 'Parda', 'Amarela', 'Indígena', 'Não dispõe da informação']
    }

    dp_raca = pd.DataFrame(dp_raca).set_index('TP_COR_RACA')

    return dp_raca



def criar_tabela_de_para_nacionalidade():
    dp_nacionalidade = {
        'TP_NACIONALIDADE': [0, 1, 2, 3, 4],
        'Nacionalidade_info': ['Não informado', 'Brasileiro(a)', 'Brasileiro(a) Naturalizado(a)',
                               'Estrangeiro(a)', 'Brasileiro(a) Nato(a), nascido(a) no exterior']
    }

    dp_nacionalidade = pd.DataFrame(dp_nacionalidade).set_index('TP_NACIONALIDADE')

    return dp_nacionalidade




def criar_tabela_de_para_situacao_conclusao():
    dp_conclusao = {
        'TP_ST_CONCLUSAO': [1, 2, 3, 4],
        'Situação do Ensino Médio': ['Já concluí o Ensino Médio',
                                     'Estou cursando e concluirei o Ensino Médio no Ano da Prova',
                                     'Estou cursando e concluirei o Ensino Médio após o Ano da Prova',
                                     'Não concluí e não estou cursando o Ensino Médio']
    }

    dp_conclusao = pd.DataFrame(dp_conclusao).set_index('TP_ST_CONCLUSAO')

    return dp_conclusao


def criar_tabela_de_para_ano_conclusao():
    dp_ano_conclusao = {
        'TP_ANO_CONCLUIU': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                            11, 12, 13, 14, 15, 16],
        'Ano Concluiu': ['Não informado', '2021', '2020', '2019', '2018', '2017', '2016',
                         '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008',
                         '2007', 'Antes de 2007']
    }

    dp_ano_conclusao = pd.DataFrame(dp_ano_conclusao).set_index('TP_ANO_CONCLUIU')

    return dp_ano_conclusao


def criar_tabela_de_para_status_redacao():
    dp_redacao = {
        'TP_STATUS_REDACAO': [1, 2, 3, 4, 6, 7, 8, 9],
        'Status Redacao': ['Sem problemas', 'Anulada', 'Cópia Texto Motivador', 'Em Branco',
                           'Fuga ao tema', 'Não atendimento ao tipo textual', 'Texto insuficiente', 'Parte desconectada']
    }

    dp_redacao = pd.DataFrame(dp_redacao).set_index('TP_STATUS_REDACAO')

    return dp_redacao










