# Teste de Desempenho de Leitura e Concatenação de Arquivos com Pandas e Dask.

Este projeto tem como objetivo explorar e comparar a eficiência de operações do Pandas ao lidar com grandes conjuntos de dados. Duas abordagens distintas foram implementadas para avaliar o consumo de memória e o desempenho durante operações de concatenação e leitura de dados.

## Projeto 1: `pandas-break-memory.py`

### Descrição
O script `pandas-break-memory.py` visa demonstrar o problema de consumo excessivo de memória ao utilizar a função `pd.concat` para concatenar grandes volumes de dados, ou até mesmo para fazer a leitura de grandes conjuntos de dados na memória.

### Funcionalidade
1. Leitura de múltiplos arquivos CSV do diretório 'data-files'.
2. Tentativa de concatenar os DataFrames usando `pd.concat`.
3. Medição do tempo de execução e exibição do resultado ou interrupção do processo devido ao alto consumo de memória.
4. Se a memória da máquina não for alta, conseguimos um processo morto! Para processar 1GB de arquivo .csv foi consumido quase 8GB de RAM com isso levando o processo a ser derrubado pelo Kernel.

## Projeto 2: `pandas-no-break-memory.py`

### Descrição
O script `pandas-no-break-memory.py` aborda o problema de consumo excessivo de memória utilizando o PyArrow para escrita em formato Parquet e Dask para leitura eficiente de grandes conjuntos de dados.

### Funcionalidade
1. Leitura de múltiplos arquivos CSV do diretório 'data-files'.
2. Conversão dos DataFrames para o formato Parquet usando PyArrow.
3. Utilização do Dask para leitura eficiente em chunks.
4. Monitoramento do consumo de memória durante o processo.

## Execução

  **Requirement**
  ```pip and venv.
    virtualenv venv 
    source venv/bin/activate 
    pip install -r requirements.txt
  ```
- **Projeto 1:**
    ```bash
    python pandas-break-memory.py
    ```

- **Projeto 2:**
    ```bash
    python pandas-no-break-memory.py
    ```

## Resultados Esperados
- **Projeto 1:**
    - Demonstração do alto consumo de memória durante a concatenação, com possível interrupção do processo devido à falta de recursos.

- **Projeto 2:**
    - Utilização eficiente de memória durante a leitura em chunks, sem interrupções.

**Nota:** Certifique-se de ter os requisitos instalados antes da execução, utilizando `pip install -r requirements.txt`.

Lembre-se de ajustar o código conforme necessário e experimentar com diferentes conjuntos de dados para uma análise mais abrangente.
