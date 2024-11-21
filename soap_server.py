from flask import Flask, request, Response
from datetime import datetime, timezone
from lxml import etree

app = Flask(__name__)

# Função para gerar a resposta SOAP
def gerar_resp_soap():
    hora_atual = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    soap_resposta = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tim="http://example.com/time">
       <soapenv:Header/>
       <soapenv:Body>
          <tim:GetServerTimeResponse>
             <tim:ServerTime>{hora_atual}</tim:ServerTime>
          </tim:GetServerTimeResponse>
       </soapenv:Body>
    </soapenv:Envelope>
    """
    return soap_resposta

@app.route('/ws', methods=['POST'])
def soap_servico():
    # Receber e processar a requisição SOAP
    soap_req = request.data
    print("Requisição SOAP recebida:")
    print(soap_req.decode("utf-8"))

    # Verificar se é o método correto
    root = etree.fromstring(soap_req)
    body = root.find('.//{http://schemas.xmlsoap.org/soap/envelope/}Body')
    if body is not None:
        # Gera uma resposta SOAP
        soap_resp = gerar_resp_soap()
        return Response(soap_resp, mimetype='text/xml')
    else:
        return Response("Requerimento SOAP Inválido", status=400)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)