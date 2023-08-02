from jwcrypto import jwk, jwe, jws

# This payload going to be converted to JWS in JWE token
payload = '{"dob":"28/09/1990","email":"zulfikar@okadoc.com","expired":"2024-03-11T13:40:11+03:00","fg_payment":1,"gender":"Male","i dentity_id":"784199012435761","identity_type_id":1,"latitude":25.291228369481704,"longitude":55.384015291929245,"memberIDappointment":1322,"memberIDsender":1322,"mobilenumber":"971448474646","name":"Teuku Zulfikar Amin","networkID":119}'

# JWS Signature KEY
signaturekey = "thisismycomputer"

# Build the JWS payload
jwstoken = jws.JWS(payload.encode('utf-8'))
jwstoken.add_signature(jwk.JWK.from_password(signaturekey) ,None, header={"alg":"HS256"})
jwsSig = jwstoken.serialize()

# This JWS going to be encrypted to JWE
print("\nJWS: "+jwsSig+"\n")


# JWE Encrypter Key
encrypterkey = "turnonmycomputer"

# Build the JWE Token from jwsSig
header =  {"alg": "dir","enc": "A128GCM","zip": "DEF", "cty": "JWT",}
jwetoken = jwe.JWE(jwsSig, recipient=jwk.JWK.from_password(encrypterkey), protected=header)
enc = jwetoken.serialize(compact=True)

# the jwe token should be decryptable with jwtcli-public cli app
print("JWE: "+ enc+"\n")

