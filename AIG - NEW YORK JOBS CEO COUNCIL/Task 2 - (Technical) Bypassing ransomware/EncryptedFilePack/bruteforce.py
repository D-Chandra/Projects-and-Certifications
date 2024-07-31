'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
# def attempt_extract(zf_handle, password):
#     
#
#

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for data in f:
                password = data.strip()
                try:
                    zf.extractall(pwd=password)
                    print('Encryption Key Found :', password)
                    break
                except(RuntimeError):
                    continue
            else:
                print('Unable to find Decrypt file')

            


            # Attempt to extract the zip file using each password

            # Handle correct password extract versus incorrect password attempt)

    #print("[+] Password not found in list")

if __name__ == "__main__":
    main()