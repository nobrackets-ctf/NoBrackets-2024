// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

contract Challenge {
    mapping(address => uint256) public balances;
    address public admin;
    bool public Solved = false;

    constructor() {
        admin = msg.sender; // Initial admin est le déployeur du contrat
    }

    // Fonction pour ajouter des tokens à un compte
    function deposit(uint256 amount) internal{
        balances[msg.sender] += amount;
    }

    // Fonction pour retirer des tokens
    function withdraw(uint256 amount) public {
        balances[msg.sender] -= amount;
    }

    // Fonction pour promouvoir quelqu'un en admin si sa balance est supérieure à 1 million de tokens
    function promote() public {
        require(balances[msg.sender] > 1_000_000, "Not enough balance to promote");
        admin = msg.sender;
        Solved = true;
    }

    function isSolved() public view returns(bool){
        return Solved;
    }

    receive() external payable {
        deposit(msg.value);
    }
}
