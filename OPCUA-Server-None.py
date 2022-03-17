
import sys
sys.path.insert(0, "..")
import time


from opcua import ua, Client


if __name__ == "__main__":

    client = Client("opc.tcp://10.62.52.204:48010/") #OPC-UA server address
    #client = Client("opc.tcp://10.62.50.115:48010/") #OPC-UA server address
    client.connect() #Conexion OPC-UA
    
    node = client.get_node("ns=2;s=Demo.Static.Scalar.Int16") #Direccion del nodo 
    #node = client.get_node("ns=6;s=::AsGlobalPV:iNumber") #Direccion del nodo
    
    i = 0
    while i < 30:
        print
        node.set_value(ua.DataValue(ua.Variant(i, ua.VariantType.Int16))) #Escribir valor i
        node_value = node.get_value() #Leer valor
        print("Valor actual de la variable Int16: {}".format(node_value))
        i+=1
        time.sleep(1)
