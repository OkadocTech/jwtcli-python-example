from jwcrypto import jwk, jwe, jws
from jwcrypto.common import json_encode


payload = '{"dob":"28/09/1990","email":"zulfikar@okadoc.com","expired":"2024-03-11T13:40:11+03:00","fg_payment":1,"gender":"Male","i dentity_id":"784199012435761","identity_type_id":1,"latitude":25.291228369481704,"longitude":55.384015291929245,"memberIDappointment":1322,"memberIDsender":1322,"mobilenumber":"971448474646","name":"Teuku Zulfikar Amin","networkID":119}'

# Make JWS Signature
signaturekey = "thisismycomputer"

jwstoken = jws.JWS(payload.encode('utf-8'))
jwstoken.add_signature(jwk.JWK.from_password(signaturekey) ,None, header={"alg":"HS256"})
jwsSig = jwstoken.serialize()

print("JWS: "+jwsSig+"\n")


# JWS to JWE
encrypterkey = "turnonmycomputer"
header =  {"alg": "dir","enc": "A128GCM","zip": "DEF", "cty": "JWT",}
jwetoken = jwe.JWE(jwsSig, recipient=jwk.JWK.from_password(encrypterkey), protected=header)
enc = jwetoken.serialize(compact=True)

# the jwe token should be decryptable with jwtcli-public cli app
print("JWE: "+ enc)

