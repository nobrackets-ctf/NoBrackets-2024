// SPDX-License-Identifier: MIT

/// Title: SuperVision
/// Author: K.L.M
/// Difficulty: Easy


pragma solidity ^0.8.0;

contract Challenge {
    bool public Solved = false;
    string private constant TARGET_STRING = "Bienvenue au No Brackets CTF 2024";

    function verifyString(string memory inputString) public {
        if (keccak256(abi.encodePacked(inputString)) == keccak256(abi.encodePacked(TARGET_STRING))) {
            Solved = true;
        }
    }

    function isSolved() public view returns(bool){
        return Solved;
    }
}
