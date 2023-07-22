set schema 'shopify';

begin transaction;

update apps set developer = 'Shopify Technology' where developer = 'Shopify';

update categories set title = 'Finances & Accounting' where id = '26a72de0d02e0e4e5f615332d61a878e';

commit;