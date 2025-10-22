import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, farmer_name, crop_type, quantity, price, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.farmer_name = farmer_name
        self.crop_type = crop_type
        self.quantity = quantity
        self.price = price
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": str(self.timestamp),
            "farmer_name": self.farmer_name,
            "crop_type": self.crop_type,
            "quantity": self.quantity,
            "price": self.price,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": str(self.timestamp),
            "farmer_name": self.farmer_name,
            "crop_type": self.crop_type,
            "quantity": self.quantity,
            "price": self.price,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, datetime.now(), "System", "Genesis", 0, 0, "0")
        self.chain.append(genesis_block)
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_transaction(self, farmer_name, crop_type, quantity, price):
        index = len(self.chain)
        timestamp = datetime.now()
        previous_hash = self.get_latest_block().hash
        new_block = Block(index, timestamp, farmer_name, crop_type, quantity, price, previous_hash)
        self.chain.append(new_block)
        return new_block
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    def get_all_transactions(self):
        return [block.to_dict() for block in self.chain[1:]]
    
    def get_statistics(self):
        if len(self.chain) <= 1:
            return {
                "total_transactions": 0,
                "total_volume": 0,
                "crops_summary": {},
                "total_value": 0
            }
        
        total_volume = 0
        total_value = 0
        crops_summary = {}
        
        for block in self.chain[1:]:
            total_volume += block.quantity
            total_value += block.quantity * block.price
            
            if block.crop_type in crops_summary:
                crops_summary[block.crop_type]["quantity"] += block.quantity
                crops_summary[block.crop_type]["count"] += 1
            else:
                crops_summary[block.crop_type] = {
                    "quantity": block.quantity,
                    "count": 1
                }
        
        return {
            "total_transactions": len(self.chain) - 1,
            "total_volume": total_volume,
            "crops_summary": crops_summary,
            "total_value": total_value
        }
