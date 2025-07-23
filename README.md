## Mariner needs to be in charge of own faith. Be it start of a career, reimbursement, savings or pension plan! Public development, inspection and security protection.

## People at sea need to be assured their payments come and go whenever and whoever they decided to! #BTC #LTC #SOL based solution to perform quick assets transfer for people involved in marine industry. Strict security and contract confirmation by several parties is a corner stone of the product. Many nationalities suffer from company/bank/government compliance misinterpretation. Not always if favor of a person in trouble. This environment is about to change mariner's business relations with above stated authorities. No more lost assets, pension plans or stolen money aboard the vessel!
## Be the one in possession, decision making and fully in charge of your payments!

## There is a secure bank/financial service gateway to momentarily invoice/transfer assets between desired purposes.

## Starting from the beginning of building your career. When youngster is out of personal savings and needs to built life from a scratch. 

## Dropping your anchor ashore when your pension plan is full of earned miles and achievements and you need to save and pass over your assets without giving a second chance to ANY third party in the world.

## The answer is anchored here.

# ASAIL - Atomic Swap and Interoperability Layer

## Overview
ASAIL enables atomic swaps between **Bitcoin**, **Litecoin**, and **Solana**. The system uses **Hash Time-Locked Contracts (HTLCs)** for Bitcoin and Litecoin, and **Solana smart contracts** to facilitate secure and trustless swaps between these blockchains.

## Features
- **Cross-chain atomic swaps** between Bitcoin, Litecoin, and Solana.
- **HTLC support** for Bitcoin and Litecoin.
- **Solana smart contracts** for locking/unlocking funds.
- **Cross-chain communication** via a custom or existing bridge (Wormhole).
  
## Folder Structure
- **contracts/**: Solana smart contract code.
- **btc-litecoin/**: Python scripts for Bitcoin and Litecoin HTLCs.
- **solana/**: Solana-specific code for swaps.
- **bridge/**: Code for cross-chain communication.
- **docs/**: Project documentation.

## Installation
1. **Install Dependencies**:
   - **Python**: `pip install bitcoinlib pycoind solana`
   - **Solana**: Install Solana CLI and SDK following official documentation.

2. **Deploy Solana contract**:
   - Navigate to `contracts/` and deploy the Solana smart contract using `solana deploy`.

3. **Run Tests**:
   ```bash
   pytest tests/test_btc_ltc_swap.py
   pytest tests/test_solana_swap.py

