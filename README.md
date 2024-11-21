# SOA-SOAP
Este projeto demonstra como implementar um servidor SOAP utilizando o Flask e um cliente SOAP utilizando a biblioteca zeep.

## Visão Geral

### Servidor SOAP
- Implementado com Flask.
- Retorna a data e hora atuais ao receber uma requisição SOAP.

### Cliente SOAP
- Implementado com zeep para enviar requisições SOAP ao servidor e receber respostas.

## Estrutura do Projeto

- `soap_server.py`: Contém o código do servidor SOAP.
- `soap_client.py`: Contém o código do cliente SOAP.

## Requisitos

1. **Python**
2. **Bibliotecas necessárias**:
   - Flask
   - zeep

Para instalar:

```bash
pip install flask

pip install zeep