# Extração de Dados do Site Magalu com Python e Selenium

Este projeto tem como objetivo realizar a automação da extração de dados de produtos (no caso, geladeiras) do site **Magazine Luiza** utilizando **Python**, **Selenium WebDriver**, e **PyAutoGUI**, salvando os resultados em um arquivo Excel.

---

## 📦 Estrutura do Projeto

Extraindo_dados_Magalu-main/ │ 
├── Extraindo dados Site Magalu.py # Script principal de automação 
├── .idea/ # Arquivos de configuração do ambiente (gerado pelo PyCharm)


---

## 🔧 Tecnologias Utilizadas

- **Python 3.10+**
- **Selenium**
- **PyAutoGUI**
- **Pandas**
- **XlsxWriter**
- **Google Chrome + ChromeDriver**

---

## 🚀 Funcionalidades

- Abre o navegador e acessa o site [magazineluiza.com.br](https://www.magazineluiza.com.br).
- Realiza a busca pelo termo “geladeira”.
- Espera o carregamento dos produtos na página.
- Extrai:
  - Nome do produto
  - Preço do produto
  - URL do produto
- Armazena as informações extraídas em um **DataFrame Pandas**.
- Exporta os dados para um arquivo Excel: `DadosGeladeiraMagalu.xlsx`.
- Ajusta a largura das colunas para melhor visualização no Excel.

---

## 📁 Saída Esperada

Arquivo gerado: `DadosGeladeiraMagalu.xlsx`

| Descrição do Produto | Preço | URL do Produto |
|----------------------|-------|----------------|
| Geladeira Brastemp X | R$... | https://...    |
| ...                  | ...   | ...            |

---

## ⚙️ Requisitos

Antes de executar o projeto, instale as dependências com:

```bash
pip install selenium pyautogui pandas xlsxwriter


