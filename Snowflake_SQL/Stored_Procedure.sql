create or replace procedure customer_upsert_sp()
returns varchar
language sql
execute as owner
as
$$
declare
    v_rows_merged number :=0;
begin
    merge into customers t
    using (
        select distinct CUSTOMER_ID,FIRST_NAME,LAST_NAME,EMAIL,CITY,PURCHASE_AMOUNT,PURCHASE_DATE from raw_customers
    ) s
    on t.customer_id = s.customer_id
    when matched then
        update set
            t.FIRST_NAME=s.FIRST_NAME,
            t.LAST_NAME=s.LAST_NAME,
            t.EMAIL=s.EMAIL,
            t.CITY=s.CITY,
            t.PURCHASE_AMOUNT=s.PURCHASE_AMOUNT,
            t.PURCHASE_DATE=s.PURCHASE_DATE
    when not matched then
        insert (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, CITY, PURCHASE_AMOUNT, PURCHASE_DATE)
        values(s.CUSTOMER_ID, s.FIRST_NAME, s.LAST_NAME, s.EMAIL, s.CITY, s.PURCHASE_AMOUNT, s.PURCHASE_DATE);

v_rows_merged := SQLROWCOUNT;

insert into customer_load_log (LOG_TIMESTAMP, STATUS, ERROR_MESSAGE) values (current_timestamp(), 'SUCCESS -' || :v_rows_merged || ' rows merged', NULL);

return 'Upsert completed successfully: '|| v_rows_merged ||' rows merged';

exception
    when other then
        insert into CUSTOMER_LOAD_LOG (LOG_TIMESTAMP, STATUS, ERROR_MESSAGE) values (current_timestamp(), 'FAILED', :SQLERRM);
        return 'Upsert failed: ' || :SQLERRM;
end;
$$