// SPDX-Licence-Identifier: MIT
pragma solidity >=0.8.7 <0.8.12;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract NFT is ERC721, Ownable, ERC721Royalty, ERC721Burnable, ERC721Enumerable, ERC721URIStorage {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIds;

    address royaltyAddress;
    uint96 royaltyFeesInBips;
    string public contractURI;

    event CreatedNFT(uint256 indexed _tokenId);
    event SetTokenURI(uint256 indexed _tokenId, string _tokenURI);

    constructor(
        string memory _name,
        string memory _symbol,
        uint96 _royaltyFeesInBips
    ) ERC721(_name, _symbol) {
        royaltyAddress = owner();
        royaltyFeesInBips = _royaltyFeesInBips;
        setRoyaltyInfo(owner(), royaltyFeesInBips);
    }

    function safeMint(address _to, string memory _tokenURI) public onlyOwner {
        _tokenIds.increment();
        uint256 tokenId = _tokenIds.current();
        _safeMint(_to, tokenId);
        _setTokenURI(tokenId, _tokenURI);
        emit CreatedNFT(tokenId);
    }

    function getTokenIds() public view returns (uint256) {
        return _tokenIds.current();
    }

    function getContractURI() public view returns (string memory) {
        return contractURI;
    }

    function getTokenExists(uint256 _tokenId) public view returns (bool) {
        bool tokenExists = _exists(_tokenId);
        return tokenExists;
    }

    function getTokenOwner(uint256 _tokenId) public view returns (address) {
        address _tokenOwner = ownerOf(_tokenId);
        return _tokenOwner;
    }

    function setContractURI(string memory _contractURI) public onlyOwner {
        contractURI = _contractURI;
    }

    function setTokenURI(uint256 _tokenId, string memory _tokenURI)
        public
        onlyOwner
    {
        require(
            _isApprovedOrOwner(_msgSender(), _tokenId), 
            "ERC721: caller is not owner nor approved"
        );
        _setTokenURI(_tokenId, _tokenURI);
        emit SetTokenURI(_tokenId, _tokenURI);
    }

    // ERC-2981
    function setTokenRoyalty(uint256 _tokenId, address _receiver, uint96 _royaltyFeesInBips)
        internal
        onlyOwner
    {
        _setTokenRoyalty(_tokenId, _receiver, _royaltyFeesInBips);
    }

    // ERC-2981
    function setRoyaltyInfo(address _receiver, uint96 _royaltyFeesInBips) public onlyOwner {
        royaltyAddress = _receiver;
        royaltyFeesInBips = _royaltyFeesInBips;
        _setDefaultRoyalty(_receiver, _royaltyFeesInBips);
    }

    function royaltyInfo(uint256 _tokenId, uint256 _salePrice)
        external
        view
        override
        returns (address receiver, uint256 royaltyAmount)
    {
        royaltyAmount = (_salePrice * royaltyFeesInBips) / _feeDenominator() + _tokenId * 0;
        return (royaltyAddress, royaltyAmount);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        require(
            _exists(tokenId),
            "ERC721Metadata: URI query for nonexistent token"
        );
        return super.tokenURI(tokenId);
    }

    function _burn(uint256 tokenId)
        internal
        virtual
        override(ERC721, ERC721Royalty, ERC721URIStorage)
        onlyOwner
    {
        super._burn(tokenId);
        _resetTokenRoyalty(tokenId);
    }

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Royalty, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
