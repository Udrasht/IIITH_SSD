delimiter @@
create procedure q4() 
begin 
declare nm varchar(50);
declare done int default 0; 
declare city varchar(50); 
declare country varchar(50); 
declare gr decimal(10,0); 
declare cur_1 cursor for select CUST_NAME,WORKING_AREA,CUST_COUNTRY,GRADE from customer where AGENT_CODE like "A00%"; 
declare continue handler for not found set done=1; 
open cur_1;
get_stud:loop 
fetch cur_1 into nm,city,country,gr; 
select nm,city,country,gr;
if done=1 then leave get_stud; 
end if; 
end loop get_stud;
close cur_1; 
end@@
call q4()@@
