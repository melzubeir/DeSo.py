### Deso Identity

1. Getting JWT token

```python
import deso
SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoIdentity = deso.Identity(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
print(desoIdentity.getJWT())
```

2. Validate JWT token

```python
import deso
desoIdentity = deso.Identity()
jwt_tokenn = "" # JWT TOKEN TO VALIDATE
userPublicKey = "" # User's public Key whoose JWT you wanna validate
print(desoIdentity.validateJWT(JWT=jwt_token, publicKey=userPublicKey))
```

3. Sign transaction (OFFLINE OBVIOUSLY)

```python
import deso
SEED_HEX = 'YOUR SEED SEED_HEX'
transactionHex = " Transaction Hex of the transaction created by public Key"
desoIdentity = deso.Identity()
print(desoIdentity.signTransaction(seedHex = SEED_HEX, transactionHex=transactionHex))
```
