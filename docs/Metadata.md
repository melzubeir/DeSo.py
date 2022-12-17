### Metadata

1. Getting Deso Price

```python
import deso

# takes two optional Argument; publicKey and nodeURL. By default NodeURL is https://node.deso.org/api/v0/"
desoMetadata = deso.Metadata()
response = desoMetadata.getExchangeRate() # returns a response object.
print(response.json()) #  you can also use response.status_code to check if request was succesful
```

2. Getting Node Health

```python
import deso
desoMetadata = deso.Metadata()
print(desoMetadata.getNodeHealth().json())
```

3. Getting App State which includes node fee, diamond level map and other info related to node

```python
import deso
desoMetadata = deso.Metadata()
print(desoMetadata.getAppState().json())
```

4. Getting value of each diamond

```python
import deso
desoMetadata = deso.Metadata()
print(desoMetadata.getDiamondLevelMap()) # getDiamondLevelMap takes optional inDesoNanos argument which is by default True.
```
