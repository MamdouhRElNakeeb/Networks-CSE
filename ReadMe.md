## CRC Algorithm Implementation


### <b>Note</b>
in <b>main.py</b> You will find a simple finite state automota(machine) with the program data flow and how it works.

To run the Program Just :
```c++
python  main.py
```
Or Use the Windows Excutable File (<b>.exe</b>) file press double click or in <b>CMD</b> write:
```
main.exe
```

run the commands as bellow : <br> 
- 1st
```
generator < file(.txt) | verify(verifier)
```

Example:
```
generator < test1 | verify
```
<p>This Command will generate a file (transmitted_msg.txt) -> (Generator Part) 
& a Correct or uncorrect message -> (Verification Part)</p>


- 2nd 
```
generator < file(.txt) | alter(invert) (num) | verify(verifier)
```


Example:
```
generator < test1 | alter 3 | verify
```
<p>This Command will generate a file (transmitted_msg_alter.txt) -> (Generator Part) 
& a Correct or uncorrect message -> (Verification Part)</p>



<b>Note :</b> you can type filename with <strong>.txt</strong> or just the name of it.









