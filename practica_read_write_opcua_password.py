

#from asyncua import Client
#from asyncua import ua

from opcua import Client
from opcua import ua
import time

#import sys
#sys.path.insert(0, "..")


if __name__ == "__main__":
    print("starting....xxx")
    opcua_server_address ="opc.tcp://10.62.52.204:48010"
    #opcua_server_address ="opc.tcp://10.62.52.204:48010"
    #opcua_server_address ="opc.tcp://169.254.23.30:48010"
    client = Client(opcua_server_address) #OPC-UA server address
    print("client gotten....{}".format(opcua_server_address))
    #client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate_ibon.der,privatekey_ibon.pem") #Seguridad de la conexion
    #client.set_security_string("Basic256,SignAndEncrypt,certificate.der,private_key.pem") #Seguridad de la conexion
    username = "john"
    password = "master"
    #username = "IoTLab"
    #password = "pa55word21"
    
    client.set_user(username)
    client.set_password(password)


    print("gonna connect to Servidor OPCUA")
    client.connect() #Conexion OPC-UA
    
    
    client.connect_socket()
    client.create_session()
    client.activate_session()


    print("connectado a Servidor OPCUA")

    node = client.get_node("ns=2;s=Demo.Static.Scalar.Int16") #Direccion del nodo 
    #node = client.get_node("ns=6;s=::AsGlobalPV:iNumber") #Direccion del nodo
    
    i = 0
    while i < 5:
        print
        node.set_value(ua.DataValue(ua.Variant(i, ua.VariantType.Int16))) #Escribir valor i
        node_value = node.get_value() #Leer valor
        print("Valor actual de la variable Int16: {}".format(node_value))
        i+=1
        time.sleep(1)
    client.disconnect() #Desconexion OPC-UA
