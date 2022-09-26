import psutil;

for i in psutil.process_iter(['name', 'status']):
    
    if i.info['status'] == 'running':
        
        print(i.info)