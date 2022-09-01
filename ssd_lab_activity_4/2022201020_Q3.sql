delimiter @@
create procedure sys() 
begin 
select CUST_NAME,GRADE from customer where RECEIVE_AMT+OPENING_AMT>10000; 
end@@
call sys()@@
