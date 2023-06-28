#This is a blockchain simulation program

#Import library
import hashlib

#Create Block class
class Block:
  #Defining variables within Block Class
  def __init__(self, data, prev_hash):
    #Setting values and names to the variables
    self.data = data
    self.prev_hash = prev_hash
    #Setting value to a new method to calculate hash of block
    self.hash = self.calc_hash()

  #Create a hash calculation method using SHA-256
  def calc_hash(self):
    #Converts data into a string of 256 bits
    sha = hashlib.sha256()
    #Encode data into 8 bits
    sha.update(self.data.encode('utf-8'))
    return sha.hexdigest()


#Create the Blockchain class
class Blockchain:
  #Create a constructor for the Blockchain class
  def __init__(self):
    self.chain = [self.create_genesis_block()]

  #Method to create genesis block
  def create_genesis_block(self):
    #Imputs data as genesis block and 0 previous hashes
    return Block("Genesis Block", "0")

  #Create a method that creates a new block and adds it to the Blockchain (List)
  def add_block(self, data):
    #Holds data of previous block
    prev_block = self.chain[-1]
    #New block consisting of data and hashrate of previous block
    new_block = Block(data, prev_block.hash)
    #Adds new block to the Blockchain
    self.chain.append(new_block)


#Test the Blockchain
blockchain = Blockchain()

#Add blocks to the blockhain
blockchain.add_block('First block')
blockchain.add_block('Second block')
blockchain.add_block('Third block')

#Print and show the blockchian
print('Blockchain: ')
for block in blockchain.chain:
  print('Data:', block.data)
  print('Previous hash:', block.prev_hash)
  print('Hash:', block.hash)
  print()

