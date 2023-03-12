alphabet=['a','b','c','d','e','f','g','h','i','j','k','l',
  'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction =input("Type'encode' to encrypt ,Type'decode'to decrypt \n").lower()
txt = input("Type your message:\n ").lower()
shift =int(input("Type the shift number\n"))
def encrypt(Plain_txt ,shift_amount):
 cipher_text=""
 for letter in Plain_txt:
     position=alphabet.index(letter) 
     new_position =position +shift_amount
     new_letter =alphabet [new_position]
     cipher_text +=new_letter
 print(f"The encoded text is {cipher_text}")
     



def decrypt(cipher_text ,shift_amount):
 Plain_text=""
 for letter in cipher_text:
     position=alphabet.index(letter) 
     new_position =position-shift_amount
     Plain_text += alphabet [new_position]
    
 print(f"The decoded text is {Plain_text}")



if direction =="encode":
    encrypt(Plain_txt=txt,shift_amount=shift)
elif direction =="decode":
    decrypt(cipher_text=txt,shift_amount=shift)