# Welcome - K.L.M

## Contrat

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Challenge {

    bool public solved = false;

    function win(string memory answer) public {
        if (keccak256(abi.encodePacked(answer)) == keccak256(abi.encodePacked("Welcome to the final !")))
        {
            solved = true;
        }
    }

    function isSolved() public view returns(bool){
        return solved;
    }
}
```

## Solve
Facile :)) Contrat d'attaque:

```solidity
contract Attack {

    address public challenge;

    function setChallenge(address _challenge) public {
        challenge = _challenge;
    }

    function attack() public {
        (bool success, ) = challenge.call(abi.encodeWithSignature("win(string)", "Welcome to the final !"));
        require(success, "call failed");
    }
}
```

```bash
mkdir atksrc
cd atksrc
forge init
rm src/* test/* script/*
mv atk.sol src/
forge build
forge create src/atk.sol:Attack --rpc-url $RPC --private-key $PK

Ensuite, on utilisera $ATK comme variable contenant l'adresse de notre contrat d'attaque.
```

```bash
cast send $ATK "setChallenge(address)" $TAR -r $RPC --private-key $PK
cast send $ATK "attack()" -r $RPC --private-key $PK
cast call $TAR "isSolved()(bool)" -r $RPC
True
```

Win !