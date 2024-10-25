import base64

hexnmber="42617365363420697320776964656C79207573656420666F722073656E64696E6720652D6D61696C206174746163686D656E74732E"
hexdecryption= bytes.fromhex(hexnmber)
base64numbers= base64.b64encode(hexdecryption)

print ("The encoded result is : ", base64numbers)