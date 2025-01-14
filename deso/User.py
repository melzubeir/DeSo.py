import requests

NODES = [
    'https://node.deso.org/api/v0/',
    'https://love4src.com/api/v0/',
]
PUBKEY = "BC1YLgk64us61PUyJ7iTEkV4y2GqpHSi8ejWJRnZwsX6XRTZSfUKsop"


class User:
    def __init__(
        self,
        nodeURL=NODES[0],
        readerPublicKey=PUBKEY,
    ):
        self.NODE_URL = nodeURL
        self.readerPublicKey = readerPublicKey

    def getSingleProfile(
        self, username="", publicKey="", NoErrorOnMissing=False
    ):
        """Gives user profile info."""
        endpointURL = self.NODE_URL + "get-single-profile"
        payload = {
            "PublicKeyBase58Check": publicKey,
            "Username": username,
            "NoErrorOnMissing": NoErrorOnMissing,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-single-profile"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getUsersStateless(self, listOfPublicKeys, skipForLeaderboard=True):
        """Returns information about list of PublicKeys"""
        endpointURL = self.NODE_URL + "get-users-stateless"
        payload = {
            "PublicKeysBase58Check": listOfPublicKeys,
            "SkipForLeaderboard": skipForLeaderboard,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-users-stateless"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getProfilePicURL(self, publicKey):
        """Returns the profile pic URL for a public key"""
        profilePicURL = f"{self.NODE_URL}get-single-profile-picture/" \
            "{publicKey}?fallback=https://node.deso.org/assets/img/" \
            "default_profile_pic.png"
        return profilePicURL

    def getMessagesStateless(
        self,
        publicKey,
        numToFetch=25,
        sortAlgorithm="time",
        followersOnly=False,
        followingOnly=False,
        holdersOnly=False,
        holdingsOnly=False,
        fetchAfterPublicKey="",
    ):
        endpointURL = self.NODE_URL + "get-messages-stateless"
        payload = {
            "PublicKeyBase58Check": publicKey,
            "FetchAfterPublicKeyBase58Check": fetchAfterPublicKey,
            "NumToFetch": numToFetch,
            "HoldersOnly": holdersOnly,
            "HoldingsOnly": holdingsOnly,
            "FollowersOnly": followersOnly,
            "FollowingOnly": followingOnly,
            "SortAlgorithm": sortAlgorithm,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-messages-stateless"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getNotifications(
        self,
        publicKey,
        startIndex=-1,
        numToFetch=50,
        filterOutNotificationCategories={},
    ):
        # filterOutNotification is a map that looks like {"diamond": True,
        # "like": True,  "transfer": True, "follow": True, "nft": True,
        # "post": True} ever True means that the specific notification
        # category will be filtered out
        payload = {
            "PublicKeyBase58Check":
                publicKey,
            "FetchStartIndex":
                startIndex,
            "NumToFetch":
                numToFetch,
            "FilteredOutNotificationCategories":
                filterOutNotificationCategories,
        }
        # why is this endpoint different from the others?
        # [TODO - check on this]
        endpointURL = "https://diamondapp.com/api/v0/get-notifications"
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-notifications"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getNFTs(self, userPublicKey,
                isForSale=False):
        """Gets the NFTs associated with a user,
        setting isForSale = True returns only the NFTs that are for sale."""
        payload = {
            "UserPublicKeyBase58Check": userPublicKey,
            "ReaderPublicKeyBase58Check": self.readerPublicKey,
            "IsForSale": isForSale,
        }

        endpointURL = self.NODE_URL + "get-nfts-for-user"
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-nfts-for-user"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getDerivedKeys(self, publicKey):
        payload = {"PublicKeyBase58Check": publicKey}
        endpointURL = self.NODE_URL + "get-user-derived-keys"
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-user-derived-keys"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getTransactionInfo(
        self,
        publicKey,
        limit=200,
        lastTransactionIDBase58Check="",
        lastPublicKeyTransactionIndex=-1,
    ):
        payload = {
            "PublicKeyBase58Check": publicKey,
            "LastTransactionIDBase58Check": lastTransactionIDBase58Check,
            "LastPublicKeyTransactionIndex": lastPublicKeyTransactionIndex,
            "Limit": limit,
        }
        # why is this endpoint different from the others?
        # [TODO - check on this]
        endpointURL = "https://node.deso.org/api/v1/transaction-info"
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "transaction-info"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getHoldersForPublicKey(
        self,
        publicKey="",
        username="",
        fetchAll=False,
        numToFetch=100,
        fetchHodlings=False,
        isDAOCOIN=False,
        lastPublicKey="",
    ):
        payload = {
            "PublicKeyBase58Check": publicKey,
            "Username": username,
            "LastPublicKeyBase58Check": lastPublicKey,
            "NumToFetch": numToFetch,
            "FetchHodlings": fetchHodlings,
            "FetchAll": fetchAll,
            "IsDAOCoin": isDAOCOIN,
        }

        endpointURL = self.NODE_URL + "get-hodlers-for-public-key"
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-hodlers-for-public-key"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getFollowsStateless(
        self,
        username="",
        publicKey="",
        getFollowing=True,
        numToFetch=50,
        lastPublicKey="",
    ):
        """Returns list of user followings and followers"""
        payload = {
            "Username": username,
            "PublicKeyBase58Check": publicKey,
            "GetEntriesFollowingUsername": not getFollowing,
            "LastPublicKeyBase58Check": lastPublicKey,
            "NumToFetch": numToFetch,
        }

        endpointURL = self.NODE_URL + "get-follows-stateless"
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-follows-stateless"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getDaoCoinLimitOrders(self, daoCoinPublicKey):
        payload = {
            "DAOCoin1CreatorPublicKeyBase58Check": daoCoinPublicKey,
            "DAOCoin2CreatorPublicKeyBase58Check": "DESO",
        }
        endpointURL = self.NODE_URL + "get-dao-coin-limit-orders"
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-dao-coin-limit-orders"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

    def getDaoCoinPrice(self, daoCoinPublicKey, type="MARKET"):
        # returns dao coin price in DESO
        if type == "MARKET":
            daoLimtOrders = self.getDaoCoinLimitOrders(
                daoCoinPublicKey=daoCoinPublicKey
            ).json()
            lowestAsk = 0
            highestBid = 0
            orderList = daoLimtOrders["Orders"]
            for orders in orderList:
                operationType = orders["OperationType"]
                ExchangeRateCoinsToSellPerCoinToBuy = orders[
                    "ExchangeRateCoinsToSellPerCoinToBuy"
                ]
                daodaoPriceInDeso = 1 / ExchangeRateCoinsToSellPerCoinToBuy
                if operationType == "ASK":
                    if daodaoPriceInDeso < lowestAsk or lowestAsk == 0:
                        lowestAsk = daodaoPriceInDeso
                if operationType == "BID":
                    if (
                        ExchangeRateCoinsToSellPerCoinToBuy > highestBid
                        or highestBid == 0
                    ):
                        highestBid = ExchangeRateCoinsToSellPerCoinToBuy
            try:
                daoCoinPrice = (lowestAsk + highestBid) / 2
            except Exception:
                daoCoinPrice = 0
            return daoCoinPrice

    def getDiamondsForPublicKey(self, publicKey, received=True):
        """Returns diamonds received/given by publicKey."""
        payload = {
            "PublicKeyBase58Check": publicKey,
            "FetchYouDiamonded": not received,
        }
        endpointURL = self.NODE_URL + "get-diamonds-for-public-key"
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "get-diamonds-for-public-key"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response
