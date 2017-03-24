snmptable -v 2c -c mak30v3r -m /home/u1069621/ENTITY-MIB.txt -Cf , CATRN10-09MR01 1.3.6.1.2.1.47.1.1.1 | cut -d "," -f 1,4,10,12,13 | sed -n '1,3d;p' | head -n 5

