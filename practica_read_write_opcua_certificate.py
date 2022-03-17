from opcua import Client
from opcua import ua
import time

if __name__ == "__main__":

        client = Client("opc.tcp://10.62.48.213:48010")
        client.load_client_certificate("certificate.der")
        client.load_private_key("private_key.pem")
        client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate.der,private_key.pem")
        client.connect()
        node = client.get_node("ns=2;s=Demo.Static.Scalar.Int16")

        i = 0
        while i < 3:
            print
            node.set_value(ua.DataValue(ua.Variant(i, ua.VariantType.Int16)))
            node_value = node.get_value()
            print("Valor actual de la variable Int16: {}".format(node_value))
            i+=1 
            time.sleep(1)
        client.disconnect()
        print("Disconnected")
