### Social

1. Making post to deso blockchain

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'
desoSocial = deso.Social(PUBLIC_KEY, SEED_HEX)
'''In the above deso.Social() constructor, you can pass `derivedPublicKey` and `derivedSeedHex`
to make the transactions using derived keys.
NOTE: YOU MUST PASS ORIGINAL PUBLIC KEY TO CREATE THE TRANSACTION
''''

# submitPost() takes many optional argument like imageURLs, videoURLs, postExtraData etc.
# you will use the same function to make comment and quote any post.
print(desoSocial.submitPost("This is a test post")) #returns a response object. add .json() in end to see complete response
```

2. Follow user

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(nodeURL="https://diamondapp.com/api/v0/",  publicKey = PUBLIC_KEY, seedHex = SEED_HEX)
print(desoSocial.follow("BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg", isFollow=True).json())
```

3. Repost a post

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
postHashHexToRepost = "bd292216e8cc1b7f2dd2cc6bba5afa20b65a4b9966ea191644c90254bedbe177"
print(desoSocial.repost(postHashHexToRepost).json())
```

4. Quote a post

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
postHashHexToQuote = "bd292216e8cc1b7f2dd2cc6bba5afa20b65a4b9966ea191644c90254bedbe177"
print(desoSocial.quote(body = "this is quoted post", postHashHexToQuote).json())
```

5. Like a post

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
postHashHex = "bd292216e8cc1b7f2dd2cc6bba5afa20b65a4b9966ea191644c90254bedbe177"
print(desoSocial.like(postHashHex, isLike=True).json())
```

6. Diamond a post

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
postHashHex = "bd292216e8cc1b7f2dd2cc6bba5afa20b65a4b9966ea191644c90254bedbe177"
receiverPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoSocial.diamond(postHashHex, receiverPublicKey,  diamondLevel=2).json())
```

7. Update Profile

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
print(desoSocial.updateProfile(FR=10, description="This is my description",
      username="NotItsAditya", profilePicBase64='').json())


# In the above example, make sure profilePicBase64 is BASE64 encoded image otherwise it wont' work.
# you can also pass `extraData`, a dict argument for extra data in profile
```

8. Send Private Message

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
receiverPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoSocial.sendPrivateMessage(receiverPublicKey, "This DM is send using DesoPy library").json())
```

9. Minting a postHashHex as NFT

```python
import deso

SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
postHashHex = "bd292216e8cc1b7f2dd2cc6bba5afa20b65a4b9966ea191644c90254bedbe177"
print(desoSocial.mint(postHashHex, minBidDeSo=1, copy=2, creatorRoyality=10, coinHolderRoyality=4, isForSale=True).json())
```

10. Updating NFT to put it on sale, or as buy now etc.

```python
import deso
SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
postHashHex = "bd292216e8cc1b7f2dd2cc6bba5afa20b65a4b9966ea191644c90254bedbe177"
print(desoSocial.updateNFT(postHashHex, buyNowPriceInDeso=2,
      buyNow=True, minBidDeso=1.5, forSale=2, serialNumber=1).json())
```

11. Burn an NFT

```python

import deso
SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
postHashHex = "bd292216e8cc1b7f2dd2cc6bba5afa20b65a4b9966ea191644c90254bedbe177"
print(desoSocial.burnNFT(postHashHex, serialNumber=2).json())
```

12. Create NFT Bid

```python

import deso
SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
postHashHex = "bd292216e8cc1b7f2dd2cc6bba5afa20b65a4b9966ea191644c90254bedbe177"
print(desoSocial.createNFTBid(NFTPostHashHex=postHashHex, serialNumber=1, bidAmountDeso=2).json())
```

13. Transfer NFT

```python

import deso
SEED_HEX = 'YOUR SEED SEED_HEX'
PUBLIC_KEY = 'YOUR PUBLIC_KEY'

desoSocial = deso.Social(publicKey=PUBLIC_KEY, seedHex=SEED_HEX)
postHashHex = "bd292216e8cc1b7f2dd2cc6bba5afa20b65a4b9966ea191644c90254bedbe177"
receiverPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoSocial.transferNFT(postHashHex, receiverPublicKey, serialNumber=1).json())
```
