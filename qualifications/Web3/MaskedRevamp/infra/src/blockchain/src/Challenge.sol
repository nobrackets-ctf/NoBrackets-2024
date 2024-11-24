// SPDX-License-Identifier: UNLICENSED

/// Title: Masked
/// Author: K.L.M
/// Difficulty: Medium / Hard


pragma solidity ^0.8.0;

contract Challenge {

    bool public Solved = false;
    address public Admin;

    modifier OnlyAdmin{
        require(msg.sender == Admin, "Passage interdit");
        _;
    }

    function defuse(uint guess) OnlyAdmin public {
        if (guess == block.timestamp){
            Solved = true;
        }
    }

    function changeOwner() public {
        Admin = msg.sender;
    }

    function isSolved() public view returns(bool){
        return Solved;
    }
}