## Create an ERC20
- https://dev.to/stermi/how-to-create-an-erc20-token-and-a-solidity-vendor-contract-to-sell-buy-your-own-token-4j1m

## Tokens
- These tokens represent fungible and tradable assets or utilities that reside on their own blockchains
- These tokens are usually created, distributed, sold, and circulated through the standard initial coin offering (ICO) process, which involves a crowdfunding exercise to fund project development.

## How Crypto Tokens Work
- Cryptocurrencies or virtual currencies are denominated into these tokens, which reside on their own blockchains.

### These ERC Ethereum standards are the most well-known and popular 

    ERC - 20
    ERC - 721
    ERC - 1155
    ERC - 777

- (https://dev.to/envoy_/ks-what-are-ethereum-request-for-comments-erc-standards-5f80)


## How ERC-20 Tokens Work
- ERC-20 tokens are created with Ethereum smart contracts.
- Ethereum allows developers to write applications that run on the blockchain with smart contracts, which encapsulate all of the business logic of these applications.
- In the case of an ERC-20 token, the smart contract governs all of the behavior about how the token works, and keeps track of token ownership and account balances.
- ERC-20 is an API specification for how Ethereum tokens should be built.
- It dictates certain events that our token must have, like a transfer event
- smart contracts can emit events that consumers can subscribe to, and with this standard, we can subscribe to events that tell us when tokens are sold.

```
    contract ERC20Token {
        // ...

        function transfer(address _to, uint256 _value) public returns (bool success) {
            require(balanceOf[msg.sender] >= _value);

            balanceOf[msg.sender] -= _value;
            balanceOf[_to] += _value;

            Transfer(msg.sender, _to, _value);

            return true;
        }

        // ...
    }
```

- Artile (https://www.dappuniversity.com/articles/code-your-own-cryptocurrency-on-ethereum) 

- (https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md)
