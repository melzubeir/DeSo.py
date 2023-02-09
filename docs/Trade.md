### Trade

1. Send deso to public Key

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'
desoTrade = deso.Trade(PUBLIC_KEY, SEED_HEX )

print(desoTrade.sendDeso( recieverPublicKeyOrUsername = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg", desoToSend = 0.01).json())
```

2. Buy creator coin

```python
import deso
SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoTrade = deso.Trade(PUBLIC_KEY, SEED_HEX)
creatorPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoTrade.buyCreatorCoin(creatorPublicKey=creatorPublicKey, desoAmountToBuy=2).json())
```

3. get creator coins held by a publicKey

```python
import deso

desoTrade = deso.Trade()
creatorPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoTrade.getHeldCoinsOfCreator(publicKeyOfCoin=creatorPublicKey).json())
```

4. Get selling amount of a creator coin

```python
import deso
desoTrade = deso.Trade()
coinsInCirculationNanos = 3857329848
balanceNanons = 34938
desoLockedNanos = 12948584035
print(desoTrade.amountOnSell(desoLockedNanos = desoLockedNanos, coinsInCirculation=coinsInCirculationNanos, balanceNanos=balanceNanos))
```

5. Selling a creator coin

```python
import deso
SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoTrade = deso.Trade(PUBLIC_KEY, SEED_HEX)

coinsToSellNanons = 34938
creatorPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoTrade.sellCreatorCoin(
    creatorPublicKey=creatorPublicKey,  coinsToSellNanos=coinsToSellNanons).json())
```

6. Send creator coin

```python
import deso
SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoTrade = deso.Trade(PUBLIC_KEY, SEED_HEX)

coinsToSendNanos = 34938
creatorPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoTrade.sendCreatorCoins(creatorPublicKey=creatorPublicKey,
      receiverUsernameOrPublicKey="Octane", creatorCoinNanosToSend=coinsToSendNanos).json())
```

7. Send DAO coins

```python
import deso
SEED_HEX = "Your seed Hex here"
PUBLIC_KEY = "Your public key"

'''Sends DAO coin to publicKey or username. Use the hex() function to convert a number to hexadecimal
for Example, if you want to send 15 DAO coin, set coinsToTransfer to hex(int(15*1e18))'''
desoTrade = deso.Trade(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
coinsToTransfer = 15
coinsToTransferInRequiredForamt = hex(int(coinsToTransfer * 1e18))
transferStatus = desoTrade.sendDAOCoins(coinsToTransfer=coinsToTransferInRequiredForamt,
                                        daoPublicKeyOrName="CockyClout", receiverPublicKeyOrUsername="ItsAditya")
print(transferStatus)
```

8. Burn DAO coins

```python
import deso
SEED_HEX = "Your seed Hex here"
PUBLIC_KEY = "Your public key"

'''Burns DAO coin of daoPublicKeyOrName. Use the hex() function to convert a number to hexadecimal
        for Example, if you want to burn 15 DAO coin, set coinsToBurn to hex(int(15*1e18))'''
desoTrade = deso.Trade(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
coinsToBurn = 5000000
coisToBurnInRequiredFormat = hex(int(coinsToBurn * 1e18))
burnStatus = desoTrade.burnDAOCoins(coinsToBurn=coisToBurnInRequiredFormat,
                                        daoPublicKeyOrName="CockyClout")
print(burnStatus)
```

9. Mint DAO coins
```python
import deso

SEED_HEX = "Your seed Hex here"
PUBLIC_KEY = "Your public key"

'''Mint DAO coins. Use the hex() function to convert a number to hexadecimal
        for Example, if you want to mint 15 DAO coin, set coinsToBurn to hex(int(15*1e18))'''
desoTrade = deso.Trade(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
coinsToMint = 1000000
coinsToBurnInRequiredFormat = hex(int(coinsToMint * 1e18))
mintStatus = desoTrade.mintDAOCoins(coinsToBurnInRequiredFormat)
print(mintStatus)
```
