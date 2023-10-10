import subprocess
result1=subprocess.run(["python3","fetcher.py","isbn_names.txt","0","2000"],capture_output=True,text=True)
result2=subprocess.run(["python3","fetcher.py","isbn_names.txt","2000","4000"],capture_output=True,text=True)
result3=subprocess.run(["python3","fetcher.py","isbn_names.txt","4000","6000"],capture_output=True,text=True)
result4=subprocess.run(["python3","fetcher.py","isbn_names.txt","6000","8000"],capture_output=True,text=True)
result5=subprocess.run(["python3","fetcher.py","isbn_names.txt","8000","10000"],capture_output=True,text=True)
result6=subprocess.run(["python3","fetcher.py","isbn_names.txt","10000","12000"],capture_output=True,text=True)
result7=subprocess.run(["python3","fetcher.py","isbn_names.txt","12000","14000"],capture_output=True,text=True)
result8=subprocess.run(["python3","fetcher.py","isbn_names.txt","14000","16000"],capture_output=True,text=True)
result9=subprocess.run(["python3","fetcher.py","isbn_names.txt","16000","18000"],capture_output=True,text=True)
result10=subprocess.run(["python3","fetcher.py","isbn_names.txt","18000","20000"],capture_output=True,text=True)
result11=subprocess.run(["python3","fetcher.py","isbn_names.txt","20000","22000"],capture_output=True,text=True)
result12=subprocess.run(["python3","fetcher.py","isbn_names.txt","22000","24208"],capture_output=True,text=True)


results=[result1.stdout,result2.stdout,result3.stdout,result4.stdout,result5.stdout,result6.stdout,result7.stdout,result8.stdout,result9.stdout,result10.stdout,result11.stdout,result12.stdout]

for i in range(1,13):
    with open(f"./logs/out{i}.txt","w") as file:
        file.write(results[i-1])
        print(f"log written to ./logs/out{i}.txt")

print("data scrapped succesfully")

