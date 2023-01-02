## Prerequisite
- CURL
- Docker
- Docker-Compose
- Go
- Node.js and NPM
- Python 2.7
- git config --global core.autocrlf false
- git config --global core.longpaths true


## Setup
    curl -sSL http://bit.ly/2ysbOFE | bash -s
    cd fabric-samples/test-network
    ./network.sh down
    ./network.sh up
    docker ps -a

### Creating Channel
    ./network.sh up createChannel -c mychannel -ca

### Deploying Smart Contract
    ./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-typescript/ -ccl typescript


### Follow This for creating and running application  
- https://hyperledger-fabric.readthedocs.io/en/latest/write_first_app.html#prepare-the-sample-application