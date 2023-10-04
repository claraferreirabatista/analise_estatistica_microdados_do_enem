import pandas as pd

dados_tratados = pd.read_parquet('ENEM_CO_TRATADO.parquet')

def criar_tabela_de_para_idades():
    dp_idades = {
        'tp_faixa_etaria': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                             11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        'faixa_etaria': ['Menor de 17 anos', '17 anos', '18 anos', '19 anos', '20 anos',
                         '21 anos', '22 anos', '23 anos', '24 anos', '25 anos',
                         'Entre 26 e 30 anos', 'Entre 31 e 35 anos', 'Entre 36 e 40 anos', 'Entre 41 e 45 anos',
                         'Entre 46 e 50 anos', 'Entre 51 e 55 anos', 'Entre 56 e 60 anos',
                         'Entre 61 e 65 anos', 'Entre 66 e 70 anos', 'Maior de 70 anos'],
        'media_idade': [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 33, 38, 43, 48, 53, 58, 63, 68, 72]
    }

    dp_idades = pd.DataFrame(dp_idades).set_index('tp_faixa_etaria')

    return dp_idades

def criar_tabela_de_para_cor_raca():
    dp_raca = {
        'tp_cor_raca': [0, 1, 2, 3, 4, 5, 6],
        'cor_raca': ['Nao declarado', 'Branca', 'Preta', 'Parda', 'Amarela', 'Indigena', 'Nao dispoe da informacao']
    }

    dp_raca = pd.DataFrame(dp_raca).set_index('tp_cor_raca')

    return dp_raca

def criar_tabela_de_para_nacionalidade():
    dp_nacionalidade = {
        'tp_nacionalidade': [0, 1, 2, 3, 4],
        'nacionalidade_info': ['Nao informado', 'Brasileiro(a)', 'Brasileiro(a) Naturalizado(a)',
                               'Estrangeiro(a)', 'Brasileiro(a) Nato(a), nascido(a) no exterior']
    }

    dp_nacionalidade = pd.DataFrame(dp_nacionalidade).set_index('tp_nacionalidade')

    return dp_nacionalidade

def criar_tabela_de_para_situacao_conclusao():
    dp_conclusao = {
        'tp_st_conclusao': [1, 2, 3, 4],
        'situacao_do_ensino_medio': ['Ja conclui o Ensino Medio',
                                     'Estou cursando e concluirei o Ensino Medio no Ano da Prova',
                                     'Estou cursando e concluirei o Ensino Medio apos o Ano da Prova',
                                     'Nao conclui e nao estou cursando o Ensino Medio']
    }

    dp_conclusao = pd.DataFrame(dp_conclusao).set_index('tp_st_conclusao')

    return dp_conclusao

def criar_tabela_de_para_ano_conclusao():
    dp_ano_conclusao = {
        'tp_ano_concluiu': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                            11, 12, 13, 14, 15, 16],
        'ano_concluiu': ['Nao informado', '2021', '2020', '2019', '2018', '2017', '2016',
                         '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008',
                         '2007', 'Antes de 2007']
    }

    dp_ano_conclusao = pd.DataFrame(dp_ano_conclusao).set_index('tp_ano_concluiu')

    return dp_ano_conclusao

def criar_tabela_de_para_status_redacao():
    dp_redacao = {
        'tp_status_redacao': [1, 2, 3, 4, 6, 7, 8, 9],
        'status_redacao': ['Sem problemas', 'Anulada', 'Copia Texto Motivador', 'Em Branco',
                           'Fuga ao tema', 'Nao atendimento ao tipo textual', 'Texto insuficiente', 'Parte desconectada']
    }

    dp_redacao = pd.DataFrame(dp_redacao).set_index('tp_status_redacao')

    return dp_redacao
