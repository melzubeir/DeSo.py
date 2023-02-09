### Posts

1. Get posts stateless - getting info about post

```python
import deso

desoPosts = deso.Posts()
postHashHex = "74d50e4d33b7512941a2ada91a947aecfc2f9fd179d67eb1e0008d4812597196"
print(desoPosts.getPostsStateless(postHashHex= postHashHex, numToFetch=10).json())

# There are other functions in getPostsStateless that can be used to get more information about a post.
```

2. Get single post information

```python
import deso

desoPosts = deso.Posts()
postHashHex = "74d50e4d33b7512941a2ada91a947aecfc2f9fd179d67eb1e0008d4812597196"
print(desoPosts.getSinglePost(postHashHex).json())
# There are other functions in getSinglePost() that can be used to get more information about a post.
```

3. Get posts by publicKey or user

```python
import deso

desoPosts = deso.Posts()
postHashHex = "74d50e4d33b7512941a2ada91a947aecfc2f9fd179d67eb1e0008d4812597196"
print(desoPosts.getPostsForPublicKey(username="ItsAditya").json())
# getPostsForPublicKey() has more arguments like publicKey, mediaRequired, numToFetch, lastPostHashHex, readerPublicKey etc.
```

4. Get serials of NFT post include other info

```python
import deso

desoPosts = deso.Posts()
postHashHex = "74d50e4d33b7512941a2ada91a947aecfc2f9fd179d67eb1e0008d4812597196"
print(desoPosts.getNFTEntriesForNFTPost(postHashHex).json())
```




5. Get likes for post

```python
import deso

desoPosts = deso.Posts()
postHashHex = "74d50e4d33b7512941a2ada91a947aecfc2f9fd179d67eb1e0008d4812597196"
print(desoPosts.getLikesForPost(postHashHex).json())
# getLikesForPost has more arguments like limit, offset etc.
```

6. Get diamonds for post

```python
import deso

desoPosts = deso.Posts()
postHashHex = "74d50e4d33b7512941a2ada91a947aecfc2f9fd179d67eb1e0008d4812597196"
print(desoPosts.getDiamondsForPost(postHashHex).json())
# getDiamondsForPost has more arguments like limit, offset etc.
```

7. Get getQuoteRepostsForPost for post

```python
import deso

desoPosts = deso.Posts()
postHashHex = "74d50e4d33b7512941a2ada91a947aecfc2f9fd179d67eb1e0008d4812597196"
print(desoPosts.getQuoteRepostsForPost(postHashHex).json())
# getQuoteRepostsForPost has more arguments like limit, offset etc.
```

8. Get Hot feed/ Posts mentioning any @ username

```python
import deso
desoPosts = deso.Posts()
print(desoPosts.getHotFeed(taggedUsername="ItsAditya").json())
```
9. Get NFT info along with all the bids made to that NFT

```python
import deso

desoPosts = deso.Posts()
postHashHex = "74d50e4d33b7512941a2ada91a947aecfc2f9fd179d67eb1e0008d4812597196"
print(desoPosts.getNFTBidsForNFTPost(postHashHex).json())
```
