import code as x 
import threading as Thread
_db_lock=Thread.Lock()

x.create("rani",50)
x.create("src",70,3600) 
x.read("rani")
x.read("src")
x.create("rani",70)
x.modify("rani",75)
x.delete("rani")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
