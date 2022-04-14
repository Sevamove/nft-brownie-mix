// SPDX-Licence-Identifier: MIT
pragma solidity >=0.8.7 <0.8.12;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

error ProvidedIdenticalTokenURI(uint256 _tokenId, string _tokenURI);

contract Collectible is 
    ERC721,
    Ownable,
    Pausable,
    ERC721Royalty,
    ERC721Burnable,
    ERC721URIStorage,
    ERC721Enumerable
{
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    string public contractURI;

    address royaltyReceiver;
    uint96 royaltyFraction; // e.g. 100 (1%); 1000 (10%)

    constructor(
        string memory _name,
        string memory _symbol,
        string memory _contractURI,
        address _royaltyReceiver,
        uint96 _royaltyFraction
    ) ERC721(_name, _symbol) {
        contractURI = _contractURI;
        royaltyReceiver = _royaltyReceiver;
        royaltyFraction = _royaltyFraction;

        setDefaultRoyalty(royaltyReceiver, royaltyFraction);
    }

    event Minted(address _to, uint256 _tokenId, string _tokenURI);
    event SetTokenURI(uint256 _tokenId, string _tokenURI);
    event SetDefaultRoyalty(address _receiver, uint96 _fraction);
    event SetTokenRoyalty(uint256 _tokenId, address _receiver, uint96 _fraction);
    event DeletedDefaultRoyalty();
    event ResetTokenRoyalty(uint256 _tokenId);

    modifier isValidTokenURI(uint256 _tokenId, string memory _tokenURI) {
        bytes32 bTokenURI = keccak256(bytes(_tokenURI));
        
        require(
            bTokenURI.length > 0,
            "validTokenURI: Token URI can not be empty string."
        );

        if (_tokenId != 0) {
            bytes32 bExistingTokenURI = keccak256(bytes(tokenURI(_tokenId)));

            if (bTokenURI == bExistingTokenURI) {
                revert ProvidedIdenticalTokenURI(_tokenId, _tokenURI);
            }
        }
        _;
    }

    function pause() public onlyOwner {_pause();}

    function unpause() public onlyOwner {_unpause();}

    function setContractURI(string memory _contractURI) public onlyOwner {
        contractURI = _contractURI;
    }

    function safeMint(address _to, string memory _tokenURI)
        public
        onlyOwner
        isValidTokenURI(_tokenIdCounter.current(), _tokenURI)
    {
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(_to, tokenId);
        _setTokenURI(tokenId, _tokenURI);
        emit Minted(msg.sender, tokenId, _tokenURI);
    }

    function setTokenURI(uint256 _tokenId, string memory _tokenURI)
        public
        onlyOwner
        isValidTokenURI(_tokenId, _tokenURI)
    {
        require(
            _isApprovedOrOwner(msg.sender, _tokenId),
            "ERC721: caller is not allowed to manage token ID."
        );
        _setTokenURI(_tokenId, _tokenURI);
        emit SetTokenURI(_tokenId, _tokenURI);
    }

    function setDefaultRoyalty(address _receiver, uint96 _feeNumerator)
        public
        onlyOwner
    {
        royaltyReceiver = _receiver;
        royaltyFraction = _feeNumerator;
        _setDefaultRoyalty(_receiver, _feeNumerator);
        emit SetDefaultRoyalty(_receiver, _feeNumerator);
    }

    function setTokenRoyalty(
        uint256 _tokenId,
        address _receiver,
        uint96 _feeNumerator
    ) 
        public
        onlyOwner
    {
        require(
            _isApprovedOrOwner(msg.sender, _tokenId),
            "ERC721: caller is not allowed to manage token ID."
        );
        _setTokenRoyalty(_tokenId, _receiver, _feeNumerator);
        emit SetTokenRoyalty(_tokenId, _receiver, _feeNumerator);
    }

    function deleteDefaultRoyalty() public onlyOwner {
        _deleteDefaultRoyalty();
        emit DeletedDefaultRoyalty();
    }

    function resetTokenRoyalty(uint256 _tokenId)
        public
        onlyOwner
    {
        _resetTokenRoyalty(_tokenId);
        emit ResetTokenRoyalty(_tokenId);
    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage, ERC721Royalty)
    {
        require(_exists(tokenId), "Token ID set of nonexistent token.");
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
    
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable, ERC721Royalty)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}


