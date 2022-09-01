delimiter @@ 
create procedure res(in city varchar(40))
begin
declare a varchar(40);
set a=city;
select CUST_NAME from customer where WORKING_AREA=a;
end
@@
call res("Bangalore")@@

