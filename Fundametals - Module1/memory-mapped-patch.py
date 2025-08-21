# Open a large binary file with mmap, locate all occurrences of the byte sequence b"\x90\x90\x90\x90", and overwrite them with b"\xCC\xCC\xCC\xCC".  

import mmap 

with open('largefile.bin', 'r+b') as f: 
    mm = mmap.mmap(f.fileno(), 0) 
    target = b"\x90\x90\x90\x90" 
    replacement = b"\xCC\xCC\xCC\xCC"
    pos = mm.find(target)
    while pos != -1:
        mm[pos:pos+len(target)]=replacement
        pos=mm.find(target, pos+len(replacement)) 
    mm.flush()
    mm.close()