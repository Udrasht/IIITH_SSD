delimiter @@
create procedure addnum(in n1 int,in n2 int,out res int)
begin
declare a1 int;
declare a2 int;
set a1=n1;
set a2=n2;
set res=a1+a2;
end@@
CALL addnum(4,5,@out_value);
@@
SELECT @out_value@@
