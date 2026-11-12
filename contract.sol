
pragma solidity ^0.4.19;

contract MyContract {

    address private owner;

    // Constructor
    constructor() public {
        owner = msg.sender;
    }

    // Get owner's address
    function getOwner() public view returns (address) {
        return owner;
    }

    // Get owner's balance
    function getbalance() public view returns (uint256) {
        return owner.balance;
    }

    // Deposit exactly 2 ETH
    function deposit() external payable {
        require(msg.value == 2 ether, "Please send two ethers");
    }

    // Withdraw contract balance
    function withdraw() external {
        require(msg.sender == owner, "No");
        msg.sender.transfer(address(this).balance);
    }
}
