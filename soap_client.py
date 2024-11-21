from zeep import Client

# URL do WSDL (não temos WSDL neste exemplo, então usamos o endpoint diretamente)
endpoint = "http://127.0.0.1:8080/ws"

# XML de Requisição SOAP
req_soap = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tim="http://example.com/time">
   <soapenv:Header/>
   <soapenv:Body>
      <tim:GetServerTime/>
   </soapenv:Body>
</soapenv:Envelope>
"""

# Usar Zeep para enviar a requisição SOAP
from zeep.transports import Transport
from requests import Session

sessão = Session()
transporte = Transport(session=sessão)

resposta = sessão.post(endpoint, data=req_soap, headers={"Content-Type": "text/xml"})

# Exibir a resposta SOAP
print("SOAP Resposta:")
print(resposta.text)