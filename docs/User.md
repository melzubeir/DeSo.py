### User

1. Getting user profile

```python
import deso
desoUser = deso.User()
print(desoUser.getSingleProfile(username="ItsAditya").json())
# you can set username to "" and use publicKey instead. Like: getSingleProfiel(publicKey = "BBC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg")
```

2. Getting publicKey info

```python
import deso
desoUser = deso.User()
publicKeyList = ["BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg",
    "BC1YLhGyi3t6ppCMARk3pmXGTkrSJXw3GWxQsYwQp58897ho8Nbr1it"]
print(desoUser.getUsersStateless(listOfPublicKeys=publicKeyList).json())
```

3. Getting profile pic URL

```python
import deso
desoUser = deso.User()
print(desoUser.getProfilePicURL(
    "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"))
```

4. Getting User Messages

```python
import deso
desoUser = deso.User()
userPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoUser.getMessagesStateless(
    publicKey=userPublicKey, numToFetch=10).json())
# There are more argument in getMessagesStateless like sortAlgorithm, followersOnly, followingOnly, holdersOnly, holdingsOnly, fetchAfterPublicKey
```

5. Getting user notifications

```python
import deso
desoUser = deso.User()
userPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoUser.getNotifications(userPublicKey, numToFetch=1000).json())
# There are other argument in getNotifications() like startIndex, filterOutNotificationCategories, etc.
```

6. Getting User NFTs

```python
import deso
desoUser = deso.User()
userPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoUser.getNFTs(userPublicKey = userPublicKey, isForSale=True).json())
```

7.  Get derived keys of a user

```python
import deso
desoUser = deso.User()
userPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoUser.getDerivedKeys(userPublicKey).json())
```

8. Getting transaction info of a user

```python
import deso
desoUser = deso.User()
userPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoUser.getTransactionInfo(userPublicKey).json())
# There are other arguments in getTransactionInfo() like limit, lastPublicKeyTransactionIndex and lastTransactionIDBase58Check
```

9. Getting holders for a public key

```python
import deso
desoUser = deso.User()
userPublicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoUser.getHoldersForPublicKey(userPublicKey).json())
# There are other arugments in getHoldersForPublicKey like username, fetchAll, numToFetch, fetchHodlings, isDAOCOIN, lastPublicKey
```

10. Getting DAO coin limit orders of a DAO coin

```python
import deso
desoUser = deso.User()
daoCoinPublicKey = "BC1YLj3zNA7hRAqBVkvsTeqw7oi4H6ogKiAFL1VXhZy6pYeZcZ6TDRY"
print(desoUser.getDaoCoinLimitOrders(daoCoinPublicKey))
```


11. Getting DAO coin price (market price)

```python
import deso
desoUser = deso.User()
daoCoinPublicKey = "BC1YLj3zNA7hRAqBVkvsTeqw7oi4H6ogKiAFL1VXhZy6pYeZcZ6TDRY"
print(desoUser.getDaoCoinPrice(daoCoinPublicKey))
```

12. Geting user followings/followers


```python
import deso
desoUser = deso.User()
print(desoUser.getFollowsStateless(username = "ItsAditya").json())
```

The default behavior from the above code will return the users the account is following.
To get the list of the account's followers, you must set **getFollowing** to *False*.

```python
print(desoUser.getFollowsStateless(username = "ItsAditya", getFollowing = False).json())
```

13. Getting diamonds sent/received by a publicKey

```python
import deso

desoUser = deso.User()
publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
print(desoUser.getDiamondsForPublicKey(publicKey, received=False).json())
# set received = True to get diamonds given to a publicKey
```
