import pandas as pd

def mostrar_estatisticas(dados):
    # Forçar o pandas a mostrar as informações como float, 2 casas decimais
    pd.set_option('display.float_format', lambda x: '%.2f' % x)

    # Selecionar apenas as colunas desejadas
    dados_numericos = dados[['NU_NOTA_REDACAO', 'NU_NOTA_GERAL', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT']]

    # Mostrar as estatísticas descritivas
    display(dados_numericos.describe())
