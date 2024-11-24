# HiddenContract - K.L.M

On a un bytecode, on fonce sur notre decompiler préféré :))

```Solidity
function function_selector() public payable { 
    MEM[64] = 128;
    0x293(0, 'NBCTF{Y0U_F0UND_M3?}');
    require(!msg.value);
```

On lit le flag directement, Facile !