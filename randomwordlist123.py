output_file = "wordlist.txt" 
 
 # ubah sesuai value
with open(output_file, "w") as file: 
    for i in range(1, 100001):  
        file.write(f"{i:04d}\n")   
 
print(f"Wordlist: {output_file}")