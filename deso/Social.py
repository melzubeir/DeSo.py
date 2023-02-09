from deso.utils import submitTransaction, appendExtraData
import requests
from deso.Sign import Sign_Transaction
from arweave.arweave_lib import Transaction
from arweave.transaction_uploader import get_uploader
import arweave
import pathlib

NODES = [
    'https://node.deso.org/api/v0/',
    'https://love4src.com/api/v0/',
]
PUBKEY = "BC1YLgk64us61PUyJ7iTEkV4y2GqpHSi8ejWJRnZwsX6XRTZSfUKsop"


class Social:
    def __init__(
        self,
        publicKey,
        seedHex=None,
        nodeURL="https://node.deso.org/api/v0/",
        derivedPublicKey=None,
        derivedSeedHex=None,
        minFee=1000,
        derivedKeyFee=1700,
        appName="DesoPy",
    ):
        self.SEED_HEX = seedHex
        self.PUBLIC_KEY = publicKey
        self.NODE_URL = nodeURL
        self.appName = appName
        self.DERIVED_PUBLIC_KEY = derivedPublicKey
        self.DERIVED_SEED_HEX = derivedSeedHex
        self.MIN_FEE = minFee if seedHex else derivedKeyFee

    def submitPost(
        self,
        body,
        imageURLs=[],
        videoURLs=[],
        postHashHexToModify="",
        parentStakeID="",
        isHidden=False,
        repostedPostHash="",
        language="en",
        postExtraData={},
    ):
        postExtraData["App"] = self.appName
        postExtraData["Language"] = language
        error = None
        endpointURL = self.NODE_URL + "submit-post"
        finalPostExtraData = postExtraData

        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            if "DerivedPublicKey" not in finalPostExtraData:
                finalPostExtraData[
                    "DerivedPublicKey"
                ] = self.DERIVED_PUBLIC_KEY

        payload = {
            "UpdaterPublicKeyBase58Check": self.PUBLIC_KEY,
            "PostHashHexToModify": postHashHexToModify,
            "ParentStakeID": parentStakeID,
            "Title": "",
            "BodyObj": {
                "Body": body,
                "ImageURLs": imageURLs,
                "VideoURLs": videoURLs,
            },
            "RepostedPostHashHex": repostedPostHash,
            "PostExtraData": finalPostExtraData,
            "Sub": "",
            "IsHidden": isHidden,
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "submit-post"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def repost(
        self,
        postHashHexToRepost,
        postHashHexToModify="",
        parentStakeID="",
        postExtraData={"App": "DesoPy", "Language": "en"},
    ):

        error = None
        endpointURL = self.NODE_URL + "submit-post"
        finalPostExtraData = postExtraData
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            if "DerivedPublicKey" not in finalPostExtraData:
                finalPostExtraData[
                    "DerivedPublicKey"
                ] = self.DERIVED_PUBLIC_KEY

        payload = {
            "UpdaterPublicKeyBase58Check": self.PUBLIC_KEY,
            "PostHashHexToModify": postHashHexToModify,
            "ParentStakeID": parentStakeID,
            "Title": "",
            "BodyObj": {},
            "RepostedPostHashHex": postHashHexToRepost,
            "PostExtraData": finalPostExtraData,
            "Sub": "",
            "IsHidden": False,
            "MinFeeRateNanosPerKB": self.MIN_FEE,
            "InTutorial": False,
        }

        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "submit-post"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def quote(
        self,
        postHashHexToQuote,
        body="",
        imageURLs=[],
        videoURLs=[],
        postExtraData={"App": "DesoPy", "Language": "en"},
    ):
        error = None
        endpointURL = self.NODE_URL + "submit-post"
        finalPostExtraData = postExtraData
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            if "DerivedPublicKey" not in finalPostExtraData:
                finalPostExtraData[
                    "DerivedPublicKey"
                ] = self.DERIVED_PUBLIC_KEY

        payload = {
            "UpdaterPublicKeyBase58Check": self.PUBLIC_KEY,
            "PostHashHexToModify": "",
            "ParentStakeID": "",
            "Title": "",
            "BodyObj": {
                "Body": body,
                "ImageURLs": imageURLs,
                "VideoURLs": videoURLs,
            },
            "RepostedPostHashHex": postHashHexToQuote,
            "PostExtraData": finalPostExtraData,
            "Sub": "",
            "IsHidden": False,
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }

        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "submit-post"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def follow(self, publicKeyToFollow, isFollow=True):
        error = None
        endpointURL = self.NODE_URL + "create-follow-txn-stateless"
        payload = {
            "FollowerPublicKeyBase58Check": self.PUBLIC_KEY,
            "FollowedPublicKeyBase58Check": publicKeyToFollow,
            "IsUnfollow": not isFollow,
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "create-follow-txn-stateless"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def like(self, postHashHex, isLike=True):
        error = None
        endpointURL = self.NODE_URL + "create-like-stateless"
        payload = {
            "ReaderPublicKeyBase58Check": self.PUBLIC_KEY,
            "LikedPostHashHex": postHashHex,
            "IsUnlike": not isLike,
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }
        response = requests.post(endpointURL, json=payload)
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "create-like-stateless"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def diamond(self, postHashHex, receiverPublicKey, diamondLevel=1):
        error = None
        endpointURL = self.NODE_URL + "send-diamonds"
        payload = {
            "SenderPublicKeyBase58Check": self.PUBLIC_KEY,
            "DiamondPostHashHex": postHashHex,
            "DiamondLevel": diamondLevel,
            "ReceiverPublicKeyBase58Check": receiverPublicKey,
            "MinFeeRateNanosPerKB": self.MIN_FEE,
            "InTutorial": False,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "send-diamonds"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def updateProfile(
        self,
        FR,
        description,
        username,
        profilePicBase64,
        newStakeMultipleBasisPoint=12500,
        extraData={},
    ):
        error = None
        endpointURL = self.NODE_URL + "update-profile"
        payload = {
            "UpdaterPublicKeyBase58Check": self.PUBLIC_KEY,
            "MinFeeRateNanosPerKB": self.MIN_FEE,
            "NewCreatorBasisPoints": int(FR * 100),
            "NewDescription": description,
            "NewUsername": username,
            "NewProfilePic": profilePicBase64,
            "ExtraData": extraData,
            "NewStakeMultipleBasisPoints": newStakeMultipleBasisPoint,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "update-profile"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def sendPrivateMessage(self, receiverPublicKey, message):
        error = None
        endpointURL = self.NODE_URL + "send-message-stateless"
        payload = {
            "SenderPublicKeyBase58Check": self.PUBLIC_KEY,
            "RecipientPublicKeyBase58Check": receiverPublicKey,
            "MessageText": message,
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "send-message-stateless"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def mint(
        self,
        postHashHex,
        minBidDeSo,
        copy=1,
        creatorRoyalty=0,
        coinHolderRoyalty=0,
        isForSale=False,
        AdditionalCoinRoyaltiesMap={},
        AdditionalDESORoyaltiesMap={},
    ):
        '''
        Additional CC royalty or deso wallet royalty can be set by setting
        up AdditionalCoinRoyaltiesMap AdditionalDESORoyaltiesMap.
        It is map of PublicKey: percentage * 100.
        Example: AdditionalCoinRoyalitiesMap =
        {"BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg": 10*100}
        for setting up 10%
        '''
        error = None
        endpointURL = self.NODE_URL + "create-nft"
        if postHashHex is None:
            return None
        payload = {
            "UpdaterPublicKeyBase58Check": self.PUBLIC_KEY,
            "NFTPostHashHex": postHashHex,
            "NumCopies": copy,
            "NFTRoyaltyToCreatorBasisPoints": round(creatorRoyalty * 100),
            "NFTRoyaltyToCoinBasisPoints": round(coinHolderRoyalty * 100),
            "HasUnlockable": False,
            "IsForSale": isForSale,
            "MinBidAmountNanos": round(minBidDeSo * 1e9),
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "create-nft"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        try:
            transactionHex = response.json()["TransactionHex"]
        except Exception as e:
            raise SystemExit(e)

        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def uploadToArweave(wallet, image):
        wallet = arweave.Wallet(wallet)
        with open(image, "rb", buffering=0) as file_handler:
            tx = Transaction(
                wallet, file_handler=file_handler, file_path=image)
            file_extension = pathlib.Path(image).suffix
            type = str(file_extension[1:])
            tx.add_tag("Content-Type", "image/" + type)
            tx.sign()
            uploader = get_uploader(tx, file_handler)
            while not uploader.is_complete:
                uploader.upload_chunk()
            tx.send()
            image_id = str(tx.id)
            transaction_id = wallet.get_last_transaction_id()
            build_url = (
                "https://" + transaction_id[1:] + ".arweave.net/" + image_id
            )
            return build_url

    def updateNFT(
        self,
        postHashHex,
        buyNowPriceInDeso,
        buyNow=True,
        minBidDeso=1,
        forSale=True,
        serialNumber=1,
    ):
        error = None
        endpointURL = self.NODE_URL + "update-nft"
        payload = {
            "BuyNowPriceNanos": round(buyNowPriceInDeso * 1e9)
            if buyNow
            else round(minBidDeso * 1e9),
            "UpdaterPublicKeyBase58Check": self.PUBLIC_KEY,
            "IsBuyNow": buyNow,
            "NFTPostHashHex": postHashHex,
            "SerialNumber": serialNumber,
            "IsForSale": forSale,
            "MinBidAmountNanos": None
            if buyNow
            else round(minBidDeso * 1e9),
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "update-nft"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])
        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def burnNFT(self, postHashHex, serialNumber):
        error = None
        endpointURL = self.NODE_URL + "burn-nft"
        payload = {
            "UpdaterPublicKeyBase58Check": self.PUBLIC_KEY,
            "NFTPostHashHex": postHashHex,
            "SerialNumber": serialNumber,
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "burn-nft"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])

        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def createNFTBid(self, bidAmountDeso, NFTPostHashHex, serialNumber):
        error = None
        endpointURL = self.NODE_URL + "create-nft-bid"
        payload = {
            "UpdaterPublicKeyBase58Check": self.PUBLIC_KEY,
            "NFTPostHashHex": NFTPostHashHex,
            "SerialNumber": serialNumber,
            "BidAmountNanos": round(bidAmountDeso * 1e9),
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "create-nft-bid"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error": "Something went wrong while signing the transactions."
                " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])

        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse

    def transferNFT(self, NFTPostHashHex, receiverPublicKey, serialNumber):
        error = None
        endpointURL = self.NODE_URL + "transfer-nft"
        payload = {
            "SenderPublicKeyBase58Check": self.PUBLIC_KEY,
            "ReceiverPublicKeyBase58Check": receiverPublicKey,
            "NFTPostHashHex": NFTPostHashHex,
            "SerialNumber": serialNumber,
            "EncryptedUnlockableText": "",
            "MinFeeRateNanosPerKB": self.MIN_FEE,
        }
        try:
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.Timeout:
            endpointURL = NODES[1] + "transfer-nft"
            response = requests.post(endpointURL, json=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        transactionHex = response.json()["TransactionHex"]
        if (
            self.DERIVED_PUBLIC_KEY is not None
            and self.DERIVED_SEED_HEX is not None
            and self.SEED_HEX is None
        ):
            extraDataResponse = appendExtraData(
                transactionHex, self.DERIVED_PUBLIC_KEY, self.NODE_URL
            )
            error = extraDataResponse.json()
            transactionHex = extraDataResponse.json()["TransactionHex"]
        seedHexToSignWith = (
            self.SEED_HEX if self.SEED_HEX else self.DERIVED_SEED_HEX
        )
        try:
            signedTransactionHex = Sign_Transaction(
                seedHexToSignWith, transactionHex
            )
        except Exception as e:
            error = {
                "error":
                    "Something went wrong while signing the transactions."
                    " Make sure publicKey and seedHex are correct."
            }
            raise e(error["error"])

        submitTransactionResponse = submitTransaction(
            signedTransactionHex, self.NODE_URL
        )
        return submitTransactionResponse
