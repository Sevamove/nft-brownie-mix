// SPDX-Licence-Identifier: MIT
pragma solidity >=0.8.7 <0.8.12;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract NFT is 
    ERC721,           /* Non-Fungible Token Standard */
    Ownable,          /* Simple mechanism with a single account authorized for all privileged actions. */
    ERC721Royalty,    /* A standardized way to retrieve royalty payment information. */
    ERC721Burnable,   /* Token holders will be able to destroy their tokens. */
    ERC721Enumerable, /* Allows on-chain enumeration of all tokens or those owned by an account. */
    ERC721URIStorage  /* We use it to store an item's metadata. */
{
    /// @dev Counter that can only be incremented, decremented or reset.
    using Counters for Counters.Counter;

    /// @dev Current amount of minted NFTs.
    Counters.Counter private _tokenIds;

    address royaltyAddress;
    uint96 royaltyFeesInBips;
    string public contractURI;

    /// @dev Events of the contract.
    event Minted(
        uint256 indexed _tokenId,
        address _beneficiary,
        string _tokenURI,
        address _minter
    );
    event SetTokenURI(uint256 indexed _tokenId, string _tokenURI);

    /// @notice Contract constructor.
    constructor(
        string memory _name,
        string memory _symbol,
        uint96 _royaltyFeesInBips
    ) ERC721(_name, _symbol) {
        royaltyAddress = owner();
        royaltyFeesInBips = _royaltyFeesInBips;
        setRoyaltyInfo(owner(), royaltyFeesInBips);
    }

    /**
     * @dev Safely mints new token ID and transfers it to `_to`.
     * @param _to The owner of the new token ID.
     * @param _tokenURI URI metadata that belongs to token ID.
     */
    function safeMint(address _to, string memory _tokenURI) public onlyOwner {

        // Valid args.
        _assertMintingParamsValid(_tokenURI, _msgSender());

        _tokenIds.increment();
        uint256 tokenId = _tokenIds.current();

        // Mint token and set token URI.
        _safeMint(_to, tokenId);
        _setTokenURI(tokenId, _tokenURI);

        emit Minted(tokenId, _to, _tokenURI, _msgSender());
        emit SetTokenURI(tokenId, _tokenURI);
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
    function setRoyaltyInfo(address _receiver, uint96 _royaltyFeesInBips) public onlyOwner {
        royaltyAddress = _receiver;
        royaltyFeesInBips = _royaltyFeesInBips;
        _setDefaultRoyalty(_receiver, _royaltyFeesInBips);
    }

    ////////////////////
    /// VIEW METHODS
    ////////////////////

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

    /**
     * @notice Returns how much royalty is owed and to whom.
     * @param _tokenId Token ID of the generated art.
     * @param _salePrice Sale price of that token ID.
     */
    function royaltyInfo(uint256 _tokenId, uint256 _salePrice)
        external
        view
        override
        returns (address receiver, uint256 royaltyAmount)
    {
        royaltyAmount = (_salePrice * royaltyFeesInBips) / _feeDenominator() + _tokenId * 0;
        return (royaltyAddress, royaltyAmount);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Royalty, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    /////////////////////////////////
    /// INTERNAL AND PRIVATE METHODS
    /////////////////////////////////
    
    /**
     * @notice Checks that the URI is not empty and the designer is a real address.
     * @param _tokenURI URI supplied on minting.
     * @param _artist Address supplied on minting.
     */
    function _assertMintingParamsValid(string memory _tokenURI, address _artist) pure internal {
        require(bytes(_tokenURI).length > 0, "_assertMintingParamsValid: Token URI is empty.");
        require(_artist != address(0), "_assertMintingParamsValid: Artist is zero address.");
    }

    // ERC-2981
    function setTokenRoyalty(uint256 _tokenId, address _receiver, uint96 _royaltyFeesInBips)
        internal
        onlyOwner
    {
        _setTokenRoyalty(_tokenId, _receiver, _royaltyFeesInBips);
    }

    /**
     * @notice Destroys token ID. The approval is cleared when the token is burned.
     * @notice Override additionally clears the royalty information for the token.
     * @param tokenId Token ID to burn.
     */
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
}
